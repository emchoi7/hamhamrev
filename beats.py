import librosa
import sys

filename = 'humble.mp3'
#load humble
y, sr = librosa.load(filename)

#get beats
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#print
print(beat_times)
librosa.output.times_csv('beat_times.csv', beat_times)