#!/usr/bin/env python
"""
    Take a midi file and convert it to parsons code, with a limit and offset
"""
import mido
import sys

def midi_to_parsons(midifile, limit=16, offset=0):
    """
        Input: midifile (string) = A midi file path
               limit    (int)    = How long is the parsons code
               offset   (int)    = How many notes in do we start

        Output: parsons (string) = A string containing a parsons code length
                                   limit at an offset from the start of the file
    """
    count = 0
    parsons = ""
    for message in mido.MidiFile(midifile):
        if "note_on" in str(message) and offset == 0:
            if parsons == "":
                # initialise list
                prev = message.note
                parsons += "*"

            # simple comparison
            elif message.note > prev:
                parsons += "u"
                prev = message.note
            elif message.note < prev:
                parsons += "d"
                prev = message.note
            elif message.note == prev:
                parsons += "r"
                prev = message.note

            #increment count
            count += 1
            if count >= limit:
                break
        elif "note_on" in str(message):
            offset -= 1

    return parsons

if __name__ == "__main__":
    print(midi_to_parsons(sys.argv[1]))
