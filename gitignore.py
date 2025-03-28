# It's common to run git add . to stage all changed files at once. This is bad for when you have a file
# in your working directory you dont want committed though, such as auto generated files like .pyc or
# __pycache__ or files containing secrets like .env. or node_modules for js.

# A .gitignore file solves this by execluding whatever files are referenced in it from being committed


# To ignore all files of a certain pattern use the wildcard:
# *.txt

# to ignore something in just the directory the gitignore is in but not the sub-directories use /
# /main

# To negate ignoring something:
# *.txt
# !important.txt

