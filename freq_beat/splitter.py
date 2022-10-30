# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_notesplitter.ipynb.

# %% auto 0
__all__ = ['split_note']

# %% ../nbs/03_notesplitter.ipynb 3
from pretty_midi import Note
from .manager import copy_note
    
def split_note(note: Note, num_pieces):
    start = note.start
    pitch = note.pitch
    velocity = note.velocity
    note_length = note.duration
    piece_length = note_length / num_pieces
    start_times = map(lambda x: start + x * piece_length, range(num_pieces))
    return [copy_note(note, start=piece_start, end=piece_start + piece_length) for piece_start in start_times]