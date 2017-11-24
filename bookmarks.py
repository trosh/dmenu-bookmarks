#!/usr/bin/env python3
"""
Start a browser based on user input typed into dmenu
"""

from sys import argv
from subprocess import check_output, run

# Accronyms to be typed at the start of the dmenu input (followed by a space)
# and corresponding base search URL
PREFIXES = {
    "g"   : ("+", "https://www.google.com/search?q="),
    "d"   : ("+", "https://www.duckduckgo.com/?q="),
    "y"   : ("+", "https://www.youtube.com/results?search_query="),
    "yt"  : ("+", "https://www.youtube.com/results?search_query="),
    "we"  : ("+", "https://en.wikipedia.org/w/index.php?search="),
    "wf"  : ("+", "https://fr.wikipedia.org/w/index.php?search="),
    "wpe" : (" ", "https://en.wikipedia.org/wiki/"), # Exact page name
    "wpf" : (" ", "https://fr.wikipedia.org/wiki/"), # Exact page name
}

def build_search(prefix, query, sep):
    """
    Create search URL
    @param  prefix  Base search URL
    @param  query   Space-separated search query
    @return  Search URL ready for browser
    """
    return prefix + query.replace(" ", sep)

def determine_url(result):
    """
    Choose what URL to pass to browser based on user input
    @param  result  User-given string typed in dmenu
    @return  Protocol-prefixed URL ready for browser
    """
    # Is `result` a fully formed URL ?
    if "://" in result:
        url = result
    else:
        # Is `result` a search pattern ?
        for accro, prefix in PREFIXES.items():
            if result.startswith(accro + " "):
                url = build_search(prefix[1],
                                   result[len(accro)+1:],
                                   prefix[0])
                break
        else:
            # Is `result` a partially formed URL  ?
            if " " not in result and "." in result:
                url = "https://" + result
            # Default : duckduckgo search
            else:
                sep, prefix = PREFIXES["d"]
                url = build_search(prefix, result, sep)
    return url

def main(browser, urlprefix, bookmarkstxt, dmenuopts):
    """
    Get user input from dmenu, build resulting URL,
    append input to bookmarkstxt if not hidden, run browser
    @param  browser       String to execute to run the browser (e.g. "firefox")
    @param  urlprefix     String to place directly before the URL
                          in the browser call (e.g. "--url=")
    @param  bookmarkstxt  Filename of the file to pipe into dmenu
                          (e.g. "/home/user/.bookmarks.txt")
    @param  dmenuopts     Optional arguments to pass to dmenu
                          (e.g. "-fn", "Courier")
    """
    # Pipe bookmarkstxt to dmenu, get user input as result
    with open(bookmarkstxt, "r") as bookmarks:
        result = check_output(["dmenu", "-p", bookmarkstxt]
                              + dmenuopts,
                              stdin=bookmarks
                             ).decode("utf8").rstrip()
    # Check if result should be kept hidden (space prefix)
    if result.startswith(" "):
        result = result[1:]
    else:
        # Is result in bookmarkstxt ?
        result_present = False
        with open(bookmarkstxt, "r") as bookmarks:
            for line in bookmarks:
                if line.rstrip() == result:
                    result_present = True
                    break
        if not result_present:
            # Append result to bookmarkstxt
            with open(bookmarkstxt, "a") as bookmarks:
                bookmarks.write(result + "\n")
    url = determine_url(result)
    run([browser, urlprefix + url])

if __name__ == "__main__":
    main(argv[1], argv[2], argv[3], argv[4:])
