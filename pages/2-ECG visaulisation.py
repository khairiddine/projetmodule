import streamlit as st
import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt



custom_css = """
    <style>
[data-testid="stAppViewContainer"]{
background-color: 'white';

}
[data-testid="stSidebar"]{
  background-image: linear-gradient(to bottom right, green, white);


}
       
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
# Read the CSV file into a DataFrame
data = pd.read_csv('ptbdb_normal.csv')

# Select a row using a widget
st.header('CHOISSISEZ UN  SIGNIAL DE CLIENT: ')
row_index = st.slider('', 0, len(data)-1, 0)
selected_row = data.iloc[row_index]

# Display the selected row
st.write(':green[ Le signial de client selectionné:]', selected_row)
st.header('LE CODE :')
st.code("row_index = st.slider('', 0, len(data)-1, 0) ")
st.code('selected_row = data.iloc[row_index] ')
st.code('st.line_chart(selected_row)')
st.header('Le signial originale ')
# Plot the ECG signal
st.line_chart(selected_row)

# Calculate the heart rate
t_r = np.argmax(selected_row)
freq_cardiaque = 60 * 1000 / (t_r - 0)

# Display heart rate
st.write('Heart Rate:', freq_cardiaque)





# Plot original and processed ECG signals
st.title('Effet du rééchantillonnage et de la quantification')
st.header("Définition:")

st.markdown(
    """
L'échantillonnage consiste à transformer un signal continu en un signal discret. La quantification consiste à convertir un signal discret en un signal numérique.
Le graphique qui sera généré montrera que le signal ECG reéchantillonné a une fréquence d'échantillonnage plus faible que le signal ECG original.
Le signal ECG quantifié a une amplitude plus faible que le signal ECG original.
Vous pouvez modifier le code pour tester différents paramètres d'échantillonnage et de quantification. 
Par exemple, vous pouvez essayer de reéchantillonner le signal ECG à une fréquence d'échantillonnage plus élevée ou de quantifier le signal ECG avec une résolution plus élevée.

""",
)

# Select an ECG signal using a widget
st.write(':green[choisir un signial ECG:] ')
ecg_signal_index = st.slider('', 4, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]

# Resample the ECG signal
ecg_signal_downsampled = scipy.signal.resample(ecg_signal, 100)

# Quantize the ECG signal
ecg_signal_quantized = np.round(ecg_signal * 10) / 10

# Plot original, resampled, and quantized signals
fig, ax = plt.subplots()
ax.plot(ecg_signal, label='Original')
ax.plot(ecg_signal_downsampled, label='rééchantillonnée')
ax.plot(ecg_signal_quantized, label='Quantifié')
ax.set_title('Effet du rééchantillonnage et de la quantification')
ax.set_xlabel('Temps(s)')
ax.set_ylabel('Amplitude (mV)')
ax.legend()
st.header('LE CODE :')
st.code('ecg_signal_downsampled = scipy.signal.resample(ecg_signal, 100)')
st.code('ecg_signal_quantized = np.round(ecg_signal * 10) / 10')
st.code("plt.plot(ecg_signal, label='Original')")
st.code("plt.plot(ecg_signal_downsampled, label='Reéchantillonné')")
st.code(" plt.plot(ecg_signal_quantized, label='Quantifié')")
st.code('st.pyplot(fig)')
# Display the plot using Streamlit
st.pyplot(fig)



ecg_fft = np.fft.fft(ecg_signal_downsampled)

# Plot FFT
fig, ax = plt.subplots()
ax.set_title('Transformée de Fourier du signal rééchantillonné')
st.markdown(""" Si vous effectuez la FFT sur le signal original temporel, vous obtiendrez une représentation du signal
             dans le domaine fréquentiel. La FFT vous donnera la puissance du signal à différentes fréquences.""")
st.header('LE CODE :')
st.code('ecg_fft = np.fft.fft(ecg_signal_downsampled)')
st.code("ax.plot(np.abs(ecg_fft))")
ax.set_xlabel('Frequence(Hz)')

ax.set_ylabel('Amplitude (mV)')
ax.plot(np.abs(ecg_fft))

# Display the plot using Streamlit
st.pyplot(fig)


st.header("L'effet de tranquage")
st.markdown(""" L'effet du troncage sur un signal échantillonné est de réduire la longueur du signal. Cela peut avoir un impact sur la qualité du signal, en particulier si le troncage est important.
Lorsque le signal est tronqué, les échantillons qui sont au-delà de la longueur de la fenêtre sont supprimés. Cela peut entraîner une perte d'information, car ces échantillons peuvent contenir des informations importantes sur le signal.
L'effet du troncage sur la qualité du signal dépend de la longueur de la fenêtre et de la nature du signal. En général, plus la fenêtre est longue, moins la perte d'information est importante. L'analyse d'un signal ECG : le troncage peut entraîner une perte de précision dans la mesure de la fréquence cardiaque""")
st.header('LE CODE :')
st.write('definir la longeur de fenetre:')
st.code('window_length = 100')
st.write('Calculer la fenêtre de Hanning:')
st.code('window = np.hanning(window_length)')
st.write('Tronquer le signal:')
st.code('ecg_truncated = np.multiply(ecg_signal_downsampled, window)')
st.write('Calculer la FFT du signal tronqué:')
st.code('ecg_fft = np.fft.fft(ecg_truncated)')
st.write('Tracer la FFT du signal tronqué:')
st.code('ax.plot(np.abs(ecg_fft))')
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
ax.set_title('Afficher la FFT du signal tronqué')
ax.set_xlabel('Frequence (Hz)')
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
st.title('Signal ECG bruyant')
st.header('LE CODE :')
st.code('noise_mean = 0 ,noise_std = 0.1')
st.code('noise = np.random.normal(noise_mean, noise_std, len(ecg_signal))')
st.code('noisy_ecg_signal = ecg_signal + noise')
st.code('st.line_chart(noisy_ecg_signal)')
# Plot the noisy signal
st.line_chart(noisy_ecg_signal)


st.title('La corrélation:')
# Select a reference signal using a widget
reference_signal_index = st.slider("Sélectionner l'index du signal de référence", 0, len(data)-1, 0)
reference_signal = data.iloc[reference_signal_index]

# Select another signal for correlation calculation using a widget
signal_index = st.slider("Sélectionnez l'indice de signal pour la corrélation", 0, len(data)-1, 0)
selected_signal = data.iloc[signal_index]

# Calculate correlation
correlation = np.correlate(reference_signal, selected_signal, mode='full')
st.header('LE CODE :')
st.code('reference_signal = data.iloc[reference_signal_index]')
st.code('selected_signal = data.iloc[signal_index]')
st.code("correlation = np.correlate(reference_signal, selected_signal, mode='full')")
st.code('st.line_chart(correlation)')
# Plot the correlation
st.table(correlation[200:250])
st.line_chart(correlation)


st.header('LE RAETAR')
# Select an ECG signal using a widget
ecg_signal_index = st.slider("Sélectionner l'index du signal de référence", 1, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]

# Define the delay
delay = st.slider('Sélectionnez le délai', 0, len(ecg_signal)-1, 10)

# Apply the delay
delayed_ecg_signal = np.roll(ecg_signal, delay)
st.subheader('Le code:')
st.write('Définir le retard:')
st.code("delay = st.slider('Sélectionnez le délai', 0, len(ecg_signal)-1, 10)")
st.write('Appliquer le retard/')
st.code('delayed_ecg_signal = np.roll(ecg_signal, delay)')
st.write('Tracer le signial retardé:')
st.code('st.line_chart(delayed_ecg_signal)')
# Plot the delayed signal
st.line_chart(delayed_ecg_signal)




st.header("Afficher le signal filtré(filtre RIF)")
st.subheader('Définition de filtre RIF:')
st.markdown(""" Un filtre RIF (réponse impulsionnelle finie) est un filtre numérique qui utilise une réponse impulsionnelle finie. La réponse impulsionnelle d'un filtre est la sortie du filtre lorsque l'entrée est un signal delta.
Pour appliquer un filtre RIF à un signal, vous pouvez utiliser la fonction np.convolve(). La fonction np.convolve() renvoie le produit de convolution entre deux signaux.""")
# Select an ECG signal using a widget
ecg_signal_index = st.slider("Sélectionnez l'indice du signal ECG", 2, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]
st.subheader('Le code:')
st.code('filter_taps = [1, 0, 0, 0]')
st.code("filtered_ecg_signal = np.convolve(ecg_signal, filter_taps, mode='same')")
st.code("st.line_chart(filtered_ecg_signal)")
# Define the RIF filter taps
filter_taps = [1, 0, 0, 0]

# Apply the filter
filtered_ecg_signal = np.convolve(ecg_signal, filter_taps, mode='same')

# Plot the filtered signal
st.line_chart(filtered_ecg_signal)


st.header("Afficher le signal filtré(filtre RII)")
st.subheader('Définition du filtre RII')
st.markdown(""" Un filtre RII (réponse impulsionnelle infinie) est un filtre numérique qui utilise une réponse impulsionnelle infinie. La réponse impulsionnelle d'un filtre est la sortie du filtre lorsque l'entrée est un signal delta.
Pour appliquer un filtre RII à un signal, vous pouvez utiliser la fonction scipy.signal.lfilter(). La fonction scipy.signal.lfilter() renvoie la sortie d'un filtre numérique avec une réponse impulsionnelle infinie. """)
ecg_signal_index = st.slider("Sélectionnez l'indice du signal ECG", 3, len(data)-1, 0)
ecg_signal = data.iloc[ecg_signal_index]
st.subheader('Le code:')
st.code('filter_taps = [0.1, 0.2, 0.3, 0.2, 0.1] ')
st.code("filtered_ecg_signal = np.convolve(ecg_signal, filter_taps, mode='same')")
st.code('st.line_chart(filtered_ecg_signal)')

# Define the RII filter taps
filter_taps = [0.1, 0.2, 0.3, 0.2, 0.1]  # Modify filter taps as needed

# Apply the filter
filtered_ecg_signal = np.convolve(ecg_signal, filter_taps, mode='same')

# Plot the filtered signal
st.line_chart(filtered_ecg_signal)