# Project skills

Every Claude Code skill available to this repository, vendored so any session — local,
web, or CI — loads the same set without depending on a machine's `~/.claude/skills`.

Claude Code discovers these automatically: each subdirectory holds a `SKILL.md` whose
YAML frontmatter carries the `name` and `description` used for triggering. Invoke one
explicitly with `/<skill-name>`, or just describe the task and let the description match.

## Adding or updating a skill

Drop a new directory here containing a `SKILL.md`, or edit an existing one in place.
The directory name and the frontmatter `name` must agree.

## Naming note

`frontend-design` is the SpaceCrafter Shopify skill. Anthropic ships an unrelated skill
under the same name; it is vendored here as `frontend-design-anthropic` so both coexist.

## Catalog (62 skills)

| Skill | Source | Description |
| --- | --- | --- |
| `algorithmic-art` | personal | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields,... |
| `benepass-reimbursement` | Anthropic example | Submit expense reimbursements through Benepass (app.getbenepass.com). For users whose employer uses Benepass as their benefits platform. Handles login, benefit selection, form filling, receipt uplo... |
| `brand-artifact-generator` | personal | Transform brand identity guidelines into comprehensive physical branding strategies with AI-ready prompts, technical specifications, and client presentation materials. Use this skill when you need ... |
| `brand-artifact-prompt-generator` | personal | Generate detailed AI image prompts for spatial branding artifacts (signage, murals, wall graphics, wayfinding) by analyzing brand guidelines and site images. Use when the user needs to create promp... |
| `brand-guidelines` | Anthropic example | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatt... |
| `call-to-book` | Anthropic example | Make a phone call to book an appointment or reservation. Checks calendar first, gets explicit consent before dialing, discloses AI identity on the call, and adds the booking to calendar when done. |
| `cancel-unsubscribe` | Anthropic example | Cancel a subscription or unsubscribe from a service. Works from a description, a pasted charge line, a URL, or a photo/screenshot. Can also audit a full statement for recurring charges and cancel s... |
| `canvas-design` | personal | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create ... |
| `close-deals` | personal | Automate daily sales reports from Notion databases. Generate actionable recommendations for active projects, identify urgent items, analyze team performance, and create motivational action plans. U... |
| `design-taste-frontend` | personal | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design sys... |
| `doc-coauthoring` | Anthropic example | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This ... |
| `docx` | personal | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any mention of 'Word doc', 'word document... |
| `event-planning` | Anthropic example | Help plan an event — from a birthday dinner to a wedding. Scales to the size of the occasion. Handles venue research, guest lists, timelines, vendors, and budgets. |
| `file-expenses` | Anthropic example | Help submit an expense or reimbursement on any platform. Detects the right tool (Benepass, Brex, Concur, Expensify, etc.), finds receipts, checks for duplicates, and walks through submission. |
| `file-form` | Anthropic example | Handle small bureaucratic tasks — jury duty responses, parking tickets, passport renewals, DMV forms, permit applications, and other government or administrative paperwork. |
| `file-reading` | Anthropic bundled | Use this skill when a file has been uploaded but its content is NOT in your context — only its path at /mnt/user-data/uploads/ is listed in an uploaded_files block. This skill is a router: it tells... |
| `finance-insights` | personal | > SpaceCrafter Studio financial health checker and project expense insights generator. Use this skill when the user says "finance check", "expense report", "budget check", "run finance insights", "... |
| `financial-calculator` | Anthropic example | Run financial calculations and scenario comparisons — tax estimates, loan comparisons, retirement projections, rent vs. buy, investment scenarios, and more. Pure math, no accounts or logins needed. |
| `frontend-design` | personal | Build drop-in sections and components for the existing SpaceCrafter Studio Shopify website. Use when creating new page sections, lead-generation blocks, product explainers, or UI components for spa... |
| `frontend-design-anthropic` | Anthropic bundled | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated de... |
| `grocery-shopping` | Anthropic example | Help order groceries for delivery. Concierge-style flow — store selection, occasion-based list building, budget tracking, and cart assembly. |
| `hire-help` | Anthropic example | Help find and book a service provider for a task — cleaning, handyman, moving, assembly, yard work, errands, etc. Searches TaskRabbit, Handy, Thumbtack, and similar platforms. |
| `hygiene-scan` | personal | > Production Line Items data hygiene scanner for SpaceCrafter Studio. Use when the user says "run hygiene scan", "data hygiene", "clean production line items", "scan checkboxes", "hygiene check", "... |
| `import-memory` | Anthropic example | Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data. |
| `internal-comms` | Anthropic example | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal ... |
| `kingar-offer-letter` | personal | Generate professional offer letters for Kingar Signs Pvt Ltd (brand SpaceCrafter Studio). Use when the user says "create offer letter", "generate offer letter", "new offer letter for [name]", "offe... |
| `learn` | Anthropic example | \| Use this skill when the user wants intellectual understanding — learning how or why something works, not getting a task done or soliciting Claude's judgment. Trigger for: - Explicit learning requ... |
| `led-wall-calculator` | personal | > Calculate LED panel/wall pricing for indoor and outdoor installations. Computes total cost including panels, controllers, processors, power supplies, receiver cards, MS frame support, and generat... |
| `mcp-builder` | Anthropic example | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate exte... |
| `meal-delivery` | Anthropic example | Help order food timed to arrive at a specific time. Works backward from target arrival, suggests restaurants, builds cart, and monitors delivery. |
| `morning` | personal | Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only when the user explicitly asks to run, see, or set up their morning brief, or if they in... |
| `notion-task-outcome-analyzer` | personal | Analyze task names in a Notion "Running Task Owners" database and improve them to be outcome-focused. If a task name is not outcome-related, update it to indicate it's not an outcome. Use this skil... |
| `operator` | personal | SpaceCrafter Studio daily operations manager. Use this skill when the user says \"run operator\", \"daily briefing\", \"company tracker\", \"what's happening today\", \"operator update\", \"run dai... |
| `paint` | Anthropic example | Paint an original image in a watercolor style by writing code, not by calling an image model. Use when the user asks you to draw, paint, sketch, or make a picture of something and there is no image... |
| `pdf` | personal | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, r... |
| `pdf-reading` | Anthropic bundled | Use this skill when you need to read, inspect, or extract content from PDF files — especially when file content is NOT in your context and you need to read it from disk. Covers content inventory, t... |
| `pptx` | personal | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting... |
| `prescription-refill` | Anthropic example | Refill a prescription at a pharmacy. Works from a medication name, an Rx number, a photo of the bottle, or just "I'm running low." Confirms exactly what's being requested, gathers everything the ph... |
| `product-self-knowledge` | Anthropic bundled | Stop and consult this skill whenever your response would include specific facts about Anthropic's products. Covers: Claude Code (how to install, Node.js requirements, platform/OS support, MCP serve... |
| `production-daily-tracker` | personal | Daily production tracker that scans the Production Line Items database and updates the Production Daily Notion page with today's tasks, tomorrow's tasks, and upcoming items. Groups by project, show... |
| `return-refund` | Anthropic example | Help return an item or request a refund from any retailer. Identifies the item, finds the return policy, navigates the process, and handles shipping labels or phone calls. |
| `sales-owner-analyzer` | personal | \| Exhaustive analysis of ALL projects in Project Pipeline by status. Generates personalized daily action notes for each sales owner. Triggers: "run sales analyzer", "generate sales report", "daily ... |
| `session-start-hook` | personal | Creating and developing startup hooks for Claude Code on the web. Use when the user wants to set up a repository for Claude Code on the web, create a SessionStart hook to ensure their project can r... |
| `setup-writing-style` | Anthropic example | Learns how the user writes from their own sent messages and docs, and builds a voice profile so future drafts sound like them instead of generic AI. The profile is saved as the my-writing-style ski... |
| `shopify` | personal | Build Shopify applications, extensions, and themes using GraphQL/REST APIs, Shopify CLI, Polaris UI components, and Liquid templating. Capabilities include app development with OAuth authentication... |
| `signage-quote` | personal | > Generate professional signage quotations from design images or specs. Analyzes uploaded signage designs to identify materials, dimensions, LED types, and fabrication methods, then produces a full... |
| `signage-render-generator` | personal | > Generate photorealistic signage renders using Google AI Studio (Nano Banana / Gemini image generation). Takes structural signage specs (from structural-signage-design skill or manual input) and p... |
| `skill-creator` | personal | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a sk... |
| `slack-gif-creator` | Anthropic example | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me ... |
| `space-crafter-content-engine` | personal | > Full content engine for Space Crafter Studio — a spatial branding and experiential design studio. Use this skill for ANY of the following: scanning design trends and generating social media post ... |
| `space-crafter-studio` | personal | > AI content partner for Space Crafter Studio — a spatial branding and experiential design studio. Use this skill for ANY content creation, copywriting, or brand communication task for Space Crafte... |
| `spacecrafter-ceo-cockpit-refresh` | personal | Daily morning refresh of Akshay's CEO Cockpit — updates the Notion backup page and the in-app artifact |
| `spacecrafter-partnerships` | personal | Build Space Crafter Studio's outbound pipeline. Two engines. (1) PARTNERSHIP outreach to signage manufacturers, trade fabricators and branding agencies who send continuous work. (2) CLIENT outreach... |
| `squad-daily` | personal | SpaceCrafter Studio daily squad scorecard and focus planner. Use this skill whenever Akshay says 'run squad daily', 'squad daily', 'squad update', 'squad report', 'squad scorecard', 'squad standup'... |
| `stop-slop` | personal | Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells. |
| `structural-signage-design` | personal | > Generate structural shop designs for signage pylons and building-mounted LED panels — material selection, wind load calculations (IS 875), fabrication-ready specs, foundation details, anchor bolt... |
| `theme-factory` | personal | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifac... |
| `wall-vocab` | personal | > Brand language and voice skill for Wall Vocab — the D2C wall art brand by Space Crafter Studio (neon quote signs, 3D letters, moss letters, typographic and pop-culture wall pieces sold online in ... |
| `watch` | personal | Watch a video (URL or local path). Downloads with yt-dlp, extracts auto-scaled frames with ffmpeg, pulls the transcript from captions (or Whisper API fallback), and hands the result to Claude so it... |
| `web-artifacts-builder` | personal | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state ma... |
| `work-order` | personal | > Generate simple production work orders on Notion pages. Analyzes a signage design image, selects the right departments, creates a production flow diagram, lists total materials needed, and gives ... |
| `xlsx` | personal | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .csv, or .tsv file ... |

## Not included

Slash commands compiled into the `claude` binary itself — `code-review`, `simplify`,
`loop`, `dataviz`, `artifact-design`, `artifact-diagramming`, `artifact-capabilities`,
`claude-api`, `run`, `stop-slop`, `update-config`, `keybindings-help`,
`fewer-permission-prompts`, `init`, `security-review` — ship with the CLI and are always
available. They exist only inside the executable, so there are no files to vendor.
