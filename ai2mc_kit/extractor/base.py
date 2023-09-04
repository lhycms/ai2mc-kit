from abc import ABCMeta, abstractclassmethod

class BaseExtractor(ABCMeta):
    @abstractclassmethod
    def extract(self):
        pass