# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_randrum.ipynb.

# %% auto 0
__all__ = ['midi_note_to_drum_name', 'drum_name_to_note', 'drum_names', 'feet', 'hands', 'foo', 'drum_cleaner', 'DrumBeat']

# %% ../nbs/01_randrum.ipynb 3
def foo(): pass

# %% ../nbs/01_randrum.ipynb 5
midi_note_to_drum_name = {
    35: "KickL",
    36: "KickR",
    37: "SnareRest",
    38: "Snare",
    41: "Tom4",
    42: "HihatClosed",
    45: "Tom3",
    46: "HihatOpen",
    47: "Tom2",
    48: "Tom1",
    49: "CrashL",
    51: "RideR",
    52: "China",
    53: "RideRBell",
    55: "RideLBell",
    57: "CrashR",
    59: "RideL",
}

drum_name_to_note = {v: k for k, v in midi_note_to_drum_name.items()}

drum_names = list(drum_name_to_note.keys())
feet = ['KickL', 'KickR']
hands = ['SnareRest', 'Snare', 'Tom4', 'HihatClosed', 'Tom3', 'HihatOpen', 'Tom2', 'Tom1', 'CrashL', 'RideR', 'China', 'RideRBell', 'RideLBell', 'CrashR', 'RideL']


def drum_cleaner(drum_notes):
    # TODO
    # check that we do not have overlapping kicks
    # check that L and R kick alternate
    # make sure we do not have 3 hand drums playing at the same time
    cleaned_drum_notes = drum_notes
    return cleaned_drum_notes

# %% ../nbs/01_randrum.ipynb 6
import pretty_midi
import random

class DrumBeat:
    def __init__(self) -> None:
        self.song = pretty_midi.PrettyMIDI()
        self.drums = pretty_midi.Instrument(program=0)

    def create_random_line(self, beat_length, drum_group, song_length=10, play_prob=0.4):
        num_beats = int(song_length // beat_length)
        for i in range(num_beats):
            play = random.uniform(0, 1) < play_prob
            if play:
                drum_to_play = random.choice(drum_group)
                pitch = drum_name_to_note[drum_to_play]
                start = i * beat_length
                end = start + beat_length
                note = pretty_midi.Note(start=start, end=end, velocity=80, pitch=pitch)
                self.drums.notes.append(note)

    def create_random_song(self):
        self.create_random_line(0.25, feet, play_prob=.75)
        self.create_random_line(0.25, hands)
        self.create_random_line(0.25, hands)
        self.song.instruments.append(self.drums)
        self.song.write("beats/rand-drum-beat.mid")
