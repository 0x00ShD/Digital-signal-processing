import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Step 1: Recording the audio
duration = 1  # Duration of the recording in seconds
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
frequency_axis = np.fft.fftfreq(len(audio_data), d=1.0 / sample_rate)

# Create a figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

# Plot the magnitude spectrum in the first subplot
ax1.plot(frequency_axis, magnitude)
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude")
ax1.set_title("Magnitude Spectrum")

# Plot the original audio signal in the second subplot
time_axis = np.linspace(0, duration, len(audio_data))
ax2.plot(time_axis, audio_data)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Amplitude")
ax2.set_title("Original Audio Signal")

# Apply inverse FFT and generate the IFFT signal
inverse_fft_result = np.fft.ifft(fft_result)
ifft_signal = np.real(inverse_fft_result)

# Plot the IFFT signal in the third subplot
ax3.plot(time_axis, ifft_signal)
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Amplitude")
ax3.set_title("IFFT Signal")

# Adjust spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()

# Step 3: Play the original audio
print("Playing original audio...")
sd.play(audio_data, sample_rate)
sd.wait()  # Wait for the audio playback to complete
