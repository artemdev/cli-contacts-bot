from helper_bot.src.constants import bcolors
from helper_bot.src.notes.note_book import NoteBook
from helper_bot.src.ui.NoteBookUserInterface import NoteBookUserInterface
from helper_bot.src.notes.note import Note
from helper_bot.src.notes.note_input_handler import NoteInputHandler


# ADD NOTE
def add_note_handler():
    new_note = Note()
    note_input_handler = NoteInputHandler()
    print(f"{bcolors.OKBLUE}Enter q to exit{bcolors.ENDC}")

    while True:
        # add title
        note_input_handler.get_title(new_note)

        # add description
        note_input_handler.get_description(new_note)

        if new_note.title.value == '' and new_note.description.value == '':
            print(
                f"{bcolors.FAIL}Note can't be without a title and description{bcolors.ENDC}")
        else:
            # add tags
            note_input_handler.get_tags(new_note)

            # add new note to notes list
            notes_database = NoteBook()
            try:
                notes_database.add(new_note)
                print(
                    f"{bcolors.OKGREEN}The note has been successfully added{bcolors.ENDC}")
            except Exception as e:
                print(f"{bcolors.FAIL}Something went wrong: {e}{bcolors.ENDC}")
            break


# SHOW ALL NOTES
def show_all_notes():
    notes_database = NoteBook()
    notes_ui = NoteBookUserInterface()

    if len(notes_database) == 0:
        notes_ui.not_found()
    else:
        notes_ui.show_all(notes_database)


# SEARCH NOTE
def search_note():
    notes_ui = NoteBookUserInterface()

    while True:
        print(f"{bcolors.OKBLUE}Choose an option:{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}1. Search in tags{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}2. Search in content{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}3. Exit{bcolors.ENDC}")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            search = input("Search: ")
            notes_database = NoteBook()
            result = notes_database.search(search.lower().strip(), 'tag')
            if result:
                is_printed = notes_ui.show_all(result)
                if is_printed:
                    break
            else:
                print(
                    f"{bcolors.WARNING}No results found for the query.{bcolors.ENDC}")
        elif choice == "2":
            search = input("Search: ")
            notes_database = NoteBook()
            result = notes_database.search(search.lower().strip(), 'content')
            if result:
                is_printed = notes_ui.show_all(result)
                if is_printed:
                    break
            else:

                notes_ui.not_found()

        elif choice == '3':
            break
        else:
            print(
                f"{bcolors.FAIL}Invalid choice. Please enter a valid number.{bcolors.ENDC}")


# DELETE _NOTE
def delete_note():
    print(f"{bcolors.WARNING}If you don't know the id, you can use 'search note' to search for the note, or 'show all notes' to display all notes{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Enter q to exit{bcolors.ENDC}")

    while True:
        entered_id = input("Enter the id of the note you want to delete: ")

        if entered_id == "q":
            break
        elif not entered_id:
            print(f"{bcolors.WARNING}Blank line is not a id.{bcolors.ENDC}")
        else:
            try:
                notes_database = NoteBook()
                is_deleted = notes_database.delete(int(entered_id))
                if is_deleted:
                    print(
                        f"{bcolors.OKGREEN}The note was successfully deleted{bcolors.ENDC}")
                    break
                else:
                    print(f"{bcolors.WARNING}Id not found.{bcolors.ENDC}")
            except ValueError:
                print(f"{bcolors.FAIL}The id must be a number.{bcolors.ENDC}")


# EDIT _NOTE
def edit_note():
    print(f"{bcolors.WARNING}If you don't know the id, you can use 'search note' to search for the note, or 'show all notes' to display all notes{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Enter q to exit{bcolors.ENDC}")
    while True:
        entered_id = input("Enter the id of the note you want to edit: ")

        if entered_id == "q":
            break
        elif not entered_id:
            print(f"{bcolors.WARNING}Blank line is not a id.{bcolors.ENDC}")
        else:
            notes_database = NoteBook()
            try:
                current_note = notes_database.get_note_by_id(int(entered_id))
                if not current_note:
                    print(f"{bcolors.WARNING}Id not found.{bcolors.ENDC}")
                else:
                    print(f"{bcolors.OKBLUE}Choose an option:{bcolors.ENDC}")
                    print(f"{bcolors.OKBLUE}1. Edit title{bcolors.ENDC}")
                    print(f"{bcolors.OKBLUE}2. Edit description{bcolors.ENDC}")
                    print(f"{bcolors.OKBLUE}3. Edit tags{bcolors.ENDC}")
                    print(f"{bcolors.OKBLUE}4. Exit{bcolors.ENDC}")

                    choice = input("Enter the number of your choice: ")

                    if choice == "1":
                        print(
                            f"{bcolors.WARNING}Title must contain at most 50 characters.{bcolors.ENDC}")
                        try:
                            new_title = input("Enter a new title: ")
                            notes_database.edit(
                                int(entered_id), new_title, 'title')
                            print(
                                f"{bcolors.OKGREEN}The title was successfully edited{bcolors.ENDC}")
                            break
                        except ValueError as e:
                            print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
                    elif choice == "2":
                        print(
                            f"{bcolors.WARNING}Description must contain at most 80 characters.{bcolors.ENDC}")
                        try:
                            new_description = input(
                                "Enter a new description: ")
                            notes_database.edit(
                                int(entered_id), new_description, 'description')
                            print(
                                f"{bcolors.OKGREEN}The description was successfully edited{bcolors.ENDC}")
                            break
                        except ValueError as e:
                            print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
                    elif choice == "3":
                        print(
                            f"{bcolors.WARNING}Tags must contain at most 40 characters.{bcolors.ENDC}")
                        print(
                            f"{bcolors.OKBLUE}Multiple tags can be separated with a comma{bcolors.ENDC}")
                        try:
                            new_tags = input("Enter new tags: ")
                            if len(new_tags) <= 80:
                                notes_database.edit(
                                    int(entered_id), new_tags, 'tags')
                                print(
                                    f"{bcolors.OKGREEN}The tags was successfully edited{bcolors.ENDC}")
                                break
                            else:
                                print(
                                    f"{bcolors.FAIL}Tags must contain at most 40 characters.{bcolors.ENDC}")
                        except ValueError as e:
                            print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
                    elif choice == '4':
                        break
                    else:
                        print(
                            f"{bcolors.FAIL}Invalid choice. Please enter a valid number.{bcolors.ENDC}")
            except ValueError:
                print(f"{bcolors.FAIL}The id must be a number.{bcolors.ENDC}")
