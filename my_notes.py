import os
import datetime

def addNote(note):
    timestamp = datetime.datetime.now()
    f = open('my_note_doc.txt', 'a')
    f.write(f'[{timestamp}]:\t{note}\n\n')
    f.close()

def openNote():
    os.startfile('my_note_doc.txt')

if __name__ == "__main__":
    addNote('This is an amazing piece of text')
    openNote()
