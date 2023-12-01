import streamlit as st
import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv('ptbdb_normal.csv')

# Select a row using a widget
row_index = st.slider('Select row index', 0, len(data)-1, 0)
selected_row = data.iloc[row_index]

# Display the selected row
st.write('Selected Row:', selected_row)

# Plot the ECG signal
st.line_chart(selected_row)

# Calculate the heart rate
t_r = np.argmax(selected_row)
freq_cardiaque = 60 * 1000 / (t_r - 0)

# Display heart rate
st.write('Heart Rate:', freq_cardiaque)

# Plot original and processed ECG signals
st.title('Effect of Resampling and Quantization')

# Select an ECG signal using a widget
ecg_signal_index = st.slider('Select ECG signal index', 0, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]

# Resample the ECG signal
ecg_signal_downsampled = scipy.signal.resample(ecg_signal, 100)

# Quantize the ECG signal
ecg_signal_quantized = np.round(ecg_signal * 10) / 10

# Plot original, resampled, and quantized signals
fig, ax = plt.subplots()
ax.plot(ecg_signal, label='Original')
ax.plot(ecg_signal_downsampled, label='Resampled')
ax.plot(ecg_signal_quantized, label='Quantized')
ax.set_title('Effect of Resampling and Quantization')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude (mV)')
ax.legend()

# Display the plot using Streamlit
st.pyplot(fig)


ecg_fft = np.fft.fft(ecg_signal_downsampled)

# Plot FFT
fig, ax = plt.subplots()
ax.set_title('Fourier Transform of Resampled Signal')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude (mV)')
ax.plot(np.abs(ecg_fft))

# Display the plot using Streamlit
st.pyplot(fig)





# Define the window length
window_length = 100

# Calculate the Hanning window
window = np.hanning(window_length)

# Truncate the signal
ecg_truncated = np.multiply(ecg_signal_downsampled, window)

# Calculate the FFT of the truncated signal
ecg_fft = np.fft.fft(ecg_truncated)

# Plot FFT of the truncated signal
fig, ax = plt.subplots()
ax.set_title('Display FFT of the Truncated Signal')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude (mV)')
ax.plot(np.abs(ecg_fft))

# Display the plot using Streamlit
st.pyplot(fig)

# Define the mean and standard deviation of the noise
noise_mean = 0
noise_std = 0.1

# Generate noise
noise = np.random.normal(noise_mean, noise_std, len(ecg_signal))

# Add noise to the signal
noisy_ecg_signal = ecg_signal + noise
st.title('Noisy ECG signal')
# Plot the noisy signal
st.line_chart(noisy_ecg_signal)



# Select a reference signal using a widget
reference_signal_index = st.slider('Select reference signal index', 0, len(data)-1, 0)
reference_signal = data.iloc[reference_signal_index]

# Select another signal for correlation calculation using a widget
signal_index = st.slider('Select signal index for correlation', 0, len(data)-1, 0)
selected_signal = data.iloc[signal_index]

# Calculate correlation
correlation = np.correlate(reference_signal, selected_signal, mode='full')

# Plot the correlation
st.line_chart(correlation)






# Select an ECG signal using a widget
ecg_signal_index = st.slider('Select ECG signal index', 1, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]

# Define the delay
delay = st.slider('Select delay', 0, len(ecg_signal)-1, 10)

# Apply the delay
delayed_ecg_signal = np.roll(ecg_signal, delay)

# Plot the delayed signal
st.line_chart(delayed_ecg_signal)




st.header("Afficher le signal filtré(filtre RIF)")
# Select an ECG signal using a widget
ecg_signal_index = st.slider('Select ECG signal index', 2, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]

# Define the RIF filter taps
filter_taps = [1, 0, 0, 0]

# Apply the filter
filtered_ecg_signal = np.convolve(ecg_signal, filter_taps, mode='same')

# Plot the filtered signal
st.line_chart(filtered_ecg_signal)


st.header("Afficher le signal filtré(filtre RII)")
ecg_signal_index = st.slider('Select ECG signal index', 3, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]

# Define the RII filter taps
filter_taps = [0.1, 0.2, 0.3, 0.2, 0.1]  # Modify filter taps as needed

# Apply the filter
filtered_ecg_signal = np.convolve(ecg_signal, filter_taps, mode='same')

# Plot the filtered signal
st.line_chart(filtered_ecg_signal)