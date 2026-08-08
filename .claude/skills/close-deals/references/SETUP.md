# Close Deals - Setup and Configuration Guide

## Overview

This skill automates daily sales reports from your Notion databases, providing actionable recommendations for each active project. It analyzes project status, identifies urgent items, and generates motivational action items to help your sales team close more deals.

## Prerequisites

- Python 3.7 or higher
- Notion account with API access
- pip (Python package manager)

## Installation

1. **Install required Python packages:**

```bash
pip install requests schedule --break-system-packages
```

2. **Get your Notion API key:**

   - Go to https://www.notion.so/my-integrations
   - Click "+ New integration"
   - Give it a name (e.g., "Close Deals Bot")
   - Select your workspace
   - Click "Submit"
   - Copy the "Internal Integration Token" (starts with `ntn_`)

3. **Share your databases with the integration:**

   - Open your projects database in Notion
   - Click "..." (three dots) in the top right
   - Click "Add connections"
   - Select your integration
   - Click "Confirm"
   - Repeat for any related databases

4. **Get your Database IDs:**

   - Open your database in Notion
   - Look at the URL: `https://notion.so/workspace/DATABASE_ID?v=VIEW_ID`
   - Copy the DATABASE_ID (32 characters, no hyphens)

5. **Create or identify your report page:**

   - Create a new blank page in Notion where reports will be updated daily
   - Copy the page ID from the URL
   - OR: Let the setup script create one for you

## Configuration

### Option 1: Interactive Setup (Recommended)

Run the setup wizard:

```bash
python scripts/setup.py
```

This will:
- Test your Notion API connection
- List your available databases
- Help you create a report page
- Save configuration to `.env` file

### Option 2: Manual Configuration

Create a `.env` file with:

```bash
NOTION_API_KEY=ntn_your_api_key_here
NOTION_DATABASE_ID=your_database_id_here
NOTION_REPORT_PAGE_ID=your_report_page_id_here
REPORT_RUN_TIME=10:00
```

Then load the environment variables:

```bash
# Linux/Mac
export $(cat .env | xargs)

# Windows (PowerShell)
Get-Content .env | ForEach-Object {
    $name, $value = $_.split('=')
    Set-Item -Path "env:$name" -Value $value
}
```

## Database Schema Requirements

Your Notion projects database should have these properties (exact names may vary):

### Required Properties:
- **Status** (Status or Select): Current project status
  - Targeted
  - Lead
  - In Discussion (sales+ Design)
  - Design - production design
  - Production
  - On Hold
  - Fixing
  - Repair
  - PAYMENT PENDING
  - Won (excluded from reports)
  - Lost (excluded from reports)

### Recommended Properties:
- **Name/Title** (Title): Project name
- **Owner/Assigned to** (Person): Salesperson responsible
- **Amount/Value/Project Value** (Number): Deal value
- **Customer Ready/Customer is Ready** (Checkbox): Customer readiness indicator
- **Created Date** (Created time): Auto-generated
- **Last Edited** (Last edited time): Auto-generated

The script will automatically detect and use whatever property names you have for these common fields.

## Usage

### Running the Report Manually

Test the report generation:

```bash
python scripts/schedule_daily_report.py --now
```

### Running on a Schedule

#### Option 1: Python Scheduler (Recommended for always-on systems)

Start the scheduler to run daily at 10 AM:

```bash
python scripts/schedule_daily_report.py
```

Keep this process running (e.g., in a terminal, tmux session, or as a system service).

To run at a different time:

```bash
python scripts/schedule_daily_report.py 09:30
```

#### Option 2: Cron (Linux/Mac)

Add to your crontab:

```bash
crontab -e
```

Add this line (adjust paths):

```bash
0 10 * * * cd /path/to/skill && /usr/bin/python3 scripts/generate_daily_report.py "$NOTION_API_KEY" "$NOTION_DATABASE_ID" "$NOTION_REPORT_PAGE_ID"
```

#### Option 3: Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Set trigger: Daily at 10:00 AM
4. Set action: Run `python` with arguments pointing to `generate_daily_report.py`
5. Set environment variables in the action settings

## Report Structure

The daily report includes:

1. **Header** - Date and summary statistics
   - Total active projects
   - High priority count
   - Payment pending count
   - Customer ready count

2. **Project Sections** (for each active project):
   - Project name with urgency indicator (🔥 high, ⚡ medium, 📋 low)
   - Status, owner, days open, project value
   - Link to the Notion project page
   - 7-8 actionable recommendations specific to the project status
   - Motivational closing statement

3. **Footer** - Motivational message to drive action

## Customization

### Adjusting Urgency Rules

Edit `scripts/generate_daily_report.py`, find the `analyze_project` method:

```python
def analyze_project(self, project: Dict[str, Any]) -> Dict[str, Any]:
    # Modify urgency logic here
    if project.get("customer is ready"):
        analysis["urgency"] = "high"
    
    # Add custom rules
    if project.get("Days Open") > 60:
        analysis["urgency"] = "high"
```

### Customizing Recommendations

Edit the `_generate_recommendations` method to add or modify status-specific recommendations:

```python
elif status == "Your Custom Status":
    recommendations.append("📌 Your custom action item")
```

### Changing Report Format

Edit the `_create_report_blocks` method to modify how the report looks in Notion.

## Troubleshooting

### "Missing required configuration"
- Ensure all environment variables are set
- Check that .env file is loaded
- Verify API key format (starts with `ntn_`)

### "Unauthorized" or "Object not found"
- Share the database with your integration in Notion
- Verify database ID is correct (32 characters)
- Check that API key is valid

### "No projects found"
- Verify database has projects with status other than "Won" or "Lost"
- Check Status property name matches your database
- Try running without filters first

### Report not updating
- Check that report page ID is correct
- Verify the integration has write access to the page
- Look for error messages in the script output

## Integration with Claude

When using this skill with Claude:

1. **Trigger phrases:**
   - "Generate my daily sales report"
   - "Update the close deals report"
   - "Show me today's sales priorities"

2. **Claude will:**
   - Read the skill documentation
   - Execute the report generation script
   - Analyze the results
   - Provide insights and suggestions

3. **Ask Claude to:**
   - "Analyze which deals need urgent attention"
   - "Summarize payment pending projects"
   - "Show me Praveen's active projects"
   - "What should I focus on today?"

## Best Practices

1. **Daily Review:** Review the report every morning at 10 AM
2. **Follow Up:** Act on high-priority items immediately
3. **Update Notion:** Keep project status and notes current
4. **Team Communication:** Share relevant sections with team members
5. **Track Progress:** Monitor trends week-over-week

## Support

For issues or questions:
- Check the troubleshooting section above
- Review Notion API documentation: https://developers.notion.com
- Verify your database structure matches requirements
