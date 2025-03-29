# Whenever youre working on new changes for a project you always want to be working on those changes
# in a branch separate from main, but eventually youll want to add your changes permanently to main
# this is where merge comes in.

# branches are used to safely make changes without affecting the primary branch where the permanent code
# resides. Once youre happy with the changes however you want to merge the branch into the primary one
# so that those changes can become apart of the main product.

# The typical workflow for pretty much every dev looks like this:
# 1. update repo to latest code with git fetch or pull
# 2. branch off the main branch and give it a name that represents what you're working on. Fix the bug,
#    create the feature, update the docs, etc. and create your one or more commits.
# 3. merge those changes back from your branch into the main line. At a company this will typically involve
#    sending some sort of pull request so that your changes can be evaluated and approved.


# If you merge a branch into main, git creates a new commit on main that has the histories of both main and
# the other branch as parents. This creates a merge commit.

# By default when you do git log it only shows the commits for the current branch, to show commits for all
# your branches add the --all flag. To make it a more visually revealing graph, showcasing the relationship
# between the commits add the --graph flag

# When you do git log, HEAD -> on a branch tip indicates what branch youre currently on.



# diverging history means that some branch such as main has commits, and at some point a branch was made
# which has it's own commits, the commit at which the branch was initially created is the base of the branch
# the most current commit of the branch is the tail.

# The main branch may continue to have commits added to it of which the second branch has no reference to
# it only has reference to its base commit on the main branch and all the parent commits before that.

# To merge the diverging histories we need to make a merge commit that represents the two histories as one.
# A merge commit will have both histories as a parent.


# The process for merge commit looks like this:
# 1. first we need to find the merge base or best common ancestor, which is the nearest ancestor in common
#    to both branches. It's the commit in which the branch was created.
# 2. you then replay main branches commits starting from the merge bae into a new commit,
# 3. then replay the second branches commits starting from the merge base into the same commit.
# 4. commit that new commit to main. It will be a special merge commit with two parents. The previous
#    commit on main and the head of the second branch.


# The --parents flag shows the hash of a commits parents



# git log showcases your commit history.
# --oneline gives you a condensed view of your history. The commit hashes are condensed to the first 7 chars
# which is all thats necessary to refer to a commit. Also you get the commit message

# --graph paints a bunch of lines to show how your history has diverged into branches and ome back together
# through merges

# --decorate gives branch and tag info. useful to see how far youve strayed from a branch, what branch
# youre on or where a previous branch might be. The values are no, short, and full. Short being the default
# no takes away the info, short just shows the branch name, full shows the path to the branch in the refs
# directory.

# --parents shows the hash of a commits parent. Especially useful for merge commits that have two parents.



# Fast forward merges are the simplest kind of merges. They occur when a feature branch has all the commits
# of the base branch (meaning no additional commits were added to main while working on the new branch)
# In that situation git will simply move the base branch pointer to the tip of the feature branch to merge
# This is called a fast-forward merge.
# When a fast forward merge occurs no merge commit is created. The base branch simply moves its tip pointer
# to the tip of the feature branch.


# Common workflow for a team of devs:
# 1. create a branch to work on a new feature or change
# 2. make the change
# 3. merge the branch back into main
# 4. remove the branch
# 5. repeat.

# Once you merge a branch you dont need it anymore and should remove it.

# You can do that with -d flagch




