---
name: local-server
description: Serves a local directory or file on port 8000 using Python's built-in HTTP server. Use this whenever you need to preview HTML files in the browser, especially for presentations, web apps, or any file that requires HTTP context (Google Fonts, JS modules, etc.). Kills any existing process on port 8000 before starting.
---

# Local Server Skill

This skill starts a Python HTTP server on port 8000 so HTML files can be previewed in the browser at `http://localhost:8000`.

## Instructions

### 1. Kill any existing process on port 8000
```bash
fuser -k 8000/tcp 2>/dev/null || true
```

### 2. Start the server in the background from the target directory
```bash
nohup python3 -m http.server 8000 --directory "[TARGET_DIR]" > /tmp/http_server.log 2>&1 &
echo "Server PID: $!"
```

### 3. Wait briefly and verify
```bash
sleep 1 && curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/
```

### 4. Provide the URL to the user
- **Base URL**: `http://localhost:8000/`
- **For specific files**: `http://localhost:8000/[filename].html`

---

## ⚠️ Notes
- **Target Directory**: Always `--directory` to the folder *containing* the HTML file.
- **Port conflicts**: Always kill port 8000 first — there may be a previous server running.
- **Log file**: Server output goes to `/tmp/http_server.log` — check this if the server doesn't start.
- **Stopping the server**: `fuser -k 8000/tcp`
