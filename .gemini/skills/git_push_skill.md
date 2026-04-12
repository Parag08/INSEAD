# Git Sync Skill

This skill automates the process of staging, committing, and pushing changes to the repository using a specific SSH key.

## Instructions

When executing this skill, the AI must follow these sequential steps:

### 1. Stage All Changes
Execute the following command to stage all modifications:
```bash
git add .
```

### 2. Create a Descriptive Commit
1. Review staged changes using `git status` and `git diff --cached`.
2. Generate a concise, meaningful commit message based on the changes.
3. Execute the commit:
```bash
git commit -m "[Commit Message]"
```

### 3. Secure Push to Remote
Push the committed changes to GitHub using the dedicated SSH key:
```bash
GIT_SSH_COMMAND="ssh -i /home/parag/.ssh/id_ed25519_parag08 -o StrictHostKeyChecking=accept-new" git push
```

---

## ⚠️ Important Notes
- **SSH Key**: Always use `/home/parag/.ssh/id_ed25519_parag08`.
- **Identity**: Ensure `git config user.name` and `git config user.email` are set if the commit fails.
- **Conflicts**: If the push is rejected due to remote changes, stop and ask the user for instructions on how to reconcile (rebase or merge).
