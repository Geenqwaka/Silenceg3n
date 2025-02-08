import pyaudio
import sys
import threading
import os
from pystray import Icon, MenuItem, Menu
from PIL import Image

# Оптимальные параметры для минимальной нагрузки
RATE = 8000
CHANNELS = 1
FORMAT = pyaudio.paInt8
CHUNK = 4096
silence = b'\x00' * CHUNK

# Фоновый процесс воспроизведения тишины
def play_silence():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    while True:
        stream.write(silence)

# Завершение программы
def exit_program(icon, item):
    icon.stop()
    sys.exit()

# Загрузка встроенной иконки (из exe-файла)
def load_icon():
    icon_path = os.path.join(sys._MEIPASS, "icon.ico") if hasattr(sys, "_MEIPASS") else "icon.ico"
    return Image.open(icon_path)

# Запуск потока для тишины
threading.Thread(target=play_silence, daemon=True).start()

# Создание значка в трее
icon = Icon("silent_sound", load_icon(), menu=Menu(MenuItem("Exit", exit_program)))
icon.run()
