# Often our coworkers make code changes we need to accept into our repo's
# This is where the distributed in distributed VCS comes from.
# We can have remotes which are external repo's with mostly the same git history as our local repo

# When it comes to git (the cli tool) there isnt a central repo. Github is simply someone else's repo

# Github being used as a source of truth for our code is only convention.


# In git another repo other than your local repo is called a remote.
# The convention is that when youre treating the remote as your source of truth for your code (such as
# Github) you name the remote "origin"
# This remote is treated as the "true" repo. It's where you and your coworkers keep all of the up to date
# code.

# The syntax for attaching a remote to your repo is:
# git remote add <name> <uri>



# Adding a remote to a repo doesnt mean we have access to the contents of the remote. We have to fetch
# the contents.


# git fetch downloads all the content of the remotes .git/objects directory into the one in your local repo
# just because we fetched all the metadata of the remote doesnt mean we have all the files. To showcase
# run git log and youll see you have none of the remotes commits.

