#!/bin/bash
set -e

mkdir -p ~/.config/rofi/ ~/.config/qtile/ ~/.config/alacritty/
cp config/qtile/*.py ~/.config/qtile/
cp config/rofi/* ~/.config/rofi/
cp config/alacritty/* ~/.config/alacritty/
cp xinitrc ~/.xinitrc