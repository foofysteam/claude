#!/usr/bin/env python3
"""
Setup script for Close Deals skill.
Helps configure Notion API credentials and create the report page.
"""

import os
import sys
import json
import requests
from datetime import datetime


NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"


def test_notion_connection(api_key: str) -> bool:
    """Test if the Notion API key is valid."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION
    }
    
    try:
        response = requests.get(f"{BASE_URL}/users/me", headers=headers)
        response.raise_for_status()
        user = response.json()
        print(f"✅ Connected to Notion as: {user.get('name', 'Unknown')}")
        return True
    except Exception as e:
        print(f"❌ Failed to connect to Notion: {e}")
        return False


def list_databases(api_key: str):
    """List available databases."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/search", headers=headers, json={
            "filter": {"property": "object", "value": "database"}
        })
        response.raise_for_status()
        databases = response.json().get("results", [])
        
        print(f"\n📊 Found {len(databases)} databases:")
        for i, db in enumerate(databases[:10], 1):  # Show first 10
            title = "".join([t.get("plain_text", "") for t in db.get("title", [])])
            print(f"  {i}. {title}")
            print(f"     ID: {db['id']}")
        
        return databases
    except Exception as e:
        print(f"❌ Failed to list databases: {e}")
        return []


def create_report_page(api_key: str, parent_id: str) -> str:
    """Create a new page for the daily sales report."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    
    payload = {
        "parent": {"page_id": parent_id},
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": f"📊 Daily Sales Report - {datetime.now().strftime('%Y-%m-%d')}"
                        }
                    }
                ]
            }
        }
    }
    
    try:
        response = requests.post(f"{BASE_URL}/pages", headers=headers, json=payload)
        response.raise_for_status()
        page = response.json()
        page_id = page["id"]
        print(f"✅ Created report page with ID: {page_id}")
        return page_id
    except Exception as e:
        print(f"❌ Failed to create report page: {e}")
        return None


def save_config(api_key: str, database_id: str, report_page_id: str):
    """Save configuration to a .env file."""
    env_content = f"""# Notion API Configuration for Close Deals Skill
NOTION_API_KEY={api_key}
NOTION_DATABASE_ID={database_id}
NOTION_REPORT_PAGE_ID={report_page_id}
REPORT_RUN_TIME=10:00

# Export these variables:
# On Linux/Mac: source .env
# On Windows: Load these into your environment variables
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("\n✅ Configuration saved to .env file")
    print("📝 To use the configuration:")
    print("   Linux/Mac: export $(cat .env | xargs)")
    print("   Windows: Set these as environment variables\n")


def main():
    """Interactive setup process."""
    print("🚀 Close Deals Skill - Setup Wizard")
    print("=" * 60)
    print()
    
    # Get Notion API key
    api_key = input("Enter your Notion API key: ").strip()
    if not api_key:
        print("❌ API key is required")
        sys.exit(1)
    
    # Test connection
    print("\n🔍 Testing Notion connection...")
    if not test_notion_connection(api_key):
        sys.exit(1)
    
    # List databases
    print("\n📊 Fetching your databases...")
    databases = list_databases(api_key)
    
    # Get database ID
    print("\n📝 Enter the ID of your projects database")
    database_id = input("Database ID: ").strip()
    if not database_id:
        print("❌ Database ID is required")
        sys.exit(1)
    
    # Get or create report page
    print("\n📄 Do you have an existing page for the daily report?")
    has_page = input("Enter page ID (or press Enter to create new): ").strip()
    
    if has_page:
        report_page_id = has_page
    else:
        print("\n🆕 To create a new report page, I need a parent page ID")
        print("   (This is the page where the report will be created)")
        parent_id = input("Parent page ID: ").strip()
        if not parent_id:
            print("❌ Parent page ID is required to create a new page")
            sys.exit(1)
        
        report_page_id = create_report_page(api_key, parent_id)
        if not report_page_id:
            sys.exit(1)
    
    # Save configuration
    save_config(api_key, database_id, report_page_id)
    
    print("\n" + "=" * 60)
    print("✅ Setup complete!")
    print("\n🚀 Next steps:")
    print("   1. Run a test: python scripts/schedule_daily_report.py --now")
    print("   2. Start scheduler: python scripts/schedule_daily_report.py")
    print("   3. Or set up a cron job to run at 10 AM daily")
    print("=" * 60)


if __name__ == "__main__":
    main()
