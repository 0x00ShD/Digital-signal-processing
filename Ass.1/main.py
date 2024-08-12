import scipy.signal as signal
import numpy as np
from pydub import AudioSegment
import os

# Load the audio file
audio = AudioSegment.from_file('audio_file.mp3')
rate = audio.frame_rate
data = np.array(audio.get_array_of_samples())

# Define the high-pass filter
cutoff_freq = 500 # Hz
nyquist_freq = 0.5*rate
order = 5
b, a = signal.butter(order, cutoff_freq/nyquist_freq, btype='lowpass')

# Apply the filter to the audio data
filtered_data = signal.filtfilt(b, a, data)

# Normalize the filtered data to the same range as the original data
max_amp = np.max(np.abs(data))
filtered_data = np.int16(filtered_data / np.max(np.abs(filtered_data)) * max_amp)

# Save the filtered data to a temporary WAV file
temp_file = 'temp_audio.wav'
audio = AudioSegment(
    data=filtered_data.tobytes(),
    sample_width=filtered_data.dtype.itemsize,
    frame_rate=rate,
    channels=1
)
audio.export(temp_file, format='wav')

# Load the temporary WAV file and convert it to an MP3 file
audio = AudioSegment.from_wav(temp_file)
audio.export('output_audio.mp3', format='mp3')

# Delete the temporary WAV file
os.remove(temp_file)
