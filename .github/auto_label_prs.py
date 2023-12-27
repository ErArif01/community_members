import os
from github import Github

# Get GitHub token from environment variable
token = os.getenv('GITHUB_TOKEN')

# Create a GitHub API client
g = Github(token)

# Get the current repository
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))

# Get the pull request number from the environment variables
pr_number = os.getenv('PULL_REQUEST_NUMBER')

# Get the pull request object
pr = repo.get_pull(pr_number)

# Your logic to determine labels based on PR content
labels = []
if 'keyword' in pr.title.lower() or 'keyword' in pr.body.lower():
    labels.append('label1')

# Add labels to the pull request
pr.set_labels(*labels)
