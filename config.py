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
