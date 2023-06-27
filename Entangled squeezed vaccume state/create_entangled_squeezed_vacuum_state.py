#from qiskit import QuantumCircuit
#from qiskit.quantum_info import Statevector

def create_entangled_squeezed_vacuum_state(r, phi):
    circuit = QuantumCircuit(2)

    circuit.s(0)  # Squeezing gate on qubit 0
    circuit.s(1)  # Squeezing gate on qubit 1
    circuit.cx(0, 1)  # Entangle qubit 0 and qubit 1

    return Statevector.from_instruction(circuit)
