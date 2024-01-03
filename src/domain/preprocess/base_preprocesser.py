import abc

class BasePreprocessor(abc.ABC) :


    @abc.abstractmethod
    def __call__(self) :
        raise NotImplementedError