---
name: notion-task-outcome-analyzer
description: Analyze task names in a Notion "Running Task Owners" database and improve them to be outcome-focused. If a task name is not outcome-related, update it to indicate it's not an outcome. Use this skill when the user wants to review or improve task naming in their Notion task database.
---

# Notion Task Outcome Analyzer

This skill analyzes task names in a Notion task database and improves them to be outcome-focused.

## When to Use This Skill

Use this skill when:
- The user wants to analyze their Notion task database for outcome-focused naming
- The user wants to identify and flag tasks that are not outcome-oriented
- The user wants to automatically update non-outcome tasks with a clear indicator

## What Makes a Task Name "Outcome-Related"

An outcome-related task name describes a **specific, measurable result or deliverable**, not an activity or process.

### ✅ Outcome-Related Examples:
- "Bring home 2 lakhs from MVJ" - specific amount, clear result
- "Complete Q4 financial report" - specific deliverable
- "Increase user signups by 20%" - measurable result
- "Secure signed contract with ABC Corp" - specific result
- "Launch new product feature by Oct 30" - deliverable with deadline

### ❌ NOT Outcome-Related Examples:
- "Daily Tasks" - vague, no specific outcome
- "UPDATE PAYMENT" - activity, not result
- "Meet with @" - activity, no outcome specified
- "RSP" - abbreviation without clear outcome
- "Porche" - project name, no specific outcome
- "Follow up with client" - activity without result
- "Review documents" - activity without deliverable

## Workflow

### Step 1: Fetch the Database

Fetch the user's Notion database to understand the schema:

```
Use notion-fetch tool with the database URL
```

### Step 2: Search for All Tasks

Search the database to get a sample of tasks:

```
Use notion-search tool with data_source_url from the database
Try multiple searches with different keywords to get a good sample
```

### Step 3: Analyze Each Task Name

For each task, evaluate if the name is outcome-related by checking:

1. **Specificity**: Does it describe a specific result?
2. **Measurability**: Can you tell when it's complete?
3. **Deliverable**: Does it state what will be delivered/achieved?
4. **Clarity**: Is it clear what success looks like?

If the task name fails these criteria, it's NOT outcome-related.

### Step 4: Update Non-Outcome Tasks

For tasks that are NOT outcome-related, update the task name using the pattern:

```
⚠️ NOT OUTCOME: [original task name]
```

Use the `notion-update-page` tool with:
- `command`: "update_properties"
- `properties`: {"Name": "⚠️ NOT OUTCOME: [original name]"}

### Step 5: Provide Summary

After analysis, provide a summary showing:
- Total tasks analyzed
- Number of outcome-focused tasks (left unchanged)
- Number of non-outcome tasks (updated with prefix)
- Examples of each category

## Important Notes

- Only update task names that are clearly NOT outcome-related
- Do not update tasks that already have the "⚠️ NOT OUTCOME:" prefix
- If a task name is ambiguous, fetch the full task page to check the description for context
- Batch updates in groups to avoid overwhelming the user
- Always ask for confirmation before making bulk updates if there are more than 10 tasks to update

## Decision Tree for Task Classification

```
Is the task name specific and measurable?
├─ YES: Is there a clear deliverable or result?
│  ├─ YES: ✅ Outcome-related (leave unchanged)
│  └─ NO: Check task description for context
│     ├─ Description clarifies outcome: ✅ Outcome-related
│     └─ No clear outcome in description: ❌ Update with prefix
└─ NO: Is it an activity, meeting, or vague description?
   └─ YES: ❌ Update with prefix
```

## Example Interaction

**User**: "Analyze my running task owners database and improve task names"

**Claude**:
1. Fetches the database schema
2. Searches for tasks across the database
3. Analyzes each task name for outcome focus
4. Identifies non-outcome tasks:
   - "Daily Tasks" → "⚠️ NOT OUTCOME: Daily Tasks"
   - "UPDATE PAYMENT" → "⚠️ NOT OUTCOME: UPDATE PAYMENT"
   - "Meet with @" → "⚠️ NOT OUTCOME: Meet with @"
5. Shows summary and asks for confirmation
6. Updates the tasks in Notion
7. Provides final report with links to updated tasks
