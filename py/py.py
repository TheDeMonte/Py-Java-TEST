import json
import datetime

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, default=str, indent=4)

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "created_at": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Сообщение: {note['message']}")
        print(f"Дата создания: {note['created_at']}")
        print()

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")

def filter_by_date(date_str):
    notes = load_notes()
    filtered_notes = [note for note in notes if note['created_at'].split(' ')[0] == date_str]
    return filtered_notes

def getnoteid(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

while True:
    command = input("Введите команду (add, read, delete, filter, id): ")
    
    if command == "add":
        title = input("Введите заголовок заметки: ")
        message = input("Введите тело заметки: ")
        add_note(title, message)
        
    elif command == "read":
        read_notes()
        
    elif command == "delete":
        note_id = int(input("Введите ID заметки для удаления: "))
        delete_note(note_id)
        
    elif command == "filter":
        date_input = input("Введите дату для фильтрации (гггг-мм-дд): ")
        filtered_notes = filter_by_date(date_input)
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Сообщение: {note['message']}")
            print(f"Дата создания: {note['created_at']}")
            print()

    elif command == "id":
        note_id = int(input("Введите ID заметки для просмотра заметки: "))
        note = getnoteid(note_id)
        if note:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Сообщение: {note['message']}")
            print(f"Дата создания: {note['created_at']}")
        else:
            print("Заметка с указанным ID не найдена.")        
    else:
        print("Неверная команда. Повторите попытку.")
