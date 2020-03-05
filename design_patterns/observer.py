from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


# END OF Subject interface

class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I am doing something important.")
        self._state = randrange(0,10)

        print(f"Subject: My state has just changet to: {self._state}")
        self.notify()

# END OF ConcretetSubject

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreateObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreateObserver A: Reached to the event")

class ConcreateObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreateObserver B: Reached to the event")

if __name__ == "__main__":

    subject = ConcreteSubject()

    observer_a = ConcreateObserverA()
    subject.attach(observer_a)

    observer_b = ConcreateObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()






























