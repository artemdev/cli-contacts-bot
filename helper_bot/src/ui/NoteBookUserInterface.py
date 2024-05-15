from helper_bot.src.ui.UserInterface import UserInterface
from helper_bot.src.constants import bcolors, note_header, underline


class NoteBookUserInterface(UserInterface):
    def show_all(self, result):
        print(f"{bcolors.OKBLUE}Do you want to sort the result?{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}1. No{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}2. Yes, by title{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}3. Yes, by tags{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}4. Yes, by description{bcolors.ENDC}")
        while True:
            to_sort_by = input("Enter the number of your choice: ")

            if to_sort_by == '1':
                self.print_table(result)
                return True
            elif to_sort_by == '2':
                sorted_results = dict(
                    sorted(result.items(), key=lambda x: x[1].title))
                self.print_table(sorted_results)
                return True
            elif to_sort_by == '3':
                sorted_results = dict(
                    sorted(result.items(), key=lambda x: x[1].tags))
                self.print_table(sorted_results)
                return True
            elif to_sort_by == '4':
                sorted_results = dict(
                    sorted(result.items(), key=lambda x: x[1].description))
                self.print_table(sorted_results)
                return True
            else:
                print(
                    f"{bcolors.FAIL}Invalid choice. Please enter a valid number.{bcolors.ENDC}")

    def not_found(self):
        print(f"Notes not found")

    def search_not_found(self):
        print(f"{bcolors.WARNING}No results found for the query.{bcolors.ENDC}")

    def print_table(self, data):
        print(underline)
        print(note_header)
        print(underline)
        for key, note in data.items():
            print("|{:^6}|{:^52}|{:^42}|{:^82}|".format(key, str(note.title) or 'undefined',
                                                        ', '.join(
                                                            p.value for p in note.tags) or 'undefined',
                                                        str(note.description) or 'undefined'))
        print(underline)
