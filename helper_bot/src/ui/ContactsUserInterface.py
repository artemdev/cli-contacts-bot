from helper_bot.src.ui.UserInterface import UserInterface
from helper_bot.src.constants import bcolors


class ContactsUserInterface(UserInterface):
    def show_all(self, data):
        print(f'Contacts: {data}')

    def not_found(self):
        print('There are no contacts in Contact book')

    def contact_not_found(self, name):
        print(
            f'There is not contact witn name {bcolors.FAIL}{name}{bcolors.ENDC} in the contact book ')
