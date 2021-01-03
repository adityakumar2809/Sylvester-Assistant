import os

def add_note(note):
    f = open('my_note_doc.txt', 'a')
    f.write(f'{note}\n\n')
    f.close()

def open_note():
    os.startfile('my_note_doc.txt')

if __name__ == "__main__":
    add_note('This is an amazing piece of text')
    open_note()
