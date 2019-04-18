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
    endTime = startTime + noteLong
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
        termLong = 4
        noteLong = 1
        noteNumber = 0
        updownFlag = np.random.randint(0,2)
        for terms in range(0,12):
            baseNote = 7+np.random.randint(0,7)
            ## set base notes
            for chords in range(0,7,2):
                instrument.notes.append(makeNote(noteList[baseNote+chords], noteTime, termLong, 75))
            randomNumber = np.random.randint(0,5)*2 - 4
            firstNoteNumber = 7*4 + baseNote + randomNumber

            ## 最初の小節でないなら
            if terms != 0:
                ## 前小節の最後の音と、今小節の最初の音の差を、6以下に制限する
                while (noteNumber - firstNoteNumber) > 6:
                    ## 音の範囲が狭いと、6以下にできないときがあるため、ランダムの範囲を広げる
                    randomNumber = np.random.randint(0,7)*2 - 4
                    firstNoteNumber = 7*4 + baseNote + randomNumber

            instrument.notes.append(makeNote(noteList[firstNoteNumber], noteTime, noteLong, 100))
            continusCount = 0
            for a in range(1,4):
                ## 前の音が低い・高い音なら、音を上げ・下げておく
                if   noteNumber > 35 : noteNumber = noteNumber  - 10
                elif noteNumber < 23 : noteNumber = noteNumber + 10

                randomNumber = np.random.randint(0,4)*2

                ## 前の音と同じなら連続カウントを１上げる。
                ## 連続カウントが１以上なら、変化なし以外で再度差分を求める。
                if randomNumber == 0 and continusCount < 1 : continusCount = continusCount+1
                else : randomNumber = np.random.randint(1,4)*2

                ## 上げ下げフラグが１なら、差分値の正負を反転
                if updownFlag == 1 : randomNumber = randomNumber * -1
                noteNumber = firstNoteNumber + randomNumber

                # print("listsize:",len(noteList))
                print(randomNumber,",",noteNumber)
                instrument.notes.append(makeNote(noteList[noteNumber], noteTime + a, noteLong, 100))
                pm.instruments.append(instrument)

            updownFlag = np.random.randint(0,2)
            pm.instruments.append(instrument)
            noteTime = noteTime + termLong

        pm.write('output/' + filename + '.mid')

if __name__ == '__main__':
    main()
