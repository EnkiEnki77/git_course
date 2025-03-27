# The first step of any project is to create a repo
# A git repo represents a single project

# A repo is essentially a directory that contains a project and a hidden .git directory where git stores
# all of it's internal tracking and versioning info for the project.


# To initialize a git a repo, go into an empty directory and run git init. This creates a hidden .git
# directory in your project directory


# A file can be in several states in a git repo:
# untracked: not being tracked by git
# staged: marked for inclusion in the next commit
# committed: saved to the repo history

# git status will show you the current state of your repo, giving you the current status of each file


# When a file is first added to the project it starts off untracked in your git repo, to stage it (mark it
# inclusion in the next commit) run git add <filename> to stage individual files, or git add . to stage
# all untracked files.
# Without staging every file in the repo would be included in every commit.

# To unstage a file run git rm --cached <file>

# arguments with <> are required, arguments with [] are optional.


# After staging a file you can commit it
# A commit is a snapshot of the repo at a given point in time. It's a way to save the state of the repo,
# and is how git keeps track of changes to the project.
# A commit comes with a message that describes changes made in the commit.
# The command is:
# git commit -m "commit message"


# A git repo is a potentially very long list of commits, where each commit represents the full state of
# the repo at a given point in time.

# git log shows a history of the commits in the repo, you can see who made a commit, when it was made, and
# what was changed.

# Each commit has a commit hash that uniquely identifies it. You can refer to any commit in git by the
# first 7 characters of it's hash


