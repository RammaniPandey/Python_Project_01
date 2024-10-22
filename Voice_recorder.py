import sounddevice as sd
from scipy.io.wavfile import write

# Sampling frequency
freq = 44100

# Duration in seconds
dur = 15

# Record audio with 1 channel (mono)
print("Recording...")
recording = sd.rec(int(dur * freq), samplerate=freq, channels=1)
sd.wait()  # Wait until recording is finished
print("Recording finished!")

# Save as WAV file
write("Recording.wav", freq, recording)
