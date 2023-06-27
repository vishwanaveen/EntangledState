#from qiskit import QuantumCircuit
#from qiskit.quantum_info import Statevector

def create_entangled_coherent_state(alpha, beta):
    circuit = QuantumCircuit(2)

    circuit.initialize([alpha, beta], [0, 1])

    return Statevector.from_instruction(circuit)
