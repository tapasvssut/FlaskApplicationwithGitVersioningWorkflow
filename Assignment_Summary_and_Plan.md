# Assignment Summary and Execution Plan

## Source
This summary is based on the file:
- Assignment_ Flask Application with Git Versioning Workflow.pdf

## Assignment Summary
The assignment asks you to build a small Flask web application and manage its development using a strict Git branching workflow.

Main goals:
1. Build a working Flask app with required endpoints.
2. Use Git professionally with separate `dev` and `main` branches.
3. Release the app in two versions (Version 1 and Version 2).
4. Publish the project to GitHub with clear commit and merge history.
5. Write complete documentation in README so anyone can run and understand the project.

## Mandatory Workflow Requirements
You must follow this flow:
1. Initialize Git in the project folder.
2. Create `dev` branch.
3. Do all development only in `dev`.
4. Merge `dev` into `main` only after features are complete and tested.
5. Repeat the same process for each release version.

Evaluator will check that `main` has stable code and that history clearly shows version progression.

## Task-Wise Breakdown
### Task 1: Basic Flask App
Required endpoints:
- `/` -> Welcome to the App
- `/health` -> App is running

### Task 2: Git Setup + Version 1 Release
Required sequence:
1. `git init`
2. Create and switch to `dev`
3. Commit files with meaningful message
4. Push `dev`
5. Merge `dev` into `main`
6. Push `main`

### Task 3: Feature Implementation (Choose one)
Option A: Voting App
- `/vote/<name>`: add vote for candidate
- `/results`: return all votes in JSON

Option B: Password Manager
- `/add` (POST): store username/password from JSON
- `/get/<username>` (GET): fetch password or return error

### Task 4: Version 2 Enhancement
If Option A (Voting):
- Add `/reset` to clear all vote data

If Option B (Password Manager):
- Add `/delete/<username>` to delete stored user data

Then follow same Git release flow from `dev` to `main`.

### Task 5: README Documentation
README must include:
1. Project title and simple description
2. Installation and setup commands
3. API endpoint table (URL, method, behavior, sample response)
4. Git workflow explanation (`dev` and `main`)
5. Version history (V1 vs V2)
6. Mandatory embedded screenshots:
   - App running in browser
   - GitHub page showing `dev` and `main`
   - Commit/merge history showing V1 and V2

## Execution Plan (Practical)
### Phase 1: Environment and Base App
1. Create project folder and files (`app.py`, `requirements.txt`, `.gitignore`, `README.md`).
2. Install Flask.
3. Implement `/` and `/health`.
4. Run app and verify on localhost.

### Phase 2: Version 1 Development in dev Branch
1. Initialize Git and create `dev` branch.
2. Implement chosen feature set (Voting or Password Manager core endpoints).
3. Test endpoints with browser/Postman.
4. Commit with clear message: Version 1 feature completion.
5. Push `dev`, merge to `main`, push `main`.

### Phase 3: Version 2 Enhancement in dev Branch
1. Switch back to `dev`.
2. Add required enhancement endpoint (`/reset` or `/delete/<username>`).
3. Test complete flow.
4. Commit with clear message: Version 2 enhancement.
5. Push `dev`, merge to `main`, push `main`.

### Phase 4: Documentation and Submission
1. Finalize README with all required sections.
2. Add screenshots into README using Markdown image links.
3. Verify repository branch list and commit history are visible on GitHub.
4. Re-check app runs without errors.

## Suggested Commit Messages
- `Version 1: add base Flask app and core endpoints`
- `Version 1: add voting feature with results endpoint`
- `Version 2: add reset endpoint for voting data`
- `docs: complete README with workflow and screenshots`

## Quality Checklist Before Submission
- App runs successfully on localhost.
- All required endpoints return correct responses.
- JSON endpoints return valid JSON.
- Development done in `dev`, not directly in `main`.
- Two clear releases visible in merge history.
- README has all required sections and screenshots.
