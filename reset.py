# git reset command be used to undo the last commit or any change in the index (staged but uncommitted
# changes) or worktree (unstaged changes)

# the --soft flag is useful if you just want to go back to a previous commit but keep all your changes.
# Committed changes will be uncommitted and staged, staged and unstaged changes will be left alone.


# So if you want to go back to a previous commit but keep changes use --soft
# If you want to go back to a previous commit, but discard the changes use --hard


# When you run git status if it says working tree clean it means there are no unstaged changes.
# If git identifies changes to file that havent been stage (added to the index) the changes will be in
# the working tree


# Be really careful when using git reset --hard, you can end up permanently deleting your work. This will
# remove changes from your git repo and set your project back to the previous commit. You wont be able
# to recover those changes.

# git reset --hard commit_hash will reset your working directory (project) and index to the state of the
# commit youre resetting to. discarding all commit changes after.

