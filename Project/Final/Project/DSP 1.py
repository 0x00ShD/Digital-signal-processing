import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Step 1: Recording the audio
duration = 20 # Duration of the recording in seconds
sample_rate = 44100  # Sample rate (44100 Hz is a common value)

print("Recording audio...")

# Record the audio from the microphone
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()  # Wait for the recording to complete

# Save the recorded audio as a .wav file
output_file = "recorded_audio.wav"
wavfile.write(output_file, sample_rate, audio)

print("Audio saved as", output_file)

# Step 2: Apply FFT and plot magnitude spectrum
audio_data = audio.flatten()  # Flatten the audio to a 1D array

# Compute the Fourier Transform
fft_result = np.fft.fft(audio_data)
magnitude = np.abs(fft_result)

# Generate the frequency axis
frequency_axis = np.fft.fftfreq(len(audio_data), d=1.0/sample_rate)

# Plot the magnitude spectrum
plt.plot(frequency_axis, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Magnitude Spectrum")
plt.show()

# Step 3: Apply inverse FFT and generate original audio
inverse_fft_result = np.fft.ifft(fft_result)
original_audio = np.real(inverse_fft_result)

# Play the original audio
print("Playing original audio...")
sd.play(original_audio, sample_rate)
sd.wait()  # Wait for the audio playback to complete
