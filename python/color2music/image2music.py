import cv2
import glob
import os
import numpy as np
import pretty_midi

def calcRGB(img_array):
    average_color_per_row = np.average(img_array, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    return average_color

def makeNote(note, startTime, noteLong, velocity):
    endTime =  startTime + noteLong
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=startTime, end=endTime)
    return note

def makeAllChordList(chord):
    allChordList = []
    majorChordSubList = [0, 2, 4, 5, 7, 9, 11]
    for octave in range(2,10) :
        for sub in majorChordSubList :
            allChordList.append(octave*12 + sub + chord)

    return allChordList

def main():
    files = glob.glob("./images/*")

    for fname in files:
        # read image
        filename = os.path.basename(fname)
        bgr = cv2.imread(fname, -1)
        average_color = calcRGB(bgr)

        # initial define about music
        pm = pretty_midi.PrettyMIDI(resolution=960, initial_tempo=120)
        instrument = pretty_midi.Instrument(0)

        noteList = makeAllChordList(0);

        noteTime = 0
        updownFlag = np.random.randint(0,2)
        termLong = 4
        noteLong = 1
        noteNumber = 0
        for a in range(0,12):
            baseNote = np.random.randint(0,7)
            instrument.notes.append(makeNote(noteList[7+baseNote], noteTime, termLong, 75))
            instrument.notes.append(makeNote(noteList[7+baseNote+2], noteTime, termLong, 75))
            instrument.notes.append(makeNote(noteList[7+baseNote+4], noteTime, termLong, 75))

            randomNumber = np.random.randint(0,5)*2 - 4
            firstNoteNumber = 7*4 + baseNote + randomNumber

            if noteNumber!=0:
                while (noteNumber-firstNoteNumber) > 6:
                    randomNumber = np.random.randint(0,10)*2 - 4
                    firstNoteNumber = 7*4 + baseNote + randomNumber

            instrument.notes.append(makeNote(noteList[firstNoteNumber], noteTime, noteLong, 100))

            continusCount = 0
            for a in range(1,4):
                if noteNumber > 35 : noteNumber = noteNumber  - 10
                elif noteNumber < 23 : noteNumber = noteNumber + 10

                randomNumber = np.random.randint(0,4)*2
                if continusCount<1 : continusCount = continusCount+1
                else :
                    randomNumber = np.random.randint(1,4)*2

                if updownFlag==1 : randomNumber = randomNumber * -1
                noteNumber = firstNoteNumber + randomNumber

                # print("listsize:",len(noteList))
                print(noteNumber)
                instrument.notes.append(makeNote(noteList[noteNumber], noteTime + a, noteLong, 100))
                pm.instruments.append(instrument)

            updownFlag = np.random.randint(0,2)
            pm.instruments.append(instrument)
            noteTime = noteTime + termLong

        pm.write('output/' + filename + '.mid')

if __name__ == '__main__':
    main()
