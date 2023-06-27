#from qiskit import QuantumCircuit
$from qiskit.quantum_info import Statevector

def create_entangled_thermal_state(n, m, temperature):
    circuit = QuantumCircuit(2)

    circuit.reset(0)  # Prepare qubit 0 in the thermal state
    circuit.reset(1)  # Prepare qubit 1 in the thermal state
    circuit.cx(0, 1)  # Entangle qubit 0 and qubit 1

    return Statevector.from_instruction(circuit)
