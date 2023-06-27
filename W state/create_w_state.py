def create_w_state(num_qubits):
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)  # Apply a Hadamard gate to the first qubit

    for i in range(1, num_qubits):
        circuit.cx(0, i)  # Apply a CNOT gate from the first qubit to the remaining qubits

    return circuit


