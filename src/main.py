import sys
import os

# Agregar la ruta del directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.quantum_simulation import quantum_simulation
from src.ml_model import train_ml_model

def main():
    print("Iniciando simulación cuántica...")
    statevector = quantum_simulation()
    
    print("\nEntrenando modelo de Machine Learning para ciberseguridad...")
    model = train_ml_model()

    print("\n🚀 Proyecto finalizado. Simulación cuántica y detección de ataques completadas.")

if __name__ == "__main__":
    main()
