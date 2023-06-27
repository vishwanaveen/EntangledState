def create_cluster_state(num_qubits):
    circuit = QuantumCircuit(num_qubits)

    for i in range(num_qubits):
        circuit.h(i)

    for i in range(num_qubits - 1):
        circuit.cx(i, i + 1)

    return circuit
