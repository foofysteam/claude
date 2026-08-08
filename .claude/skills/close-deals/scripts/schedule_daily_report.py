#!/usr/bin/env python3
"""
Scheduler for running the daily sales report at 10 AM.
This can be used with cron or as a standalone scheduled task.
"""

import os
import sys
import time
import schedule
import subprocess
from datetime import datetime


def run_daily_report():
    """Execute the daily report generation."""
    print(f"\n{'='*60}")
    print(f"🕐 Starting daily sales report at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Get configuration from environment variables
    api_key = os.getenv("NOTION_API_KEY")
    database_id = os.getenv("NOTION_DATABASE_ID")
    report_page_id = os.getenv("NOTION_REPORT_PAGE_ID")
    
    if not all([api_key, database_id, report_page_id]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: NOTION_API_KEY, NOTION_DATABASE_ID, NOTION_REPORT_PAGE_ID")
        return
    
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    report_script = os.path.join(script_dir, "generate_daily_report.py")
    
    # Run the report generation script
    try:
        result = subprocess.run(
            [sys.executable, report_script, api_key, database_id, report_page_id],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        
        if result.returncode == 0:
            print(f"\n✅ Daily report completed successfully at {datetime.now().strftime('%H:%M:%S')}")
        else:
            print(f"\n❌ Daily report failed with exit code {result.returncode}")
    
    except Exception as e:
        print(f"❌ Error running daily report: {e}")
    
    print(f"{'='*60}\n")


def setup_schedule(run_time: str = "10:00"):
    """Setup the daily schedule."""
    schedule.every().day.at(run_time).do(run_daily_report)
    print(f"📅 Scheduler configured to run daily at {run_time}")
    print(f"🔄 Waiting for scheduled time...\n")
    
    # Keep the scheduler running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n⏹️  Scheduler stopped by user")


def main():
    """Main entry point."""
    run_time = os.getenv("REPORT_RUN_TIME", "10:00")
    
    # Allow command line override
    if len(sys.argv) > 1:
        run_time = sys.argv[1]
    
    print("🚀 Close Deals - Daily Sales Report Scheduler")
    print(f"📍 Scheduled time: {run_time}")
    print(f"📊 Database ID: {os.getenv('NOTION_DATABASE_ID', 'Not set')}")
    print(f"📄 Report Page ID: {os.getenv('NOTION_REPORT_PAGE_ID', 'Not set')}")
    print()
    
    # Validate time format
    try:
        datetime.strptime(run_time, "%H:%M")
    except ValueError:
        print(f"❌ Invalid time format: {run_time}")
        print("   Use HH:MM format (e.g., 10:00)")
        sys.exit(1)
    
    # Check if we should run immediately (useful for testing)
    if "--now" in sys.argv:
        print("🏃 Running report immediately for testing...\n")
        run_daily_report()
        return
    
    # Setup and run the scheduler
    setup_schedule(run_time)


if __name__ == "__main__":
    main()
