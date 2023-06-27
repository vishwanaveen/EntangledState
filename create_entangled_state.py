from qiskit import QuantumCircuit


def create_entangled_state(state, num_qubits=None):
     output_circuit = QuantumCircuit()

    if state == 'bell':
        return create_bell_state(output_circuit)
    elif state == 'ghz':
        return create_ghz_state(output_circuit, num_qubits)
    elif state == 'w':
        return create_w_state(output_circuit, num_qubits)
    # Add more state cases as needed
    else:
        print("Invalid state name!")

    return output_circuit
