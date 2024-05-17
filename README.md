# Helper bot
 Персональний помічник(ПП) запускається командою helper, або через файл main.py
ПП містить книгу контактів та книгу нотаток

### Встановлення пакету
1. Рекомендовано встановити та активувати вiртуальне оточення
2. Перейти в папку скрипту та встановити його як пакет командою **pip install -e .**
3. Після встановлення запустити помiчника з консолі командою **helper**

### Книга контактів
Контакт книги контактів має назву(ім"я) та містить список телефонів , 
а також (необов"язково) дату народження, електронну адресу та адресу.

Є ряд команд по роботі з книгою контактів:
- **create contact** - створення контакту: 
    після команди вводиться ім"я(складається з літер алфавіту)
    номер телефону(складається з цифр  в кількості 10 символів)
    електронна адреса(приклад goit@gmail.com)
    адреса
    дата народження(формат день-місяць-рік, приклад 12-01-2000)
- **add phone** - добавити номер телефону до списку телефонів обраного контакту
- **show contacts** - показати весь вміст книги контактів
- **search contact by name** - знайти контакт за заданим іменем
- **edit phone** - редагувати номер телефону з заданого контакту
- **edit birthday** - редагувати дату народження з заданого контакту
- **edit address** - редагувати адресу з заданого контакту
- **edit email** - редагувати електронну адресу з заданого контакту
- **remove contact** - видалити контакт
- **remove phone** - видалити номер телефону з заданого контакту
- **remove birthday** - видалити дату народження з заданого контакту
- **remove address** - видалити адресу з заданого контакту
- **remove email** - видалити електронну адресу з заданого контакту
- **search contact** - пошук контактів за заданою інформацією про ім"я контакту або номер телефону(або по буквам або по цифрам)'''
- **birthdays** - пошук контактів з днями народження у період (днів) заданий користувачєм

### Книга нотатків
 Нотаток  складаеться з назви, опису та списку тегів. Кожен нотаток має унікальний ідентифікатор,
 який потрібен для управління нотатком(редагування чи видалення)

Є ряд команд по роботі з книгою нотатків:
- **add note** - команда для створення нового нотатку
- **show all notes** - виводить список всіх існуючих нотатків, з можливістю сортування результату за назвою, описом чи тегами
- **search note** - команда для пошуку серед нотатків, можливий пошук по тегам та по данним в нотатку
- **delete note** - команда для видалення нотатку
- **edit note** - команда для редагування нотатку

### Сортування папки
Сортує файл за відповдіними категоріями:
зображення переносяться до папки images
документи переносяться до папки documents
аудіо файли переносяться до audio
відео файли до video
архіви розпаковуються, та їх вміст переноситься до папки archives
файли з невідомими розширеннями переносяться в папку unknow

Викликається командою:
- **sort folder** - Після чого порібно вкзати шлях до папки, яку потрібно відсортувати та шлях де буде створена папка з результатом сортування

### Команди для завершення роботи з додатком
- **good bye**, **close**, **exit** - завершення роботи додатка


Developed a Command-Line Interface (CLI) Application: Built a CLI application, [helper_bot](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fartem%2FDesktop%2Fprojects%2Fgoit-python%2Fcore%2Fcli-contacts-bot%2Fhelper_bot%2F__init__.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "helper_bot/__init__.py"), in Python that allows users to manage notes and contacts, and sort files in a directory. The application is structured in a modular way, with separate modules for different functionalities. The main entry point of the application is helper_bot/main.py.

Implemented Note Management System: Created a note management system in helper_bot/src/notes/notes_handler.py that allows users to add, view, search, delete, and edit notes. This system uses the NoteBook class from helper_bot/src/notes/note_book.py and the Note class from helper_bot/src/notes/note.py.

Built a Contact Management System: Developed a contact management system in helper_bot/src/contacts/work.py that allows users to create, add, edit, and remove contact information such as phone numbers, emails, addresses, and birthdays. This system uses the AddressBook and Record classes from helper_bot/src/contacts/classes.py.

Created User Interfaces for Different Modules: Designed user interfaces for the note and contact management systems in helper_bot/src/ui/NoteBookUserInterface.py and helper_bot/src/ui/ContactsUserInterface.py respectively. These interfaces provide feedback to the user based on their interactions with the application.

Integrated a File Sorting Utility: Integrated a file sorting utility in helper_bot/src/sorter/sort_folder.py that allows users to sort files in a directory. This utility is accessible from the main CLI of the application.
