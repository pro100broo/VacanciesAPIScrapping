from abc import ABC
from abc import abstractmethod

from .vacancy_impl.vacancy import Vacancy


class GenericDB(ABC):

    @staticmethod
    @abstractmethod
    def get_vacancies() -> list[Vacancy]:
        pass

    @staticmethod
    @abstractmethod
    def save_vacancies(vacancies: list[Vacancy]) -> None:
        pass

    @staticmethod
    @abstractmethod
    def delete_vacancies() -> None:
        pass



