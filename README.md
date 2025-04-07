# github-actions-pipeline
# GitHub Actions Workflow: Build, Auto-Merge, and Notify

This repository contains a comprehensive GitHub Actions workflow that includes building and testing your code, automatically merging approved pull requests, and sending notifications about the process results.

## Workflow Stages

### 1. Build
- Checks out your code
- Sets up Python environment
- Installs dependencies
- Runs linting with flake8
- Executes tests with pytest and generates coverage reports
- Uploads test results as artifacts

### 2. Auto-Merge
- Runs only on pull request events
- Checks if the PR has received the required approvals
- Automatically merges the PR if approved
- Uses squash merge strategy and deletes the source branch

### 3. Notify
- Sends notifications about the build and auto-merge results
- Supports multiple notification channels:
  - Slack notifications
  - Email notifications
  - Custom webhook notifications via a Python script

## Setup Instructions

1. **Repository Setup**
   - Place the workflow file in `.github/workflows/` directory
   - Create `.github/scripts/` directory and place the custom notification script there
   - Make the script executable: `chmod +x .github/scripts/custom_notification.py`

2. **Configure Secrets**
   - For Slack notifications:
     - Add `SLACK_WEBHOOK_URL` to your repository secrets
   - For email notifications:
     - Add `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_RECIPIENT` to your repository secrets
   - For custom webhook notifications:
     - Add `CUSTOM_WEBHOOK_URL` and `CUSTOM_API_KEY` (if needed) to your repository secrets

3. **Customize the Workflow**
   - Adjust the Python version as needed
   - Modify the build steps to match your project's requirements
   - Update the auto-merge criteria if necessary (e.g., required number of approvals)
   - Add or remove notification channels based on your preferences

## Workflow Triggers

This workflow is triggered by:
- Pull request events (opened, synchronized, reopened)
- Push events to main, master, and develop branches

## Files in this Repository

- `.github/workflows/build-automerge-notify.yml`: Main workflow file
- `.github/scripts/custom_notification.py`: Custom notification script
- `README.md`: This file

## Notes and Tips

- The auto-merge job will not run for pull requests created by Dependabot
- Make sure your repository has adequate permissions set for the GitHub token
- For the auto-merge functionality to work, you may need to:
  - Enable "Allow auto-merge" in your repository settings
  - Make sure branch protection rules allow the GitHub Actions bot to push to protected branches

## Customization

You can customize this workflow by:
- Adding more testing or build steps
- Changing the auto-merge criteria
- Adding different notification channels
- Modifying the notification format and content

