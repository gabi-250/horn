from horn.gui.widget import Widget
import abc
import curses


class PlayerWindow(Widget):
    __metaclass__ = abc.ABCMeta

    def __init__(self, win):
        Widget.__init__(self)
        self._win = win

    def resize(self, y, x, height, width):
        try:
            self._win.resize(height, width)
            self._win.mvwin(y, x)
            self._win.clear()
            self._win.refresh()
        except curses.error:
            # ignore curses errors for now
            pass
        self._dirty = True
