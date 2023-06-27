
def create_singlet_state():
    circuit = QuantumCircuit(2)

    circuit.h(0)
    circuit.cx(0, 1)
    circuit.x(1)

    return circuit
