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



# A benefit of merge is it preserves the true history of the project, it shows when branches were merged and
# where. Though it can make a lot of merge commits making the history hard to read and understand.

# A liner history is generally easier to read understand and work with


# So essentially we can rebase a branch, which sets the base commit of the branch to being the tip of the
# main branch, instead of whatever it was before. And now that the new branch has knowledge of the entire
# main branch history we can avoid a merge commit and just conduct a fast-forward merge. This keeps our
# history much more linear and easy to read. We then delete the branch after merging, since we don't need it

# The one benefit of allowing merge commits over sticking to fast-forward merges is it keeps our true history
# We can see where divergences in history occurred and when/where merges happened.




