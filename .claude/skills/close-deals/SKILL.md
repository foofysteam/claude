---
name: close-deals
description: Automate daily sales reports from Notion databases. Generate actionable recommendations for active projects, identify urgent items, analyze team performance, and create motivational action plans. Use when the user needs to track sales pipeline, generate sales reports, monitor project status, analyze deal progress, or get daily sales priorities.
---

# Close Deals

Automated daily sales reporting and deal tracking from Notion databases. Analyzes active projects, identifies urgent actions, and generates specific recommendations to help sales teams close more deals.

## When to Use This Skill

Use this skill when the user needs to:
- Generate daily sales reports from Notion
- Track active deals and project status
- Identify urgent follow-ups and payment collections
- Analyze sales team performance
- Get actionable recommendations for closing deals
- Monitor projects by status, owner, or priority
- Create motivational action plans for sales reps

## Quick Start

### First Time Setup

1. **Run the setup wizard:**

```bash
python scripts/setup.py
```

This interactive setup will:
- Test your Notion API connection
- Help you identify your database IDs
- Create or select a report page
- Save configuration to `.env` file

2. **Test the report generation:**

```bash
python scripts/schedule_daily_report.py --now
```

3. **Start the daily scheduler:**

```bash
python scripts/schedule_daily_report.py
```

For detailed setup instructions, see [SETUP.md](references/SETUP.md).

## Core Functionality

### Automatic Report Generation

The skill generates a comprehensive daily report that includes:

1. **Summary Dashboard**
   - Total active projects (excludes Won/Lost)
   - High priority count (customer ready, payment pending)
   - Key metrics at a glance

2. **Per-Project Analysis**
   - Current status and owner
   - Days in progress
   - Project value
   - Urgency indicators (🔥 high, ⚡ medium, 📋 low)
   - 7-8 specific action items tailored to project status
   - Motivational closing statement

3. **Smart Prioritization**
   - Projects with "customer ready" flag → highest priority
   - Payment pending → high urgency
   - Projects on hold for 30+ days → flagged for review
   - Sorted by urgency and status

### Status-Based Recommendations

The skill provides context-aware recommendations based on project status:

- **Targeted**: First contact strategies, value proposition prep, research
- **Lead**: Discovery call scheduling, qualification, introduction emails
- **In Discussion**: Proposal presentation, objection handling, timeline setting
- **Design**: Mockup sharing, approval gathering, timeline confirmation
- **Production**: Progress updates, schedule management, payment initiation
- **On Hold**: Issue identification, solution proposals, follow-up reminders
- **Fixing/Repair**: Issue documentation, client updates, quality checks
- **Payment Pending**: URGENT payment follow-up, invoice sending, escalation

Each recommendation includes:
- Specific action to take
- Relevant emoji for quick scanning
- Motivational language to drive action

## Configuration

### Required Environment Variables

```bash
NOTION_API_KEY=ntn_your_api_key_here
NOTION_DATABASE_ID=your_database_id_here
NOTION_REPORT_PAGE_ID=your_report_page_id_here
REPORT_RUN_TIME=10:00
```

### Database Requirements

Your Notion database should have:

**Required:**
- Status property (Status or Select type) with values like:
  - Targeted, Lead, In Discussion, Design, Production
  - On Hold, Fixing, Repair, PAYMENT PENDING
  - Won, Lost (these are excluded from reports)

**Recommended:**
- Project name/title (Title property)
- Owner/Assigned to (Person property)
- Amount/Value (Number property)
- Customer Ready checkbox
- Created and Last Edited timestamps

The script auto-detects property names, so exact naming is flexible.

## Usage Patterns

### Manual Report Generation

Generate a report on-demand:

```bash
python scripts/generate_daily_report.py <api_key> <database_id> <report_page_id>
```

Or with environment variables set:

```bash
python scripts/generate_daily_report.py
```

### Scheduled Daily Reports

**Option 1: Python Scheduler (Recommended)**

```bash
# Run daily at 10 AM (default)
python scripts/schedule_daily_report.py

# Run at custom time
python scripts/schedule_daily_report.py 09:30

# Test run immediately
python scripts/schedule_daily_report.py --now
```

**Option 2: Cron (Linux/Mac)**

```bash
# Edit crontab
crontab -e

# Add line (replace paths):
0 10 * * * cd /path/to/skill && python3 scripts/generate_daily_report.py "$NOTION_API_KEY" "$NOTION_DATABASE_ID" "$NOTION_REPORT_PAGE_ID"
```

**Option 3: Task Scheduler (Windows)**

Set up a scheduled task to run `generate_daily_report.py` at 10 AM daily with the required environment variables.

## Integration with Claude

When this skill is active, you can ask Claude to:

### Generate Reports
- "Generate my daily sales report"
- "Update the close deals report for today"
- "Show me today's sales priorities"

### Analyze Data
- "Which deals need urgent attention?"
- "What payment pending items do we have?"
- "Show me high priority projects"
- "What should the sales team focus on today?"

### Team-Specific Queries
- "What's on Praveen's plate today?"
- "Show me Saqlain's active projects"
- "Which team member has the most high-priority items?"

### Strategic Insights
- "What's blocking our pipeline?"
- "Why are projects stuck in 'On Hold'?"
- "What's the total value of payment pending projects?"
- "How can we accelerate deals in discussion?"

Claude will:
1. Execute the report generation script with your credentials
2. Analyze the results and project data
3. Provide insights, trends, and strategic recommendations
4. Answer specific questions about deals and team performance

## Customization

### Adjusting Urgency Rules

Edit `scripts/generate_daily_report.py`, modify the `analyze_project` method to add custom urgency logic:

```python
# Add custom urgency rules
if project.get("Deal Size") > 100000:
    analysis["urgency"] = "high"

if analysis["days_in_progress"] > 60:
    analysis["urgency"] = "high"
```

### Adding Custom Recommendations

Modify `_generate_recommendations` to add status-specific actions:

```python
elif status == "Your Custom Status":
    recommendations.append("📌 Your custom action")
    recommendations.append("✅ Another action item")
```

### Changing Report Format

Edit `_create_report_blocks` to customize the Notion report structure, add sections, or change formatting.

## Scripts Overview

### `generate_daily_report.py`
Main report generation script. Fetches projects from Notion, analyzes status, generates recommendations, and updates the report page.

**Usage:** Typically called by the scheduler, but can be run manually.

### `schedule_daily_report.py`
Scheduler that runs the report generation at a specified time daily (default 10 AM).

**Usage:** Keep running in background or as a system service.

### `setup.py`
Interactive setup wizard for first-time configuration.

**Usage:** Run once during initial setup, or when reconfiguring.

## Troubleshooting

### Common Issues

**"Missing required configuration"**
- Set environment variables or pass as command-line arguments
- Verify `.env` file exists and is loaded

**"Unauthorized" or "Object not found"**
- Share your database with the Notion integration
- Verify database and page IDs are correct

**"No projects found"**
- Check that Status property exists in your database
- Ensure you have projects with status other than "Won" or "Lost"

**Report not updating**
- Verify report page ID is correct
- Check integration has write permissions
- Review script output for errors

### Detailed Troubleshooting

See [SETUP.md](references/SETUP.md) for comprehensive troubleshooting steps.

## Best Practices

1. **Morning Review**: Check the report every day at 10 AM
2. **Immediate Action**: Address high-priority items (🔥) first
3. **Keep Notion Current**: Update project status and notes regularly
4. **Team Communication**: Share relevant sections with team members via copy-paste
5. **Weekly Analysis**: Track trends and patterns week-over-week
6. **Customer Ready Flag**: Always check this box when customers are ready to proceed
7. **Payment Follow-up**: Don't let payment pending items age beyond 7 days

## Report Output Example

```
📊 Daily Sales Report - Friday, October 24, 2025

📈 15 active projects | 🔥 5 high priority | 💰 3 payment pending | ✅ 2 customer ready

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 Website Redesign Project

Status: PAYMENT PENDING | Owner: Praveen | Days Open: 45 | Value: ₹2,50,000
✅ Customer is Ready
🔗 View Project

Action Items:
• 💸 URGENT: Follow up on payment immediately
• 📄 Send payment reminder with invoice
• 📞 Call client if payment is overdue >7 days
• 💰 Money in the bank = mission accomplished - collect today!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ Mobile App Development

Status: In Discussion (sales+ Design) | Owner: Saqlain | Days Open: 12 | Value: ₹5,00,000
🔗 View Project

Action Items:
• 📊 Present detailed proposal with pricing options
• 🤝 Address objections and concerns raised
• ⏰ Set clear next steps and decision timeline
• 🚀 You're close! One great conversation can seal this deal!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Focus on high priority items first. Every conversation matters. Let's close more deals today!
```

## License

See LICENSE.txt for complete terms.
