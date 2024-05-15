from helper_bot.src.ui.UserInterface import UserInterface
import re


class HelpUserInterface(UserInterface):
    def show_all(self):
        reg_exp = re.compile(r'- \*\*.*')

        print('\nList of available commands:\n')
        with open('README.md', 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break

                if re.match(reg_exp, line):
                    print(line.replace('*', ''))
