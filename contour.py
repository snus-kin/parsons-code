""" Parsons code to contour plot """

import sys

def contour(code):
    if code[0] != "*":
        raise ValueError("Parsons Code must start with '*'")

    contour_dict = {}
    pitch = 0
    index = 0

    maxp = 0
    minp = 0

    contour_dict[(pitch, index)] = "*"

    for point in code:
        if point == "r":
            index += 1
            contour_dict[(pitch, index)] = "-"

            index += 1
            contour_dict[(pitch, index)] = "*"
        elif point == "u":
            index += 1
            pitch -= 1
            contour_dict[(pitch, index)] = "/"

            index += 1
            pitch -= 1
            contour_dict[(pitch, index)] = "*"

            if pitch < maxp:
                maxp = pitch
        elif point == "d":
            index += 1
            pitch += 1
            contour_dict[(pitch, index)] = "\\"

            index += 1
            pitch += 1
            contour_dict[(pitch, index)] = "*"

            if pitch > minp:
                minp = pitch

    for pitch in range(maxp, minp+1):
        line = [" " for _ in range(index + 1)]
        for pos in range(index + 1):
            if (pitch, pos) in contour_dict:
                line[pos] = contour_dict[(pitch, pos)]


        print("".join(line))

if __name__ == "__main__":
    contour(sys.argv[1])
