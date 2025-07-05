#!/bin/bash
set -e

# PIKAUR : python AUR wrapper
git clone https://aur.archlinux.org/pikaur.git
cd pikaur
makepkg -fsri
cd ..

# Qtile:
sudo pacman -S \
    qitle \
    ttf-dejavu \
    xterm \
    xorg-xinit \
    xorg-server \
    xorg-xrdb

pikaur -Sy powerline-fonts-git

# X11
sudo localectl set-x11-keymap fr
git clone https://github.com/solarized/xresources.git
cp xresources/Xresources.dark ~/.Xresources
cp xinitrc ~/.xinitrc
