# Close Deals Skill - Quick Start

## Installation

1. **Download the skill:**
   - You should have received a `close-deals.skill` file

2. **Upload to Claude:**
   - In Claude, click on the "Skills" or "Tools" menu
   - Click "Add Skill" or "Upload Skill"
   - Select the `close-deals.skill` file
   - Click "Install"

3. **Install Python dependencies:**

```bash
pip install -r requirements.txt --break-system-packages
```

Or manually:

```bash
pip install requests schedule --break-system-packages
```

## Initial Setup

1. **Get your Notion API key:**
   - Go to https://www.notion.so/my-integrations
   - Create a new integration
   - Copy the API key (starts with `ntn_`)

2. **Share your database:**
   - Open your projects database in Notion
   - Click "..." → "Add connections" → Select your integration

3. **Run setup:**

```bash
python scripts/setup.py
```

Follow the prompts to configure your:
- Notion API key
- Database ID
- Report page ID

4. **Test the report:**

```bash
python scripts/schedule_daily_report.py --now
```

5. **Start daily scheduler:**

```bash
python scripts/schedule_daily_report.py
```

## Your Configuration

Your Notion API key: read from the `NOTION_API_KEY` environment variable — export it in
your shell or put it in a local `.env` that is never committed. Do not paste the token
into this file.

Database URLs you provided:
- Main database: https://www.notion.so/1a52dee8423c8039a133fabfd3370fd8
- Praveen's view: https://www.notion.so/2552dee8423c80adba2ec314576031eb?v=2682dee8423c809984e7000cd2f33aa5
- Saqlain's view: https://www.notion.so/2552dee8423c80adba2ec314576031eb?v=2922dee8423c8091a1de000ceb90b4e7
- Akshay's view: https://www.notion.so/2552dee8423c80adba2ec314576031eb?v=2952dee8423c8001a599000ce9250258
- Elsa's view: https://www.notion.so/2552dee8423c80adba2ec314576031eb?v=2952dee8423c8001a599000ce9250258

To extract database IDs from these URLs, use the 32-character ID before the `?v=` part.

## Using with Claude

Once installed, you can ask Claude:
- "Generate my daily sales report"
- "What deals need urgent attention?"
- "Show me payment pending projects"
- "Analyze Praveen's active deals"
- "What should the team focus on today?"

## Support

See `SKILL.md` for full documentation and `references/SETUP.md` for detailed setup instructions.
