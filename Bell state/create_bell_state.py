
def create_bell_state():
    # Create a quantum circuit with two qubits
    circuit = QuantumCircuit(2, 2)

    # Apply a Hadamard gate to the first qubit
    circuit.h(0)

    # Apply a controlled-X (CNOT) gate with the first qubit as the control and the second qubit as the target
    circuit.cx(0, 1)

    return circuit


