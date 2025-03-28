# rebase helps you take the diverging commits from one branch and move them to the tip of the base
# branch the feature branch is based on.
# So instead of creating a merge commit between the tips of feature and base branch;
# the tip of the base branch now becomes the base commit of the feature branch and a fast-forward merge
# can occur.
# This can allow you to maintain a merge commit free history, since all merges will be fast-forward merges.



# If you dont want to branch off the tip of the main line you can pass in a commit hash to specify what
# youd like the base commit to be.

# git switch -c branch_name base_hash


# To use rebase switch to the branch youd like to rebase onto the tip of main and run:
# git rebase main

# This does the following:
# 1. Checkout the latest commit on main to a temp location
# 2. Replay each commit one at a time from the branch youre rebasing into this temp location
# 3. Update the rebase branch to point to the last replayed commit in the temp location, this effectively
#    makes it now the rebase branch.
# 4. the rebase doesnt effect the main branch, the rebase branch now just includes all of main, meaning
#    you can now conduct a fast-forward merge/commit on main.


