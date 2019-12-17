"""
    Take a midi file and convert it to parsons code, with a limit and offset
"""
import mido

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
            if message.note > prev:
                parsons += "U"
                prev = message.note
            elif message.note < prev:
                parsons += "D"
                prev = message.note
            elif message.note == prev:
                parsons += "R"
                prev = message.note

            #increment count
            count += 1
            if count >= limit:
                break
        elif "note_on" in str(message):
            offset -= 1

    return parsons

print(midi_to_parsons('./BRAND1.MID', 16, 0))
