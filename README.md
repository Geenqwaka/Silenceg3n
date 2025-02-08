# Silenceg3n

![icon](icon.png)

Simple python program to solve problem with noisy when idle speakers (Windows 10-11)

The problem that Silenceg3n fixes - is that the speakers connected to the PC make terrible noises when idle, but when any sound is turned on (a song, a movie, any audio file), the noises completely disappear. But as soon as you turn off the audio file, the noises return again. Program just endlessly generates silence through your device's audio output for fix that issue. It supports tray control, consuming minimal system resources.

## Installation

### Requirements:
- **Windows 10/11** (other operating systems are not supported).
- Python 3.x
- Dependencies:
  - `pyaudio`
  - `pystray`
  - `Pillow`

### Install dependencies:
```bash
pip install pyaudio pystray pillow
```

## Usage

Running the Executable from Releases:

    Download the precompiled silenceg3n.exe from the Releases section of this repository.
    Simply double-click the .exe file to run the program. No installation required!

1. Once launched, the program will run in the background, generating silence through your device's audio output.
2. To control the program, use the tray icon:
   - **"Exit"** — Exits the program.

---

## License

This project is licensed under the MIT License.

