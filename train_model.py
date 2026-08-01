import os
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# -----------------------------
# Create model folder
# -----------------------------
os.makedirs("model", exist_ok=True)

# -----------------------------
# Load datasets
# -----------------------------
train = pd.read_csv("datasets/sign_mnist_train.csv")
test = pd.read_csv("datasets/sign_mnist_test.csv")

# -----------------------------
# Split features and labels
# -----------------------------
X_train = train.drop("label", axis=1).values
y_train = train["label"].values

X_test = test.drop("label", axis=1).values
y_test = test["label"].values

# -----------------------------
# Normalize pixel values
# -----------------------------
X_train = X_train / 255.0
X_test = X_test / 255.0

# -----------------------------
# Reshape into images
# -----------------------------
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# -----------------------------
# Remap labels to consecutive values
# -----------------------------
unique_labels = sorted(np.unique(y_train))

label_map = {label: index for index, label in enumerate(unique_labels)}

y_train = np.array([label_map[label] for label in y_train])
y_test = np.array([label_map[label] for label in y_test])

num_classes = len(unique_labels)

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# -----------------------------
# Build CNN
# -----------------------------
model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    MaxPooling2D((2,2)),

    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D((2,2)),

    Flatten(),

    Dense(128, activation="relu"),
    Dropout(0.3),

    Dense(num_classes, activation="softmax")
])

# -----------------------------
# Compile
# -----------------------------
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# Train
# -----------------------------
model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test)
)

# -----------------------------
# Evaluate
# -----------------------------
loss, accuracy = model.evaluate(X_test, y_test)

print(f"\nTest Accuracy: {accuracy*100:.2f}%")

# -----------------------------
# Save model
# -----------------------------
model.save("model/sign_model.h5")

print("\nModel saved successfully!")
print("Location: model/sign_model.h5")