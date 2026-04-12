---
name: git-sync
description: Automates staging, committing, and pushing code to GitHub using a specific SSH key (id_ed25519_parag08). Use this whenever you need to sync changes to the remote repository.
---

# Git Sync Skill

This skill provides a standardized workflow for maintaining repository synchronization with the remote origin.

## Instructions

When executing this skill, the agent must follow these sequential steps meticulously:

### 1. Stage Changes
Stage all modifications, deletions, and new files to the git index:
```bash
git add .
```

### 2. Create a Context-Aware Commit
1. Examine the staged changes using `git status` and `git diff --cached`.
2. Craft a concise and descriptive commit message following conventional commit standards.
3. Commit the changes:
```bash
git commit -m "[Commit Message]"
```

### 3. Push to Remote Securely
Push the branch to the remote origin using the dedicated SSH key:
```bash
GIT_SSH_COMMAND="ssh -i /home/parag/.ssh/id_ed25519_parag08 -o StrictHostKeyChecking=accept-new" git push
```

---

## ⚠️ Configuration Details
- **SSH Key Location**: `/home/parag/.ssh/id_ed25519_parag08`
- **Target Remote**: `origin`
- **Strict Host Key Checking**: Enabled with `accept-new` to ensure seamless first-time connections to GitHub.
