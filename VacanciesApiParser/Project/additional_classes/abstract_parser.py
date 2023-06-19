import requests

from abc import ABC
from abc import abstractmethod

from .vacancy_impl.vacancy import Vacancy


class GenericParser(ABC):

    @abstractmethod
    def get_vacancies(self, pages_count: int, keywords: list[str]) -> list[Vacancy]:
        pass

    @abstractmethod
    def parse_vacancy(self, vacancy_info: dict) -> Vacancy:
        pass

    @abstractmethod
    def make_request(self, url: str) -> requests.Response:
        pass
