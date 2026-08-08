#!/usr/bin/env python3
"""
Generate daily sales report from Notion databases.
This script fetches project data, analyzes status, and creates actionable recommendations.
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

# Notion API configuration
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"


class NotionSalesReporter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json"
        }
    
    def query_database(self, database_id: str, filter_obj: Optional[Dict] = None) -> List[Dict]:
        """Query a Notion database with optional filters."""
        url = f"{BASE_URL}/databases/{database_id}/query"
        payload = {}
        if filter_obj:
            payload["filter"] = filter_obj
        
        all_results = []
        has_more = True
        start_cursor = None
        
        while has_more:
            if start_cursor:
                payload["start_cursor"] = start_cursor
            
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            
            all_results.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        
        return all_results
    
    def get_page_content(self, page_id: str) -> Dict:
        """Get a Notion page by ID."""
        url = f"{BASE_URL}/pages/{page_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def update_page(self, page_id: str, properties: Dict) -> Dict:
        """Update a Notion page's properties."""
        url = f"{BASE_URL}/pages/{page_id}"
        payload = {"properties": properties}
        response = requests.patch(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def append_blocks(self, page_id: str, blocks: List[Dict]) -> Dict:
        """Append blocks to a Notion page."""
        url = f"{BASE_URL}/blocks/{page_id}/children"
        payload = {"children": blocks}
        response = requests.patch(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def get_block_children(self, block_id: str) -> List[Dict]:
        """Get children blocks of a block."""
        url = f"{BASE_URL}/blocks/{block_id}/children"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json().get("results", [])
    
    def delete_blocks(self, block_ids: List[str]):
        """Delete blocks from a page."""
        for block_id in block_ids:
            url = f"{BASE_URL}/blocks/{block_id}"
            requests.delete(url, headers=self.headers)
    
    def extract_property_value(self, prop: Dict, prop_type: str) -> Any:
        """Extract value from a Notion property based on its type."""
        if not prop:
            return None
        
        if prop_type == "title":
            return "".join([t.get("plain_text", "") for t in prop.get("title", [])])
        elif prop_type == "rich_text":
            return "".join([t.get("plain_text", "") for t in prop.get("rich_text", [])])
        elif prop_type == "select":
            select = prop.get("select")
            return select.get("name") if select else None
        elif prop_type == "multi_select":
            return [item.get("name") for item in prop.get("multi_select", [])]
        elif prop_type == "status":
            status = prop.get("status")
            return status.get("name") if status else None
        elif prop_type == "date":
            date = prop.get("date")
            return date.get("start") if date else None
        elif prop_type == "number":
            return prop.get("number")
        elif prop_type == "checkbox":
            return prop.get("checkbox", False)
        elif prop_type == "people":
            return [person.get("name", "") for person in prop.get("people", [])]
        elif prop_type == "relation":
            return [rel.get("id") for rel in prop.get("relation", [])]
        else:
            return None
    
    def parse_project(self, page: Dict) -> Dict[str, Any]:
        """Parse a project page into a structured dictionary."""
        props = page.get("properties", {})
        
        # Extract common properties (adjust based on your actual schema)
        project_data = {
            "id": page.get("id"),
            "url": page.get("url"),
            "created_time": page.get("created_time"),
            "last_edited_time": page.get("last_edited_time")
        }
        
        # Dynamically extract all properties
        for prop_name, prop_data in props.items():
            prop_type = prop_data.get("type")
            project_data[prop_name] = self.extract_property_value(prop_data, prop_type)
        
        return project_data
    
    def calculate_days_since(self, date_str: Optional[str]) -> Optional[int]:
        """Calculate days since a given date."""
        if not date_str:
            return None
        try:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            return (datetime.now(date.tzinfo) - date).days
        except:
            return None
    
    def analyze_project(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a project and generate insights."""
        analysis = {
            "project": project,
            "urgency": "medium",
            "days_in_progress": None,
            "payment_overdue": False,
            "customer_ready": False,
            "recommendations": []
        }
        
        # Calculate days in progress
        created = project.get("created_time")
        if created:
            analysis["days_in_progress"] = self.calculate_days_since(created)
        
        # Check customer readiness (adjust property name as needed)
        customer_ready_props = ["customer is ready", "Customer Ready", "Ready", "customer_ready"]
        for prop in customer_ready_props:
            if prop in project and project[prop]:
                analysis["customer_ready"] = True
                analysis["urgency"] = "high"
                break
        
        # Check payment pending
        status = project.get("Status", "").lower() if project.get("Status") else ""
        if "payment" in status and "pending" in status:
            analysis["payment_overdue"] = True
            analysis["urgency"] = "high"
        
        # Generate recommendations based on status
        self._generate_recommendations(analysis)
        
        return analysis
    
    def _generate_recommendations(self, analysis: Dict[str, Any]):
        """Generate actionable recommendations for a project."""
        project = analysis["project"]
        status = project.get("Status", "")
        recommendations = []
        
        # Status-specific recommendations
        if status == "Targeted":
            recommendations.append("🎯 Initiate first contact with prospect")
            recommendations.append("📋 Prepare value proposition and pitch deck")
            recommendations.append("🔍 Research client's business needs and pain points")
        
        elif status == "Lead":
            recommendations.append("📞 Schedule discovery call within 24 hours")
            recommendations.append("💼 Qualify lead based on budget, authority, need, timeline")
            recommendations.append("📧 Send introduction email with case studies")
        
        elif "Discussion" in status or "In Discussion" in status:
            recommendations.append("📊 Present detailed proposal with pricing options")
            recommendations.append("🤝 Address objections and concerns raised")
            recommendations.append("⏰ Set clear next steps and decision timeline")
        
        elif "Design" in status:
            recommendations.append("🎨 Share design mockups for client feedback")
            recommendations.append("✅ Get design approval in writing")
            recommendations.append("📅 Confirm production timeline and milestones")
        
        elif status == "Production":
            recommendations.append("📸 Share work-in-progress updates with client")
            recommendations.append("⚡ Ensure production stays on schedule")
            recommendations.append("💰 Initiate payment collection process")
        
        elif status == "On Hold":
            recommendations.append("🔔 Follow up to understand blocking issues")
            recommendations.append("🤔 Propose solutions to resume project")
            recommendations.append("📆 Set reminder to check in within 3 days")
        
        elif status == "Fixing" or status == "Repair":
            recommendations.append("🔧 Document issues and resolution timeline")
            recommendations.append("👤 Keep client updated on progress daily")
            recommendations.append("✨ Plan quality check before final delivery")
        
        elif "PAYMENT PENDING" in status or "Payment Pending" in status:
            recommendations.append("💸 URGENT: Follow up on payment immediately")
            recommendations.append("📄 Send payment reminder with invoice")
            recommendations.append("📞 Call client if payment is overdue >7 days")
        
        # Urgency-based recommendations
        if analysis["customer_ready"]:
            recommendations.insert(0, "🚨 PRIORITY: Customer is ready - act fast!")
        
        if analysis["days_in_progress"] and analysis["days_in_progress"] > 30:
            recommendations.append("⚠️ Project has been open for 30+ days - reassess timeline")
        
        # Add motivational close
        if status not in ["Won", "Lost"]:
            recommendations.append(self._get_motivational_statement(status, analysis))
        
        analysis["recommendations"] = recommendations
    
    def _get_motivational_statement(self, status: str, analysis: Dict) -> str:
        """Generate a motivational statement to drive action."""
        statements = {
            "Targeted": "💪 Every closed deal starts with a first step - reach out today!",
            "Lead": "🎯 Strike while the iron is hot - convert this lead into a meeting!",
            "In Discussion": "🚀 You're close! One great conversation can seal this deal!",
            "Design": "⭐ Design approval means they're committed - keep momentum high!",
            "Production": "🏆 The finish line is in sight - deliver excellence!",
            "On Hold": "🔥 Don't let this opportunity go cold - take action now!",
            "Fixing": "💎 Great service recovery builds loyalty - make it right!",
            "PAYMENT PENDING": "💰 Money in the bank = mission accomplished - collect today!"
        }
        
        if analysis["customer_ready"]:
            return "⚡ Customer is ready to move forward - this is YOUR moment to close!"
        
        return statements.get(status, "🎯 Every action brings you closer to closing - make your move!")
    
    def generate_report(self, database_id: str, report_page_id: str):
        """Generate the daily sales report."""
        print("🔍 Fetching projects from Notion...")
        
        # Fetch all projects NOT in Won or Lost status
        filter_obj = {
            "and": [
                {
                    "property": "Status",
                    "status": {
                        "does_not_equal": "Won"
                    }
                },
                {
                    "property": "Status",
                    "status": {
                        "does_not_equal": "Lost"
                    }
                }
            ]
        }
        
        projects = self.query_database(database_id, filter_obj)
        print(f"📊 Found {len(projects)} active projects")
        
        # Parse and analyze projects
        analyzed_projects = []
        for project_page in projects:
            project = self.parse_project(project_page)
            analysis = self.analyze_project(project)
            analyzed_projects.append(analysis)
        
        # Sort by urgency (high first) and status
        urgency_order = {"high": 0, "medium": 1, "low": 2}
        analyzed_projects.sort(key=lambda x: (urgency_order.get(x["urgency"], 1), x["project"].get("Status", "")))
        
        # Generate report content
        report_blocks = self._create_report_blocks(analyzed_projects)
        
        # Update the report page
        print(f"📝 Updating report page...")
        self._update_report_page(report_page_id, report_blocks)
        
        print("✅ Daily sales report generated successfully!")
        return analyzed_projects
    
    def _create_report_blocks(self, analyzed_projects: List[Dict]) -> List[Dict]:
        """Create Notion blocks for the report."""
        blocks = []
        
        # Header
        today = datetime.now().strftime("%A, %B %d, %Y")
        blocks.append({
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": f"📊 Daily Sales Report - {today}"}}]
            }
        })
        
        # Summary stats
        total = len(analyzed_projects)
        high_urgency = sum(1 for p in analyzed_projects if p["urgency"] == "high")
        payment_pending = sum(1 for p in analyzed_projects if p["payment_overdue"])
        customer_ready = sum(1 for p in analyzed_projects if p["customer_ready"])
        
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [{"type": "text", "text": {"content": f"📈 {total} active projects | 🔥 {high_urgency} high priority | 💰 {payment_pending} payment pending | ✅ {customer_ready} customer ready"}}],
                "icon": {"emoji": "📊"}
            }
        })
        
        blocks.append({
            "object": "block",
            "type": "divider",
            "divider": {}
        })
        
        # Project details
        for i, analysis in enumerate(analyzed_projects, 1):
            project = analysis["project"]
            
            # Project header
            project_name = project.get("Name") or project.get("Project Name") or project.get("Title") or f"Project {i}"
            status = project.get("Status", "Unknown")
            urgency_emoji = {"high": "🔥", "medium": "⚡", "low": "📋"}.get(analysis["urgency"], "📋")
            
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": f"{urgency_emoji} {project_name}"}}]
                }
            })
            
            # Project details
            details = []
            details.append(f"**Status:** {status}")
            
            if "Owner" in project or "Assigned to" in project:
                owner = project.get("Owner") or project.get("Assigned to")
                if isinstance(owner, list):
                    owner = ", ".join(owner)
                details.append(f"**Owner:** {owner}")
            
            if analysis["days_in_progress"]:
                details.append(f"**Days Open:** {analysis['days_in_progress']}")
            
            if "Amount" in project or "Value" in project or "Project Value" in project:
                amount = project.get("Amount") or project.get("Value") or project.get("Project Value")
                if amount:
                    details.append(f"**Value:** ₹{amount:,.2f}" if isinstance(amount, (int, float)) else f"**Value:** {amount}")
            
            if analysis["customer_ready"]:
                details.append("✅ **Customer is Ready**")
            
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": " | ".join(details)}}]
                }
            })
            
            # Link to project
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {"type": "text", "text": {"content": "🔗 ", "link": None}},
                        {"type": "text", "text": {"content": "View Project", "link": {"url": project["url"]}}}
                    ]
                }
            })
            
            # Recommendations
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": "Action Items:"}}]
                }
            })
            
            for rec in analysis["recommendations"][:8]:  # Limit to 7-8 lines as requested
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": [{"type": "text", "text": {"content": rec}}]
                    }
                })
            
            # Divider between projects
            blocks.append({
                "object": "block",
                "type": "divider",
                "divider": {}
            })
        
        # Footer
        blocks.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [{"type": "text", "text": {"content": "🎯 Focus on high priority items first. Every conversation matters. Let's close more deals today!"}}],
                "icon": {"emoji": "💪"}
            }
        })
        
        return blocks
    
    def _update_report_page(self, page_id: str, new_blocks: List[Dict]):
        """Update the report page by replacing old content with new content."""
        # Get existing blocks
        existing_blocks = self.get_block_children(page_id)
        
        # Delete existing blocks (except first one if it's a title)
        block_ids_to_delete = [block["id"] for block in existing_blocks if block["type"] != "child_page"]
        if block_ids_to_delete:
            print(f"🗑️ Clearing {len(block_ids_to_delete)} old blocks...")
            self.delete_blocks(block_ids_to_delete)
        
        # Append new blocks in batches (Notion API limit is 100 blocks per request)
        print(f"➕ Adding {len(new_blocks)} new blocks...")
        batch_size = 100
        for i in range(0, len(new_blocks), batch_size):
            batch = new_blocks[i:i+batch_size]
            self.append_blocks(page_id, batch)


def main():
    """Main entry point for the script."""
    # Get configuration from environment or arguments
    api_key = os.getenv("NOTION_API_KEY")
    database_id = os.getenv("NOTION_DATABASE_ID")
    report_page_id = os.getenv("NOTION_REPORT_PAGE_ID")
    
    # Allow command line arguments to override
    if len(sys.argv) >= 4:
        api_key = sys.argv[1]
        database_id = sys.argv[2]
        report_page_id = sys.argv[3]
    
    if not all([api_key, database_id, report_page_id]):
        print("❌ Error: Missing required configuration")
        print("\nUsage:")
        print("  python generate_daily_report.py <api_key> <database_id> <report_page_id>")
        print("\nOr set environment variables:")
        print("  NOTION_API_KEY")
        print("  NOTION_DATABASE_ID")
        print("  NOTION_REPORT_PAGE_ID")
        sys.exit(1)
    
    try:
        reporter = NotionSalesReporter(api_key)
        reporter.generate_report(database_id, report_page_id)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
