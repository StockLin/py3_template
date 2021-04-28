import time
import logging
import abc


class IExample(abc.ABC):
    
    @abc.abstractmethod
    def run(self, name:str, period:int):
        raise NotImplementedError


class Example(IExample):

    def __init__(self, name="", period=10):
        self.__name = name
        self.__period = period

    def run(self, name="", period=0):
        try:
            self.__name = name if name else self.__name
            self.__period = period if period else self.__period

            logging.info(f"Start Example..... {self.__name }, {self.__period}")

            while True:
                print(f"hello my example[{self.__period}]...... {self.__name }")
                time.sleep(int(self.__period))

        except Exception as e:
            raise e