# Qtile

## Installation (Arch based)

Install Qtile and dependencies:

```
sudo pacman -S qtile pacman-contrib
yay -S nerd-fonts-ubuntu-mono
pip install psutil
```

Test it with **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile
```

## Structure

In ```config.py```, which is the file where most people write ALL their config, I put very little.
Most all of my configuration is broken up into a number of smaller files that are imported as libraries.

If you want to modify keybindings, open ```./settings/keys.py```. To modify
workspaces, use ```./settings/groups.py```. Finally, if you want to add more
layouts, check ```./settings/layouts.py```, the rest of files don't need any
configuration to get started.

## Autostart
If you want to change *autostart* programs, open  ```./autostart.sh``` and change what programs you want to use.

## Color Themes

They are easy to create.  It only takes a handful of colors, you create them based on popular terminal or editor themes.

To set a theme, check which ones are available in ```./themes```, and write
the name of the theme you want in a file named ```./config.json```:

```json
{
    "theme": "material-ocean"
}
