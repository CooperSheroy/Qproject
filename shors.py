# Import necessary libraries
import numpy as np
from qiskit import Aer, transpile, assemble
from qiskit import QuantumCircuit
from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
from qiskit.providers.aer import QasmSimulator

N = 15  # We are factorizing 15

# Setup the simulator
simulator = Aer.get_backend('qasm_simulator')

# Set up Shor's algorithm
shor = Shor(quantum_instance=QuantumInstance(backend=simulator, shots=1024))

# Run Shor's algorithm
result = shor.factor(N)

# Output the result
print(f"The factors of {N} are {result.factors}")
