import tensorflow as tf
import numpy as np
import os

# Fungsi untuk membaca data file
def read_file_data(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# Persiapan data
data_directory = '/path/to/data/directory'
file_paths = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if os.path.isfile(os.path.join(data_directory, f))]
labels = [1 if 'important' in f else 0 for f in file_paths]  # Misalkan file yang penting memiliki 'important' dalam namanya

# Baca data file
data = [read_file_data(file_path) for file_path in file_paths]
data = [np.array(d) for d in data]

# Ubah label menjadi numpy array
labels = np.array(labels)

# Inisialisasi model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(len(data[0]),)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Kompilasi model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Pelatihan model
model.fit(data, labels, epochs=10, batch_size=32)

# Simpan model
model.save('important_file_model.h5')