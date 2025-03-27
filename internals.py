# Commit hashes are derived from their content changes, but some other stuff that effects the hash
# is the commit message, authors name and email, date and time, parent(previous) commit hashes.
# So hashes are almost always unique

# Git use a cryptographic hash algorith called SHA to generate it's hashes.


# All the data in a git repo is stored in the hidden .git directory. That includes all commits, branches,
# tags, and other objects.

# Git is made up of objects that are stored in the .git/objects directory. A commit is just a type of
# object.



# git cat-file -p <hash> lets you see the contents of a given git object, such as a commit.



# tree's are gits way of storing directories
# blob's are git's way of storing files

# When you cat-file a commit object file youll see the tree object it resides in, the author, the commiter,
# and the commit message. To see the content of the files committed themselves youd have to look inside the
# blob object

# If you git cat-file the tree object that you find inside the commit object you'll see the blob object
# Which contains the contents of the files that were committed.


# When you cat-file a commit object youll see the parent object and its hash representing the parent(previous)
# commit on the line, and youll see the tree object and it's hash that stores all of the commits changed
# content data. In the commits tree object youll find all the files and directories staged into the commit
# in the form of tree and blob objects, you can then peep into each of their contents by cat-filing into
# them.



# Git stores an entire snapshot of files on a per commit level, not just the changes.

# For optimization git compresses and packs files to store them more efficiently
# Git deduplicates files that are the same across different commits, if a file didnt change git only
# stores it once.

