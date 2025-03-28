# Branches allow you to keep track of different changes separately

# You can work on features seeing how they work out, if you like the changes you can merge the branch
# into the main line making the changes permanent, if not you can just delete the branch and go back to
# the main line.

# Branching is a way to essentially prototype changes before making them permanent.

# A branch is just a named pointer to a specific commit. When you create a branch youre creating a new
# pointer to a specific commit. The commit the branch points to (the most recent in the branch) is called
# the tip of the branch

# Because a branch is just a pointer to a commit they're cheap to create.

# To check what branch you're on: git branch


# The default branch for git is master

# However, the default github branch is main, so you should change your default to main:
# git branch -m oldname newname
# Should also change it in the global config: init.defaultBranch


# Commits on the main line before a branch is made are also a part of that branch


# To create a branch: git branch new_branch

# beterr to use switch so that you instantly switch to it though: git switch -c new_branch
# the -c flag tells git to make a new branch if the one we're trying to switch to doesnt exist.

# When you create a branch it uses the current commit you're on as the branch base, and the most
# recent commit in the branch is the tip.


# The old syntax for switching branches is git checkout. Switch is newer and more preferred though.

# Git log shows which commit each branch tip points to


# To make git log easier to read you can use the --decorate flag with short, full, or no as value

# Full shows the full ref name of your commit. a ref is just a pointer to a commit, all branches are refs

# Then theres git log --oneline, it makes the log much more compact.



# Git stores all its info in files in the .git directory at the root of your project. Even info about branches
# The heads or tips of branches are stored in .git/refs/heads directory. If you cat into one of those files
# youll see the commit hash the branch points to.


# To find the filepath of a certain file in a directory: find path/to/search -name file.txt


# some new stuff for stuff and stuff

