# Flask Application with Git Versioning Workflow

## Plan
1. Build a basic Flask app with mandatory health endpoints.
2. Implement Voting Application endpoints in the `dev` branch as Version 1.
3. Add one enhancement endpoint (`/reset`) in the `dev` branch as Version 2.
4. Merge only stable features from `dev` to `main`.
5. Document every step so another person can run and understand the full flow.

## Project Title and Description
This project is a simple web app made with Flask.
It starts with two basic routes to confirm that the app is running.
Then it adds a voting system where users can vote for candidates and view results.
In Version 2, a reset endpoint is added to clear all votes.

## Tech Stack
- Python 3.x
- Flask
- Git and GitHub

## Project Structure
```text
FlaskApplicationwithGitVersioningWorkflow/
|-- app.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Installation and Setup Steps
Follow these commands in order:

```powershell
# 1) Move to project folder
cd C:\HeroVired\FlaskApplicationwithGitVersioningWorkflow

# 2) (Recommended) Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run the application
python app.py
```

After running, open:
- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/health`

## API Endpoint Reference
| Endpoint | Method | What it does | Example response |
|---|---|---|---|
| `/` | GET | Shows home message | `Welcome to the App` |
| `/health` | GET | Shows app health status | `App is running` |
| `/vote/<name>` | GET | Adds 1 vote for candidate `<name>` | `{ "message": "Vote recorded for alice", "candidate": "alice", "votes": 2 }` |
| `/results` | GET | Returns all current vote counts in JSON | `{ "alice": 2, "bob": 1 }` |
| `/reset` | GET/POST | Clears all stored votes (Version 2 feature) | `{ "message": "All votes reset successfully" }` |

## Quick Functional Check
Use these sample URLs after app start:

```text
http://127.0.0.1:5000/vote/alice
http://127.0.0.1:5000/vote/alice
http://127.0.0.1:5000/vote/bob
http://127.0.0.1:5000/results
http://127.0.0.1:5000/reset
http://127.0.0.1:5000/results
```

Expected behavior:
- Votes increase when voting for an existing candidate.
- New candidate starts at 1 vote.
- `/results` returns JSON data.
- After `/reset`, `/results` returns `{}`.

## Git Workflow (dev and main)
Development should happen only in `dev`.
`main` should always remain stable and working.

Flow:
1. Start work in `dev`.
2. Commit completed feature in `dev`.
3. Push `dev`.
4. Merge `dev` into `main` only when tested.
5. Push `main` as stable release.

Simple diagram:

```text
main  ----(stable V1)----------(stable V2)---->
           ^ merge from dev      ^ merge from dev

dev   --build V1-->commit-->push--build V2-->commit-->push-->
```

## Version History
| Version | What was included |
|---|---|
| Version 1 | Flask app with `/`, `/health`, `/vote/<name>`, `/results` |
| Version 2 | Added `/reset` endpoint to clear voting data |

## Git Commands: Complete Step-by-Step to Push Code to GitHub
Replace `YOUR_USERNAME` and repository URL with your own details.

### A) Create local Git repository and first version release
```powershell
# 1) Move to project folder
cd C:\HeroVired\FlaskApplicationwithGitVersioningWorkflow

# 2) Initialize git
git init

# 3) Ensure main branch exists
git branch -M main

# 4) Create and switch to dev
git checkout -b dev

# 5) Add files and commit Version 1
# (If you want strict Version 1 first, temporarily comment /reset before this commit)
git add .
git commit -m "Version 1: add Flask app with health and voting endpoints"

# 6) Create GitHub repo manually (browser), then add remote
git remote add origin https://github.com/YOUR_USERNAME/FlaskApplicationwithGitVersioningWorkflow.git

# 7) Push dev
git push -u origin dev

# 8) Merge dev into main
git checkout main
git merge dev

# 9) Push main
git push -u origin main
```

### B) Version 2 release flow (if working exactly as assignment)
If you committed Version 1 without `/reset`, then:

```powershell
# 1) Go back to dev for new feature
git checkout dev

# 2) Add /reset endpoint in app.py
# 3) Commit Version 2
git add app.py README.md
git commit -m "Version 2: add reset endpoint for voting app"

# 4) Push dev
git push

# 5) Merge to main and push
git checkout main
git merge dev
git push
```

## Screenshots (Mandatory in README)
Embed these images directly in this README after you capture them:
1. App running in browser showing at least one working endpoint.
2. GitHub repository page showing both `dev` and `main` branches.
3. Commit/merge history showing Version 1 and Version 2 releases.

Example markdown format:

```markdown
![App Running](screenshots/app-running.png)
![Branches](screenshots/github-branches.png)
![Merge History](screenshots/git-history.png)
```

## Common Mistakes to Avoid
- Doing all work in `main` instead of `dev`.
- Using unclear commit messages like "done" or "fix".
- Returning wrong response format for JSON endpoints.
- Missing README sections or screenshots.

## Final Notes
- Keep `main` stable.
- Develop and test on `dev` first.
- Use clear commit messages that describe each release.
- Ensure another person can run your project by following this README only.
