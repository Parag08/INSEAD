---
name: interview-prep
description: A workflow and prompt framework for helping the user prepare for interviews by identifying core questions, analyzing correspondence/company data, and drafting tailored STAR stories from the master datastore.
---

# Interview Preparation Skill

This skill helps the user generate tailored interview preparation materials (key questions, customized STAR stories, and strategic narratives) using the Master Datastore.

## Context Locations
The tools relies on these locations:
- **Master Datastore**: `/home/parag/INSEAD/Interview/MasterDatastore/`
- **Story Index**: `/home/parag/INSEAD/Interview/MasterDatastore/stories_index.md`
- **Story Template**: `/home/parag/INSEAD/Interview/MasterDatastore/templates/star_story_template.md`

## Instructions

When the user asks you to help them prep for an interview using a specific company context, follow this exact workflow:

### Step 1: Ingest Context
1. Read the company research markdown file (if provided by the user).
2. Read the interview correspondence / dumped questions file (e.g., `company_correspondence_dump.md`).
3. Summarize the **Core Competencies** and **Vibe Check** (the specific language the company uses, e.g., "unit economics", "impact investing") the company prioritizes.

### Step 2: Formulate Core Questions
1. Based on their actual correspondence and the role context, help the user ideate the *exact* questions they are likely to face.
2. Only write questions if the user hasn't already provided a complete list. If they have, jump to mapping.

### Step 3: Match & Draft Stories
1. Consult the Master Datastore index. Suggest which stories best map to the identified questions.
2. If a story doesn't exist yet, propose a new story prompt for the user (e.g., "We need a story about X, what's a time you did this?").
3. Once you have the raw story (either from the datastore or newly provided by the user), **Tailor the Draft**.
   - Strip out irrelevant details.
   - Insert the company's specific vocabulary where natural.
   - Ensure it strictly follows the STAR framework (Situation, Task, Action, Result) defined in the template.
4. Save the finalized tailored prep in the interview folder as `[CompanyName]_Prep_Final.md`.
