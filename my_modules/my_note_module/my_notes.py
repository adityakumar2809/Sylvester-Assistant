import os
import datetime
import pathlib

def addNote(note):
    timestamp = datetime.datetime.now()
    directory_path = pathlib.Path(__file__).parent.absolute()
    f = open(f'{directory_path}\\my_note_doc.txt', 'a')
    f.write(f'[{timestamp}]:\t{note}\n\n')
    f.close()

def openNote():
    directory_path = pathlib.Path(__file__).parent.absolute()
    os.startfile(f'{directory_path}\\my_note_doc.txt')

if __name__ == "__main__":
    addNote('This is an amazing piece of text')
    openNote()
