# Audio Processing Project

## Introduction

This project focuses on audio signal processing using Fourier Transform to manipulate audio data in the frequency domain. The transformations include noise removal, speed change, filtering, and reversing the audio signal. The project utilizes Python libraries such as `numpy`, `scipy`, and `matplotlib`.

## Requirements

- Python 3.x
- numpy
- scipy
- matplotlib

Install the required packages using:
```bash
pip install numpy scipy matplotlib
```
## Preprocessing and Filtering
### Noise Removal

Identify noise frequencies using frequency/amplitude and spectrogram plots.
Apply appropriate filters to remove noise.
Generate and save cleanpotc.wav.
### Speed Changes

Double speed and save as fastpotc.wav.
Halve speed and save as slowpotc.wav.
### Reversing Audio

Reverse the cleaned audio and save as revpotc.wav.
### Mixing Audio

Combine all processed audios in the frequency domain and save as mixpotc.wav.
### Visualization
For each audio file, generate and save:

Amplitude vs. Frequency plot
Time-domain signal plot
Spectrogram
## Directory Structure
code/: Contains all the implemented functions and scripts.
newaudio/: Contains the processed audio files and corresponding plots.
## Examples
Cleaned Audio
Audio file: cleanpotc.wav
Spectrogram: cleanpotc_spectogram.png
Time-domain plot: cleanpotc_Data.png
Amplitude plot: cleanpotc_Amplitude.png
## How to Run
Ensure all required packages are installed.
Place the input audio file potc.wav in the audio/ directory.
Run the main processing script to generate processed audio files and plots.
Check the newaudio/ directory for output files.
## Additional Notes
Ensure the input audio is in the correct format.
Adjust filter parameters as needed based on the noise characteristics.
The functions are modular and can be extended for additional processing tasks.
