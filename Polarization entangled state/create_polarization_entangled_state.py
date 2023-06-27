def create_polarization_entangled_state(num_photons):
    circuit = QuantumCircuit(num_photons)

    for i in range(num_photons-1):
        circuit.h(i)
        circuit.cx(i, i+1)

    return circuit
