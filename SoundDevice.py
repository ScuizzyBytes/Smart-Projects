import sounddevice as sd
from scipy.io.wavfile import write

FS = 44100      # Частота дискретизации
SECONDS = 5     # Сколько секунд писать

print("Говори! Идет запись...")
audio = sd.rec(int(SECONDS * FS), samplerate=FS, channels=1, dtype='int16')
sd.wait()  # Ждем, пока допишутся все 5 секунд

write("mic_output.wav", FS, audio)
print("Готово! Сохранено в mic_output.wav")