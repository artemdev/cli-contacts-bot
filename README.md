# Helper Bot
Personal Assistant (PA) is launched with the `helper` command, or through the `main.py` file.
The PA contains a contact book and a notebook.

### Package Installation
1. It is recommended to install and activate a virtual environment.
2. Navigate to the script folder and install it as a package with the command **pip install -e .**
3. After installation, launch the assistant from the console with the command **helper**.

### Contact Book
A contact in the contact book has a name and contains a list of phone numbers, 
as well as (optionally) a birth date, email address, and physical address.

There are several commands for working with the contact book:
- **create contact** - creates a contact: 
    after the command, enter the name (consisting of alphabet letters),
    phone number (consisting of digits, 10 characters long),
    email address (example goit@gmail.com),
    physical address,
    birth date (format day-month-year, example 12-01-2000).
- **add phone** - add a phone number to the selected contact's list of phones.
- **show contacts** - display all contents of the contact book.
- **search contact by name** - find a contact by the given name.
- **edit phone** - edit a phone number of the selected contact.
- **edit birthday** - edit the birth date of the selected contact.
- **edit address** - edit the address of the selected contact.
- **edit email** - edit the email address of the selected contact.
- **remove contact** - delete a contact.
- **remove phone** - delete a phone number from the selected contact.
- **remove birthday** - delete the birth date from the selected contact.
- **remove address** - delete the address from the selected contact.
- **remove email** - delete the email address from the selected contact.
- **search contact** - search for contacts by given information about the contact's name or phone number (either by letters or by numbers).
- **birthdays** - search for contacts with birthdays within a period (days) specified by the user.

### Notebook
A note consists of a title, description, and a list of tags. Each note has a unique identifier,
which is needed for managing the note (editing or deleting).

There are several commands for working with the notebook:
- **add note** - command to create a new note.
- **show all notes** - displays a list of all existing notes, with the option to sort the results by title, description, or tags.
- **search note** - command to search among notes, possible search by tags and by data in the note.
- **delete note** - command to delete a note.
- **edit note** - command to edit a note.

### Folder Sorting
Sorts files into corresponding categories:
images are moved to the images folder,
documents are moved to the documents folder,
audio files are moved to the audio folder,
video files to the video folder,
archives are unpacked, and their contents are moved to the archives folder,
files with unknown extensions are moved to the unknown folder.

Invoked with the command:
- **sort folder** - After which you need to specify the path to the folder to be sorted and the path where the result folder will be created.

### Commands to Terminate the Application
- **good bye**, **close**, **exit** - terminate the application.

<!--
Developed a Command-Line Interface (CLI) Application: Built a CLI application, [helper_bot](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fartem%2FDesktop%2Fprojects%2Fgoit-python%2Fcore%2Fcli-contacts-bot%2Fhelper_bot%2F__init__.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "helper_bot/__init__.py"), in Python that allows users to manage notes and contacts, and sort files in a directory. The application is structured in a modular way, with separate modules for different functionalities. The main entry point of the application is helper_bot/main.py.

Implemented Note Management System: Created a note management system in helper_bot/src/notes/notes_handler.py that allows users to add, view, search, delete, and edit notes. This system uses the NoteBook class from helper_bot/src/notes/note_book.py and the Note class from helper_bot/src/notes/note.py.

Built a Contact Management System: Developed a contact management system in helper_bot/src/contacts/work.py that allows users to create, add, edit, and remove contact information such as phone numbers, emails, addresses, and birthdays. This system uses the AddressBook and Record classes from helper_bot/src/contacts/classes.py.

Created User Interfaces for Different Modules: Designed user interfaces for the note and contact management systems in helper_bot/src/ui/NoteBookUserInterface.py and helper_bot/src/ui/ContactsUserInterface.py respectively. These interfaces provide feedback to the user based on their interactions with the application.

Integrated a File Sorting Utility: Integrated a file sorting utility in helper_bot/src/sorter/sort_folder.py that allows users to sort files in a directory. This utility is accessible from the main CLI of the application.
 -->
