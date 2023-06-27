
def create_noon_state(num_particles):
    circuit = QuantumCircuit(num_particles)

    circuit.h(0)
    for i in range(1, num_particles):
        circuit.cx(0, i)

    return circuit
