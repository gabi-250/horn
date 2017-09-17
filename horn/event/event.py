from enum import Enum
from abc import ABC, abstractmethod
import threading


class Event(Enum):
    play = 0
    pause = 1
    stop = 2
    next = 3
    progress = 4
    new = 5


class EventProducer(object):

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def send_event(self, event):
        for obs in self._observers:
            obs.update(event)


class EventObserver(ABC):
    def __init__(self, event_producer):
        event_producer.add_observer(self)

    @abstractmethod
    def update(self, event):
        pass
