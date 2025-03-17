import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf

def train_ml_model():
    # Simular datos cuánticos para ciberseguridad
    np.random.seed(42)
    data_size = 500
    X = np.random.rand(data_size, 2)  # Características simuladas
    y = np.random.randint(0, 2, data_size)  # Etiquetas binarias

    # Dividir datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelo Random Forest para detección de patrones de ciberseguridad
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy * 100:.2f}%")

    return model

if __name__ == "__main__":
    train_ml_model()
