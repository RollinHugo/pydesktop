[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources
exec qtile start