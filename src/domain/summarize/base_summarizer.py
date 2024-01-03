import abc

class BaseSummarizer(abc.ABC) :

    @abc.abstractmethod
    def __call__(self) :
        raise NotImplementedError