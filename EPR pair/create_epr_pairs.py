

def create_epr_pairs(num_pairs):
    # Create a quantum circuit with two qubits per EPR pair
    circuit = QuantumCircuit(2 * num_pairs, 2 * num_pairs)

    for i in range(num_pairs):
        # Apply a Hadamard gate to the first qubit of each pair
        circuit.h(2 * i)

        # Apply a controlled-X (CNOT) gate with the first qubit as the control and the second qubit as the target
        circuit.cx(2 * i, 2 * i + 1)

    return circuit


