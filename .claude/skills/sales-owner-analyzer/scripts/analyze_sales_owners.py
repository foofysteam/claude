#!/usr/bin/env python3
"""
Sales Owner Analyzer Script
Analyzes Project Pipeline database and generates action notes for each sales owner.
"""

import json
import sys
from datetime import datetime, timedelta
from collections import defaultdict

# Configuration
PIPELINE_DATABASE_ID = "1a52dee8-423c-8039-a133-fabfd3370fd8"
OUTPUT_PAGE_ID = "2b12dee8-423c-80be-9959-e86cbf3d00d4"

# Analysis thresholds (in days)
STALE_UPDATE_DAYS = 7  # No update in X days = stale
URGENT_PAYMENT_DAYS = 14  # Payment pending for X days = urgent
MEETING_NEEDED_DAYS = 10  # No meeting scheduled in X days = needs meeting

def parse_date(date_str):
    """Parse ISO date string to datetime object."""
    if not date_str:
        return None
    try:
        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    except:
        return None

def days_since(date_str):
    """Calculate days since a given date."""
    if not date_str:
        return float('inf')
    date = parse_date(date_str)
    if not date:
        return float('inf')
    return (datetime.now(date.tzinfo) - date).days

def analyze_project(project, owner_name):
    """Analyze a single project and return issues found."""
    issues = {
        'no_status_update': False,
        'needs_followup_payment': False,
        'needs_meeting': False,
        'needs_closing': False,
        'missing_data': [],
        'project_name': None,
        'deal_value': None,
        'status': None,
        'last_update': None
    }
    
    props = project.get('properties', {})
    
    # Extract project name
    title_prop = props.get('Project Name') or props.get('Name') or props.get('name') or {}
    if title_prop.get('title'):
        issues['project_name'] = ''.join([t.get('plain_text', '') for t in title_prop['title']])
    
    # Extract status
    status_prop = props.get('Status') or props.get('status') or {}
    if status_prop.get('select'):
        issues['status'] = status_prop['select'].get('name')
    elif status_prop.get('status'):
        issues['status'] = status_prop['status'].get('name')
    
    # Extract deal value
    value_prop = props.get('Deal Value') or props.get('Value') or props.get('Amount') or {}
    if value_prop.get('number'):
        issues['deal_value'] = value_prop['number']
    
    # Check last edited time
    issues['last_update'] = project.get('last_edited_time')
    days_stale = days_since(issues['last_update'])
    
    # Analysis logic
    status_lower = (issues['status'] or '').lower()
    
    # 1. No status update check
    if days_stale > STALE_UPDATE_DAYS and status_lower not in ['won', 'lost', 'completed', 'closed']:
        issues['no_status_update'] = True
    
    # 2. Payment followup needed
    payment_keywords = ['payment', 'pending', 'invoice', 'collection', 'billing']
    if any(kw in status_lower for kw in payment_keywords):
        issues['needs_followup_payment'] = True
    
    # Check payment-related properties
    payment_status = props.get('Payment Status') or props.get('Payment') or {}
    if payment_status.get('select'):
        payment_val = payment_status['select'].get('name', '').lower()
        if payment_val in ['pending', 'partial', 'overdue', 'not received']:
            issues['needs_followup_payment'] = True
    
    # 3. Needs closing (ready projects not moving)
    closing_keywords = ['quotation sent', 'proposal sent', 'negotiation', 'customer ready', 'design approved']
    if any(kw in status_lower for kw in closing_keywords) and days_stale > 5:
        issues['needs_closing'] = True
    
    # Check Customer Ready property
    customer_ready = props.get('Customer Ready') or {}
    if customer_ready.get('checkbox') and status_lower not in ['won', 'lost', 'in production', 'completed']:
        issues['needs_closing'] = True
    
    # 4. Needs meeting
    meeting_keywords = ['initial contact', 'lead', 'follow up', 'waiting', 'no response']
    if any(kw in status_lower for kw in meeting_keywords) and days_stale > MEETING_NEEDED_DAYS:
        issues['needs_meeting'] = True
    
    # Check next step property
    next_step = props.get('Next Step') or props.get('Next Steps') or {}
    if next_step.get('rich_text'):
        next_text = ''.join([t.get('plain_text', '') for t in next_step['rich_text']]).lower()
        if 'meeting' in next_text or 'call' in next_text or 'visit' in next_text:
            issues['needs_meeting'] = True
    
    # 5. Missing data checks
    if not issues['project_name']:
        issues['missing_data'].append('Project Name')
    
    billing_name = props.get('Billing Name') or props.get('Client') or {}
    if not billing_name.get('rich_text') and not billing_name.get('title'):
        issues['missing_data'].append('Billing Name')
    
    contact = props.get('Contact') or props.get('Phone') or props.get('Customer Contact') or {}
    if not contact.get('phone_number') and not contact.get('rich_text'):
        issues['missing_data'].append('Contact')
    
    return issues

def group_projects_by_owner(projects):
    """Group projects by sales owner."""
    owners = defaultdict(list)
    
    for project in projects:
        props = project.get('properties', {})
        
        # Try different property names for owner
        owner_prop = props.get('Sales Owner') or props.get('Owner') or props.get('Assigned To') or {}
        
        owner_name = 'Unassigned'
        if owner_prop.get('people'):
            people = owner_prop['people']
            if people:
                owner_name = people[0].get('name', 'Unknown')
        elif owner_prop.get('select'):
            owner_name = owner_prop['select'].get('name', 'Unknown')
        elif owner_prop.get('rich_text'):
            owner_name = ''.join([t.get('plain_text', '') for t in owner_prop['rich_text']])
        
        owners[owner_name].append(project)
    
    return owners

def generate_owner_report(owner_name, projects):
    """Generate action notes for a single owner."""
    issues_summary = {
        'no_status_update': [],
        'needs_followup_payment': [],
        'needs_meeting': [],
        'needs_closing': [],
        'missing_data': []
    }
    
    for project in projects:
        # Skip won/lost/completed projects
        props = project.get('properties', {})
        status_prop = props.get('Status') or props.get('status') or {}
        status = ''
        if status_prop.get('select'):
            status = status_prop['select'].get('name', '').lower()
        elif status_prop.get('status'):
            status = status_prop['status'].get('name', '').lower()
        
        if status in ['won', 'lost', 'completed', 'closed']:
            continue
        
        issues = analyze_project(project, owner_name)
        project_info = f"**{issues['project_name'] or 'Unnamed'}**"
        if issues['deal_value']:
            project_info += f" (₹{issues['deal_value']:,.0f})"
        
        if issues['no_status_update']:
            issues_summary['no_status_update'].append(project_info)
        if issues['needs_followup_payment']:
            issues_summary['needs_followup_payment'].append(project_info)
        if issues['needs_meeting']:
            issues_summary['needs_meeting'].append(project_info)
        if issues['needs_closing']:
            issues_summary['needs_closing'].append(project_info)
        if issues['missing_data']:
            issues_summary['missing_data'].append(f"{project_info} (missing: {', '.join(issues['missing_data'])})")
    
    # Generate report text
    report_lines = [f"## 🎯 {owner_name.upper()}\n"]
    
    has_issues = False
    
    if issues_summary['no_status_update']:
        has_issues = True
        report_lines.append(f"### 📋 Status Updates Needed")
        report_lines.append(f"{owner_name}, you haven't updated the status of the following projects:")
        for p in issues_summary['no_status_update']:
            report_lines.append(f"- {p}")
        report_lines.append("")
    
    if issues_summary['needs_followup_payment']:
        has_issues = True
        report_lines.append(f"### 💰 Payment Follow-up Required")
        report_lines.append(f"{owner_name}, you need to follow up on payment with the following customers:")
        for p in issues_summary['needs_followup_payment']:
            report_lines.append(f"- {p}")
        report_lines.append("")
    
    if issues_summary['needs_closing']:
        has_issues = True
        report_lines.append(f"### 🎯 Ready to Close")
        report_lines.append(f"{owner_name}, you need to try to close the following projects:")
        for p in issues_summary['needs_closing']:
            report_lines.append(f"- {p}")
        report_lines.append("")
    
    if issues_summary['needs_meeting']:
        has_issues = True
        report_lines.append(f"### 📅 Meetings Needed")
        report_lines.append(f"{owner_name}, you need to schedule meetings with the following customers to move the project status:")
        for p in issues_summary['needs_meeting']:
            report_lines.append(f"- {p}")
        report_lines.append("")
    
    if issues_summary['missing_data']:
        has_issues = True
        report_lines.append(f"### ⚠️ Missing Information")
        report_lines.append(f"{owner_name}, please fill in missing data for these projects:")
        for p in issues_summary['missing_data']:
            report_lines.append(f"- {p}")
        report_lines.append("")
    
    if not has_issues:
        report_lines.append("✅ All active projects are up to date! Great job!\n")
    
    # Calculate proactive score
    total_active = len([p for p in projects if analyze_project(p, owner_name)['status'] not in ['won', 'lost', 'completed', 'closed']])
    total_issues = sum(len(v) for v in issues_summary.values())
    score = max(0, 10 - (total_issues / max(total_active, 1)) * 2) if total_active > 0 else 10
    report_lines.append(f"### 📊 Proactive Score: **{score:.1f}/10**\n")
    report_lines.append("---\n")
    
    return '\n'.join(report_lines)

def generate_full_report(projects_data):
    """Generate the full report for all owners."""
    owners = group_projects_by_owner(projects_data)
    
    today = datetime.now().strftime("%B %d, %Y")
    
    report = f"""# 📅 {today} - Daily Sales Action Plan

## 📊 DAILY SALES ACTION REPORT
*Auto-generated analysis of Project Pipeline database*

---

"""
    
    # Generate report for each owner
    for owner_name in sorted(owners.keys()):
        if owner_name.lower() != 'unassigned':
            report += generate_owner_report(owner_name, owners[owner_name])
    
    # Add unassigned projects if any
    if 'Unassigned' in owners and owners['Unassigned']:
        report += generate_owner_report('Unassigned', owners['Unassigned'])
    
    # Add summary section
    total_projects = len(projects_data)
    active_count = len([p for p in projects_data 
                       if p.get('properties', {}).get('Status', {}).get('select', {}).get('name', '').lower() 
                       not in ['won', 'lost', 'completed', 'closed']])
    
    report += f"""
## 📈 TEAM SUMMARY

**Total Projects in Pipeline:** {total_projects}
**Active Projects:** {active_count}
**Sales Team Members:** {len([o for o in owners.keys() if o != 'Unassigned'])}

---

*Generated by Sales Owner Analyzer | {datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""
    
    return report

if __name__ == "__main__":
    # This script is meant to be called with project data passed as JSON
    # Usage: python analyze_sales_owners.py < projects.json
    
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("""
Sales Owner Analyzer

Usage:
    echo '{"results": [...]}' | python analyze_sales_owners.py
    
The script expects Notion database query results in JSON format via stdin.
It outputs the analysis report in Notion-flavored Markdown.
        """)
        sys.exit(0)
    
    try:
        data = json.load(sys.stdin)
        projects = data.get('results', data) if isinstance(data, dict) else data
        report = generate_full_report(projects)
        print(report)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
