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

# On Github a pull request is a way



