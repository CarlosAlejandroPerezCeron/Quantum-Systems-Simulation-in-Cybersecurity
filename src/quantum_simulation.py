from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
import numpy as np
import matplotlib.pyplot as plt

def quantum_simulation():
    # Crear un circuito cuántico de 2 qubits
    qc = QuantumCircuit(2)
    qc.h(0)  # Puerta Hadamard en el primer qubit
    qc.cx(0, 1)  # Entrelazamiento cuántico

    # Ejecutar la simulación en un simulador de estado vectorial
    simulator = Aer.get_backend("statevector_simulator")
    transpiled_qc = transpile(qc, simulator)
    qobj = assemble(transpiled_qc)
    result = simulator.run(qobj).result()
    statevector = result.get_statevector()
    
    print("Estado final del sistema cuántico:", statevector)

    # Visualizar el circuito
    qc.draw("mpl")
    plt.show()

    return statevector

if __name__ == "__main__":
    quantum_simulation()

