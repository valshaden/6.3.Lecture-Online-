import sounddevice as sd
from scipy.io.wavfile import write, read
import numpy as np

sample_rate = 44100  # Частота дискретизации (Гц)
duration = 5         # Длительность записи (секунды)

print("Запись началась... Говорите!")


recording = sd.rec(
    int(duration * sample_rate),  # Общее количество сэмплов
    samplerate=sample_rate,
    channels=1,                   # 1 канал (моно), 2 - стерео
    dtype=np.int16                # Тип данных для сэмплов
)

sd.wait()
print("Запись завершена!")

filename = "my_recording.wav"
write(filename, sample_rate, recording)

print(f"Файл сохранен как {filename}")

