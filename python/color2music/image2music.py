import cv2
import glob
import os
import numpy as np
import pretty_midi

def calcRGB(img_array):
    average_color_per_row = np.average(img_array, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    return average_color

def makeNote(note, startTime, endTime):
    note = pretty_midi.Note(velocity=100, pitch=note, start=startTime, end=endTime)
    return note

def makeChord(base):
    majorCordList = [0, 2, 4, 5, 7, 9, 11]

    chordList = []
    for a in range(0,3):
        listNum= base + a * 2
        chordList.append(60 + majorCordList[listNum])

    return chordList

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

        majorCordList = [0, 2, 4, 5, 7, 9, 11]

        noteTime = 0
        for a in range(0,5):
            chordList = makeChord(np.random.randint(0,3))

            instrument.notes.append(makeNote(chordList[0], noteTime, noteTime+1))
            instrument.notes.append(makeNote(chordList[1], noteTime, noteTime+1))
            instrument.notes.append(makeNote(chordList[2], noteTime, noteTime+1))
            pm.instruments.append(instrument)
            noteTime = noteTime +1

        pm.write('output/' + filename + '.mid')
        # audio_data = pm.fluidsynth()
        # music_max = np.max(np.abs(audio_data))
        # muisc_array = (audio_data/music_max).astype(np.float32)
        # wav_file_name = 'test.wav'
        # wavfile.write(wav_file_name,44100, muisc_array)



if __name__ == '__main__':
    main()
