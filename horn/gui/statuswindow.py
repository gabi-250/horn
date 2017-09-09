# -*- coding: utf-8 -*-

from horn.event.event import EventObserver
from horn.player.player import Player
from ..player import player


class StatusWindow(EventObserver):

    def __init__(self):
        EventObserver.__init__(self)
        Player.instance().add_observer(self)
