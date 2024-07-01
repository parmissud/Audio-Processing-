import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq, irfft
from scipy.signal import resample

def read_voice(path):
    rate, data = wavfile.read(path)
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    amplitude = rfft(data)
    frequency = rfftfreq(len(data), 1 / rate)
    return rate, data,amplitude,frequency


def change_voice_speed(data, rate, speed_factor):
    new_rate = int(rate * speed_factor)
    new_data = resample(data, int(len(data) / speed_factor))
    return new_data, new_rate

def low_pass_filter(frequency, amplitude, cutoff_freq):
    filtered_amplitude = np.where(frequency > cutoff_freq, 0, amplitude)
    return filtered_amplitude

def reverse_voice(data):
    return data[::-1]

def mix_voices(data_list, rate_list):
    min_length = min(map(len, data_list))
    mixed_data = sum(data[:min_length] for data in data_list) / len(data_list)
    return mixed_data, rate_list[0]  

def write_voice(data, rate, path):
    wavfile.write(path, rate, data.astype(np.int16))

def remove_noise(data, rate, noise_threshold):
    amplitude = rfft(data)
    frequency = rfftfreq(len(data), 1 / rate)
    # حذف نویز بر اساس آستانه
    cleaned_amplitude = np.where(np.abs(amplitude) < noise_threshold, 0, amplitude)
    cleaned_data = irfft(cleaned_amplitude)
    return cleaned_data

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def plot_frequency_amplitude(amplitudeAbs,frequency, title, save_path):
    plt.plot(frequency,amplitudeAbs)
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    ensure_dir(save_path)
    plt.savefig(save_path)
    plt.close()
    plt.close()
    
def plot_spectrogram(rate, data, title, save_path):
    plt.figure(figsize=(10, 6))
    plt.specgram(data, Fs=rate, NFFT=1024, noverlap=512)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    ensure_dir(save_path)
    plt.savefig(save_path)
    plt.close()

def write_audio(file_path, rate, data):
    ensure_dir(file_path)
    wavfile.write(file_path, rate, data.astype(np.int16))

# paths
input_file = r'potc.wav'
cleaned_file = r'newaudio/cleanpotc.wav'
fast_file = r'newaudio/fastpotc.wav'
slow_file = r'newaudio/slowpotc.wav'
reverse_file = r'newaudio/revpotc.wav'

# Reading the audio file
rate, data,amplitude,frequency = read_voice(input_file)

# رسم نمودارهای اولیه
plot_frequency_amplitude(rate, data, "Original Audio Frequency/Amplitude", r'newaudio/original_frequency_amplitude.png')
plot_spectrogram(rate, data, 'Original Audio Spectrogram', r'newaudio/original_spectrogram.png')

# حذف نویز
noise_threshold = 1e8  # این مقدار باید بر اساس نمودار Frequency/Amplitude تنظیم شود
cleaned_data = remove_noise(data, rate, noise_threshold)
write_audio(cleaned_file, rate, cleaned_data)

# رسم نمودارهای صوت بدون نویز
plot_frequency_amplitude(rate, cleaned_data, 'Cleaned Audio Frequency/Amplitude', r'newaudio/cleanpotc_frequency_amplitude.png')
plot_spectrogram(rate, cleaned_data, 'Cleaned Audio Spectrogram', r'newaudio/cleanpotc_spectrogram.png')

# تغییر سرعت صوت
def change_speed(data, rate, factor):
    new_rate = int(rate * factor)
    new_data = resample(data, int(len(data) / factor))
    return new_data, new_rate

# سرعت دو برابر
fast_data, fast_rate = change_speed(cleaned_data, rate, 2)
write_audio(fast_file, fast_rate, fast_data)

# سرعت نصف
slow_data, slow_rate = change_speed(cleaned_data, rate, 0.5)
write_audio(slow_file, slow_rate, slow_data)

# معکوس کردن صوت
reverse_data = cleaned_data[::-1]
write_audio(reverse_file, rate, reverse_data)

# رسم نمودارهای صوت‌های تغییر یافته
plot_frequency_amplitude(fast_rate, fast_data, 'Fast Audio Frequency/Amplitude', r'newaudio/fastpotc_frequency_amplitude.png')
plot_spectrogram(fast_rate, fast_data, 'Fast Audio Spectrogram', r'newaudio/fastpotc_spectrogram.png')

plot_frequency_amplitude(slow_rate, slow_data, 'Slow Audio Frequency/Amplitude', r'newaudio/slowpotc_frequency_amplitude.png')
plot_spectrogram(slow_rate, slow_data, 'Slow Audio Spectrogram', r'newaudio/slowpotc_spectrogram.png')

plot_frequency_amplitude(rate, reverse_data, 'Reversed Audio Frequency/Amplitude', r'newaudio/revpotc_frequency_amplitude.png')
plot_spectrogram(rate, reverse_data, 'Reversed Audio Spectrogram', r'newaudio/revpotc_spectrogram.png')



# ترکیب صوت‌ها
mixed_data = mix_audios([cleaned_data, fast_data[:len(cleaned_data)], slow_data[:len(cleaned_data)], reverse_data[:len(cleaned_data)]], rate)
write_audio('newaudio/mixpotc.wav', rate, mixed_data)

# رسم نمودارهای صوت ترکیبی
plot_frequency_amplitude(rate, mixed_data, 'Mixed Audio Frequency/Amplitude', r'newaudio/mixpotc_frequency_amplitude.png')
plot_spectrogram(rate, mixed_data, 'Mixed Audio Spectrogram', r'newaudio/mixpotc_spectrogram.png')