#from qiskit import QuantumCircuit
#from qiskit.quantum_info import Statevector

def create_spin_squeezed_state(num_qubits, theta):
    circuit = QuantumCircuit(num_qubits)
    
    for i in range(num_qubits):
        circuit.rx(theta, i)

    return Statevector.from_instruction(circuit)
