from abc import ABC, abstractmethod


class Vendor(ABC):

    @abstractmethod
    def login(self, username, password):

        pass

    @abstractmethod
    def logout(self):

        pass