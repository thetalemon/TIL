import cv2
import glob
import os
import numpy as np
import csv
import pretty_midi

def calcRGB(img_array):
    average_color_per_row = np.average(img_array, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    return average_color

def makeNote(note, startTime, endTime):
    note_number = pretty_midi.note_name_to_number(note)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=startTime, end=endTime)
    return note

def main():
    files = glob.glob("./images/*")

    f = open('./output/RGB.csv', 'w')
    csvWriter = csv.writer(f)

    for fname in files:
        filename = os.path.basename(fname)
        bgr = cv2.imread(fname, -1)
        average_color = calcRGB(bgr)
        listData = []
        listData.append(filename)
        for element in average_color :
            listData.append(element)
        print(listData)

        csvWriter.writerow(listData)

        pm = pretty_midi.PrettyMIDI(resolution=960, initial_tempo=120)
        instrument = pretty_midi.Instrument(0)

        argsList = ["C", "D", "E", "F", "G", "A", "B"]

        for item in argsList :

            notelist = []
            noteName = item + '4'
            print(noteName),
            notelist.append(noteName)

        noteTime = 0
        for item in notelist:
            instrument.notes.append(makeNote(item, noteTime, noteTime+1))
            pm.instruments.append(instrument)
            noteTime = noteTime +1

        pm.write('output/' + filename + '.mid')



if __name__ == '__main__':
    main()
