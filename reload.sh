#!/bin/bash
set -e

mkdir -p ~/.config/rofi/ ~/.config/qtile/
cp config/qtile/*.py ~/.config/qtile/
cp config/rofi/* ~/.config/rofi/
cp xinitrc ~/.xinitrc