

def create_squeezed_state(r, phi):
    circuit = QuantumCircuit(1)

    circuit.s(qubit=0)
    circuit.rz(phi, qubit=0)
    circuit.rz(r, qubit=0)
    circuit.sdg(qubit=0)

    return circuit
