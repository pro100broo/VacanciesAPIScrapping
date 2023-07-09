"""
Main function for user interaction

"""

from open_api_websites import OpenApiWebsitesParser
from superjob import SuperJobParser
from trudvsem import TrudvsemParser
from json_db import JsonDB

from utills.colors import Color


class App:

    def main_loop(self):
        print(f"\n{Color.white}Welcome to JobsApiParser. "
              f"Enter {Color.yellow}help{Color.white} option to see the commands list")
        while True:
            match input("\n>>> ").split():
                case "help", :
                    print(
                        f"\n{Color.yellow}1. Load vacancies from the website, then save them to json file{Color.white}\n\n"
                        f"{Color.cyan}Command:{Color.white}\n"
                        f"load vac 'website_name' 'number_of_pages' *args\n\n"
                        f"{Color.cyan}Description:{Color.white}\n"
                        f"website_name: hh | superjob | zarplata | trudvsem\n"
                        f"pages: int > 0\n"
                        f"*args: search keywords separated by spaces (example: Python Django SQL)\n"
                        f"\n{Color.yellow}2. Show saved vacancies{Color.white}\n\n"
                        f"{Color.cyan}Command:{Color.white}\n"
                        f"show vac\n"
                        f"\n{Color.yellow}3. Show saved vacancies sorted by salary{Color.white}\n\n"
                        f"{Color.cyan}Command:{Color.white}\n"
                        f"show sorted vac 'order' 'number_of_vacancies'\n\n"
                        f"{Color.cyan}Description:{Color.white}\n"
                        f"order: inc (increasing) | desc (descending)\n"
                        f"number_of_vacancies: int > 0\n"
                        f"\n{Color.yellow}4. Delete saved vacancies{Color.white}\n\n"
                        f"{Color.cyan}Command:{Color.white}\n"
                        f"del vac"
                    )

                case "load", "vac", website, pages, *keywords:
                    match website:
                        case "hh":
                            JsonDB.save_vacancies(open_api_parser.get_vacancies(int(pages), keywords, "hh"))
                        case "zarplata":
                            JsonDB.save_vacancies(open_api_parser.get_vacancies(int(pages), keywords, "zarplata"))
                        case "superjob":
                            JsonDB.save_vacancies(superjob_api_parser.get_vacancies(int(pages), keywords))
                        case "trudvsem":
                            JsonDB.save_vacancies(trudvsem_api_parser.get_vacancies(int(pages), keywords))
                        case _:
                            print(f"{Color.red}Wrong website name. Check description of the command{Color.white}")

                case "show", "vac":
                    for vacancy in JsonDB.get_vacancies():
                        print(vacancy)

                case "show", "sorted", "vac", order, number_of_vacancies:
                    match order:
                        case "desc":
                            self.print_sorted_vacancies("desc", number_of_vacancies)
                        case "inc":
                            self.print_sorted_vacancies("inc", number_of_vacancies)
                        case _:
                            print(f"{Color.red}Wrong order. Check description of the command{Color.white}")

                case "del", "vac":
                    JsonDB.delete_vacancies()
                    print(f"{Color.green}Vacancies list was successfully cleaned{Color.white}")

                case "quit", :
                    return 0

                case _:
                    print(f"{Color.red}Wrong command{Color.white}")

    @staticmethod
    def print_sorted_vacancies(order: str, number_of_vacancies: int):
        sorted_vacancies = list(sorted(JsonDB.get_vacancies(), key=lambda vac: vac))

        if order == "inc":
            for i in range(number_of_vacancies):
                print(sorted_vacancies[i])
        else:
            reversed_sorted_vacancies = sorted_vacancies[::-1]
            for i in range(number_of_vacancies):
                print(reversed_sorted_vacancies[i])


if __name__ == '__main__':
    open_api_parser = OpenApiWebsitesParser()
    superjob_api_parser = SuperJobParser()
    trudvsem_api_parser = TrudvsemParser()

    app = App()
    app.main_loop()
