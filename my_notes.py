def add_note(note):
    f = open('my_note_doc.txt', 'a')
    f.write(f'{note}\n\n')
    f.close()

if __name__ == "__main__":
    add_note('This is an amazing piece of text')
