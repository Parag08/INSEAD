---
name: pdf-reader
description: Extracts text from PDF files using the pypdf library. Use this when the user needs to read, summarize, or search content within PDFs.
---

# PDF Reader Skill

This skill enables the agent to read and process the contents of PDF documents using the `pypdf` library installed in the workspace's virtual environment.

## Instructions

When the user asks to read, analyze, or search a PDF file, follow these steps:

### 1. Extract Full Text
Execute the helper script using the local `.venv` Python interpreter to extract the content:
```bash
/home/parag/INSEAD/.venv/bin/python3 /home/parag/INSEAD/.agents/skills/pdf-reader/scripts/read_pdf.py "[PDF_FILE_PATH]"
```

### 2. Search for Specific Information
To find specific terms, extract the text first and then use `grep` or your internal reasoning on the output.

---

## ⚠️ Internal Setup
- **Venv Path**: `/home/parag/INSEAD/.venv`
- **Script Path**: `/home/parag/INSEAD/.agents/skills/pdf-reader/scripts/read_pdf.py`
- **Identity**: This skill relies on the `pypdf` package being present in the `.venv`.
