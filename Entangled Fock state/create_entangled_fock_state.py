#from qiskit import QuantumCircuit
#from qiskit.quantum_info import Statevector

def create_entangled_fock_state(n, m):
    circuit = QuantumCircuit(2)

    circuit.x(0)  # Prepare qubit 0 in |1⟩ Fock state
    circuit.x(1)  # Prepare qubit 1 in |1⟩ Fock state
    circuit.cx(0, 1)  # Entangle qubit 0 and qubit 1

    return Statevector.from_instruction(circuit)
