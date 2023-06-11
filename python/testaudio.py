import pyaudio as pa
import numpy as np
import wave


p = pa.PyAudio()


freq = 440
duration = 1
t = np.linspace(0, duration, 44100)
note = np.sin(2*np.pi*freq*t)
note = note.astype(np.float32).tobytes()


stream = p.open(format=pa.paFloat32,
                channels=1,
                rate=44100,
                frames_per_buffer=1024,
                output=True,
                )
stream.write(note)
stream.stop_stream()
stream.close()
p.terminate()