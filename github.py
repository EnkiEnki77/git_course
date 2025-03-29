# Github is the most popular website for hosting remote git repositories.

# It serves as a backup of all your code on the cloud in case you lose your computer
# A central place to share your code and collaborate with others
# A public portfolio for all your coding projects

# In github you can create remote repo's hosted on their servers, and then initialize a local repo on
# your machine and connect it to the remote.


# Run git ls-remote to ensure a remote is connected.



# Git push sends any local changes in the current branch of our local repo to the connected remote repo
# branch of the same name.
# You need to be authenticated with the remote to push changes to it.

# git push origin main

# you can also push to a branch on the remote of a different name:
# git push origin <local_branch>:<remote_branch>

# You can also delete a remote branch by pushing an empty branch to it:
# git push origin :<remote_branch>

# Fetching allows you to grab the remote git repos metadata (all the stuff in the .git/objects directory)
# To grab the actual file changes we use git pull.
# git pull origin main



# On Github a pull request is a way to propose changes, typically to the rest of your team or the maintainer
# of a project you're contributing to.

# Pull requests allow team members to see what changes are being proposed and discuss them before they are
# merged into the main code base.

# Write changes on a branch other than main, then push the new branch to the github repo.
# Go to the pull requests tab and create a new pull request
# Set main as the base and the second branch as the compare branch so you can merge the second branch
# into main later.



# Configure git to rebase on pulls from github instead of merge, that way you can keep a linear commit
# history:
# git config --global pull.rebase true



# Workflow when in a team:
# 1. update local main branch whenever you start working with: git pull origin main
# 2. checkout a feature branch for changes you want to make with git switch -c <branch_name>
# 3. make changes to files
# 4. git add .
# 5. git commit
# 6. git push origin <branch_name>. dont push to main
# 7. open a pull request on github to ask permission to merge your changes into main.
# 8. ask a team member to review pull request
# 9. once approved click merge on github to merge your branch into main
# 10. delete feature branch, and repeat with a new branch for next set of changes.


# Locally after you approve a pull request and merge it you should delete the feature branch then in your
# local repo switch back to main and pull from origin to sync with it



# To avoid having to make a directory and git init, set remote, etc. Just git clone your github repo
# If you make a github repo first and clone it down the remote connection is made automatically for you.


# A README is a markdown documentation file that explains what your project is and how to run it.


# You can view your diff with the git diff command, a diff is a visual aid that shows you the difference
# between two files.



# Commits are supposed to be a snapshot of your code at a single point in time, they should represent a
# single logical change to your code. Things like the addition of a new feature, fixing a bug, refactoring
# some of your code for readability.







