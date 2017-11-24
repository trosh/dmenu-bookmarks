# dmenu-bookmarks

Run a browser onto a bookmark selected with dmenu

## Usage

    bookmarks <browser> <urlprefix> <bookmarks.txt> <dmenuopts ...>

Integrates well with a tabless browser and a modular window manager such as i3 :

    bindsym $mod+shift+b exec bookmarks chrome --app= $HOME/.bookmarks.txt -fn "Terminus:size=14"

## bookmarks.txt

One line per URL pattern

* Fully formed URL (including protocol prefix)

      https://news.ycombinator.com
      https://reddit.com

* Partially formed URL

      python.org

* Search pattern (abbreviation followed by a space before search query)

  * DuckDuckGo

        d how much wood would a woodchuck chuck

  * Google

        g would a woodchuck even chuck wood

  * YouTube

        y woodchuck chucking wood

  * Wikipedia search

        w woodchuck wood chucking

  * Wikipedia specific page

        wp woodchuck

  * Hidden pattern (space prefix)

         d whats a groundhog
