# This is a sample Python script.

# This python script generates 4-bar melodies in a randomly-chosen major key.
# The number of notes to go on the melody is chosen at random,
# and the duration and pitch of that note is also chosen at random.

# MIDIUtil library wasn't made by me, all credits for library go to its creator.

from midiutil import MIDIFile
import random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
# Only use the default track and channel:
track = 0
channel = 0
volume = 100  # 0-127, as per the MIDI standard
time = 0  # In beats
duration = 1  # In beats
tempo = 120  # In BPM

# Randomly generate a key for the melody:
key = random.randrange(0, 11)


# Set the list of degrees equal to their respective values in the chosen key:
for degree in degrees:
    degree = degree + key

# Create the MIDIFile and set the tempo:
MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track, time, tempo)

# TO DO: Randomly generate pitches for every note you will add to the file:
for degree in degrees:
    pitch = random.choice(degrees)
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("major-scale-melody2.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)


