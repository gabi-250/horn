# horn

`horn` is a console media player that aims to be as lightweight as possible.
It provides a simple console-based interface and behaves like any other media player.

### Features:
* Audio playback
  * Play/pause/stop the current media
  * Play the next item in the playlist
  * Volume control
* Playlists

### Roadmap:
`horn` was inspired by [`ranger`](https://github.com/ranger/ranger) in the sense
that the console player should be as configurable as possible.

In the future, `horn` aims to provide the following:
* Both `Vim`-like and `Emacs`-like keybindings
* a way to configure your keybindings
* a convenient way to browse files (i.e. use `ranger` inside of `horn` to import media)
* video playback
* a folder structure within the playlist (a sub-playlist in a sense)

### Dependencies:
* python3
* [Gstreamer 1.0](https://gstreamer.freedesktop.org/download/)
* [python-curses](https://docs.python.org/3.5/library/curses.html)
