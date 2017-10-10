# dmenu-bookmarks

Run a browser onto a bookmark selected with dmenu

## Usage

    bookmarks <browser> <urlprefix> <bookmarks.txt> <dmenuopts ...>

Integrates well with a minimalist window manager such as i3 :

    bindsym $mod+shift+b exec bookmarks chrome --app= $HOME/.bookmarks.txt -fn "Terminus:size=14"

## bookmarks.txt

One line per URL

Keep protocol if browser call requires it (chrome's `--app` for instance)

    https://news.ycombinator.com
    https://reddit.com
