# Quantum Glasses

Quantum Glasses is a visualization tool for single-qubit rotations on the Bloch Sphere. It is built using Python, Tkinter, and Qiskit. The application allows users to apply various quantum gates to a single qubit and visualize the resulting state on the Bloch Sphere.

This project is inspired by the work of **Jay Shah** and aims to provide an intuitive way to interact with quantum gates and qubit states.

## Features

- Apply common quantum gates (X, Y, Z, H, S, T, S†, T†) to a single qubit.
- Apply parameterized rotation gates (Rx, Ry, Rz) with customizable angles.
- Visualize the quantum state on the Bloch Sphere.
- Clear and delete operations to modify the circuit.
- User-friendly interface with buttons for each gate.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Qiskit
- Tkinter (usually comes pre-installed with Python)
- NumPy

You can install the required Python packages using pip:

```bash
pip install qiskit numpy
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/quantum-glasses.git
```

Navigate to the project directory:

```bash
cd quantum-glasses
```

Run the application:

```bash
python tut.py
```

## Usage

- **Applying Gates**: Click on the buttons corresponding to the quantum gates you want to apply. The gates will be applied to the qubit in the order you click them.
- **Parameterized Rotations**: For Rx, Ry, and Rz gates, a window will pop up allowing you to select the rotation angle (in multiples of π).
- **Visualization**: Click the "Visualize" button to see the current state of the qubit on the Bloch Sphere.
- **Clearing the Circuit**: Use the "Clear" button to reset the circuit and start over.
- **Deleting the Last Gate**: Use the "Delete" button to remove the last applied gate from the circuit.
- **About**: Click the "About" button to get more information about the application and the gates.

## Example

Here's an example of how to use the application:

1. Apply an X gate by clicking the "X" button.
2. Apply a Hadamard gate by clicking the "H" button.
3. Apply an Ry gate with a rotation angle of π/2 by clicking the "Ry" button and selecting "π/2".
4. Click the "Visualize" button to see the state of the qubit on the Bloch Sphere.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Built using Qiskit, an open-source quantum computing framework.
- Inspired by the work of **Jay Shah**.
- Developed as a simple quantum visualization tool for learning and experimentation.

