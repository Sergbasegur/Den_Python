import fileNote
import Note
import uiNote

number = 1  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = uiNote.create_note(number)
    array = fileNote.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    fileNote.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    logic = True
    array = fileNote.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет заметок')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = fileNote.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет')
    fileNote.write_file(array, 'a')