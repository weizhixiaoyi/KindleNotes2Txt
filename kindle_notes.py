# -*- coding:utf-8 -*-
import os

"""read My Clippings.txt"""
kindle_notes_file_path = "My Clippings.txt"
notes_list = []
current_note = []
with open(kindle_notes_file_path, 'r') as f:
    line = f.readline().strip('\n').replace("\ufeff", "")
    while line:
        if "=========" in line:
            if len(current_note) == 3:
                notes_list.append(current_note)
            current_note = []
        else:
            line = line.strip('\n').replace("\ufeff", "")
            if line:
                current_note.append(line)
        line = f.readline()

notes_dict = {}
for note in notes_list:
    book_name = note[0]
    note_info = note[1]
    note = note[2]
    if book_name in notes_dict.keys():
        notes_dict[book_name].append([note, note_info])
    else:
        notes_dict[book_name] = []
        notes_dict[book_name].append([note, note_info])

"""write book notes"""
book_notes_file = "book_notes"
if not os.path.exists(book_notes_file):
    os.mkdir(book_notes_file)
for book_name in notes_dict.keys():
    book_notes_file_path = book_notes_file + "/" + book_name + '.txt'
    with open(book_notes_file_path, 'w') as f:
        for i, value in enumerate(notes_dict[book_name]):
            note = value[0]
            f.write("[" + str(i + 1) + "]: " + note + '\n' * 2)
        f.write("\n")
        for i, value in enumerate(notes_dict[book_name]):
            note_info = value[1].replace("您在", "").replace("的标注", "")
            f.write("[" + str(i + 1) + "] " + note_info + '\n')