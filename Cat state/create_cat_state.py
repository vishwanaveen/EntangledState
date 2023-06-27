

def create_cat_state():
    circuit = QuantumCircuit(1)

    circuit.h(0)
    circuit.rz(0.5, 0)
    circuit.s(0)

    return circuit
