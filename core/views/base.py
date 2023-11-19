import abc


# Абстрактный метод для goalview, диктующий правила
# всем остальным view
class View(abc.ABC):

    @abc.abstractmethod
    def update_view(self):
        pass

    @abc.abstractmethod
    def clear_view(self):
        pass
