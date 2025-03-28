# To interact with the git config: git config
# To add a configuration: --add
# To store the configuration in your global config ~/.gitconfig: --global
# To store the configuration in the local repo only: omit --global

# To view your config: git config --list --local | --global
# Or view it directly: cat .git/config (local) ~/.gitconfig (global)

# To get a single value from the config add the --get flag: git config --get section.key

# To remove a key use --unset flag: git config --unset section.key


# Typically in a key/value store like a python dictionary you arent allowed to have duplicate kyes
# git doesnt care though

# To unset all of a given key: git config --unset-all section.key


# Don't add sections to your git config that git doesnt use. To remove a section use:
# git config --remove-section section



# There are four places git can be configured, from more general to more specific they are:
# 1. system (/etc/gitconfig): allows git config for whole systeme
# 2. global (~/.gitconfig): allows git config for all the projects of a single user
# 3. local (.git/config): allows git config for a specific repo of a single user
# 4. worktree (.git/config.worktree): allows git config for a part of a specific repo of a single user


# 90% of the time youll use global to set things like name and user name, other 9% youll use local
# to set project-specific config. The last 1% you might need to mess with system and worktree

# Configurations set in more specific locations override more general locations. For example setting name
# in local will override global.


