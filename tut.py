import qiskit
print(qiskit.__version__)
import tkinter
import numpy as np
from qiskit import QuantumCircuit
from tkinter import DISABLED, LEFT, RIGHT, END, WORD
from qiskit.visualization import visualize_transition
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="qiskit.visualization.transition_visualization")

#define window
root = tkinter.Tk()
root.title("Quantum Glasses") 

#set the icon
##root.iconbitmap('logo.ico')
root.geometry("460x380")
root.configure(bg="#000000")  # Set the background color of the root window to black
root.resizable(0,0) #blocks the resizing of the window

#set colors and fonts
background="#000000" # black
buttons="#FFD700" # yellow
special_buttons="#FFA500" # orange
button_font=("Arial", 15)
display_font=("Arial", 30)

#initialize the quantum circuit
def initalize_circuit():
    global circuit
    circuit = QuantumCircuit(1)

initalize_circuit()

theta=0

#define frames
display_frame = tkinter.LabelFrame(root, bg=background)
display_frame.pack()
button_frame = tkinter.LabelFrame(root, bg=background)
button_frame.pack()

#define display frame layout
display = tkinter.Entry(display_frame, font=display_font, width=120, borderwidth=5, relief=tkinter.FLAT, justify=tkinter.RIGHT, bg=background, fg=buttons)
display.pack(padx=10, pady=10)

#Define first row of buttons
X_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="X", command=lambda: [display_gate("X"), circuit.x(0)])
Y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="Y", command=lambda: [display_gate("Y"), circuit.y(0)])
Z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="Z", command=lambda: [display_gate("Z"), circuit.z(0)])
X_gate.grid(row=0, column=0, ipadx=53, pady=1, sticky='NSEW')
Y_gate.grid(row=0, column=1, ipadx=53, pady=1, sticky='NSEW')
Z_gate.grid(row=0, column=2, ipadx=53, pady=1, sticky='NSEW')

#Define second row of buttons
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="Rx", command=lambda: user_input(circuit, "x"))
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="Ry", command=lambda: user_input(circuit, "y"))
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="Rz", command=lambda: user_input(circuit, "z"))
Rx_gate.grid(row=1, column=0, ipadx=45, pady=1, sticky='NSEW')
Ry_gate.grid(row=1, column=1, ipadx=45, pady=1, sticky='NSEW')
Rz_gate.grid(row=1, column=2, ipadx=45, pady=1, sticky='NSEW')

#Define third row of buttons
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="S", command=lambda: [display_gate("S"), circuit.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="S†", command=lambda: [display_gate("S†"), circuit.sdg(0)])
hadamard = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="H", command=lambda: [display_gate("H"), circuit.h(0)])
s_gate.grid(row=2, column=0, ipadx=45, pady=1, sticky='NSEW')
sd_gate.grid(row=2, column=1, ipadx=45, pady=1, sticky='NSEW')
hadamard.grid(row=2, column=2, ipadx=45, pady=1, rowspan=2, sticky='NSEW')

#Define fourth row of buttons
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="T", command=lambda: [display_gate("T"), circuit.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, fg=background, text="T†", command=lambda: [display_gate("T†"), circuit.tdg(0)])
t_gate.grid(row=3, column=0, ipadx=45, pady=1, sticky='NSEW')
td_gate.grid(row=3, column=1, ipadx=45, pady=1, sticky='NSEW')

#Define quit and visualise buttons
quit_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, fg=background, text="QUIT", command=root.destroy)
quit_button.grid(row=4, column=0, ipadx=45, pady=1, columnspan=2, sticky='NSEW')
visualise_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, fg=background, text="Visualise", command=lambda: visualize_circuit())
visualise_button.grid(row=4, column=2, ipadx=45, pady=1, sticky='NSEW')

#Define clear, delete, and about buttons
clear_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, fg=background, text="Clear", command=lambda: clear())
clear_button.grid(row=5, column=0, ipadx=45, pady=1, columnspan=2, sticky='NSEW')
delete_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, fg=background, text="Delete", command=lambda: delete_last_gate())
delete_button.grid(row=5, column=2, ipadx=45, pady=1, sticky='NSEW')
about_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, fg=background, text="About", command=lambda: about())
about_button.grid(row=6, column=0, ipadx=45, pady=1, columnspan=3, sticky='NSEW')

#define about button
def about():
    info = tkinter.Tk()
    info.title("About")
    info.geometry('650x450')
    info.configure(bg=background)  # Set the background color of the info window to black
    info.resizable(0, 0)
    
    text = tkinter.Text(info, height=20, width=20, wrap=tkinter.WORD, font=("Arial", 15), bg=background, fg=buttons)
    
    #create label
    label = tkinter.Label(info, text="About Quantum Glasses", font=("Arial", 20), bg=background, fg=buttons)
    label.config(font=("Arial", 20))
    
    text_to_display = """
    About: Visualization tool for Single Qubit Rotation on Bloch Sphere
    
        Created by : Mayank Sharma
        Created using: Python, Tkinter, Qiskit
    
        Info about the gate buttons and corresponding qiskit commands:
    
        X = flips the state of qubit -                                 circuit.x()
        Y = rotates the state vector about Y-axis -                    circuit.y()
        Z = flips the phase by PI radians -                            circuit.z()
        Rx = parameterized rotation about the X axis -                 circuit.rx()
        Ry = parameterized rotation about the Y axis.                  circuit.ry()
        Rz = parameterized rotation about the Z axis.                  circuit.rz()
        S = rotates the state vector about Z axis by PI/2 radians -    circuit.s()
        T = rotates the state vector about Z axis by PI/4 radians -    circuit.t()
        Sd = rotates the state vector about Z axis by -PI/2 radians -  circuit.sdg()
        Td = rotates the state vector about Z axis by -PI/4 radians -  circuit.tdg()
        H = creates the state of superposition -                       circuit.h()
    
        For Rx, Ry and Rz, 
        theta(rotation_angle) allowed range in the app is [-2*PI,2*PI]
    
        In case of a Visualization Error, the app closes automatically.
        This indicates that visualization of your circuit is not possible.
    
        At a time, only ten operations can be visualized."""
    
    label.pack()
    text.pack()
    text.insert(tkinter.END, text_to_display)
    info.mainloop()

#define display functions
def display_gate(gate_input):
    """Adds a corresponding gate notation in the display to track the operations.
    If the number of operation reach ten, all gate buttons are disabled
    """
    display.insert(tkinter.END, gate_input)    
    
    #check if number of functions has reached 10 if yes
    #disable all the gate buttons
    input_gate = display.get()
    num_gates_pressed = len(input_gate)
    search_word = ["R", "D"]
    count_double_valued_gates = [input_gate.count(i) for i in search_word]
    num_gates_pressed += sum(count_double_valued_gates)
    if num_gates_pressed == 10:
        gates = [X_gate, Y_gate, Z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, hadamard, t_gate, td_gate]
        for gate in gates:
            gate.config(state=DISABLED)

def delete_last_gate():
    """Deletes the most recent gate from the display and the circuit"""
    input_gate = display.get()
    if input_gate:
        last_gate = input_gate[-1]
        display.delete(len(input_gate) - 1, tkinter.END)
        if last_gate == "X":
            circuit.x(0)
        elif last_gate == "Y":
            circuit.y(0)
        elif last_gate == "Z":
            circuit.z(0)
        elif last_gate == "S":
            circuit.s(0)
        elif last_gate == "H":
            circuit.h(0)
        elif last_gate == "T":
            circuit.t(0)
        elif last_gate == "†":
            if input_gate[-2] == "S":
                circuit.sdg(0)
            elif input_gate[-2] == "T":
                circuit.tdg(0)
            display.delete(len(input_gate) - 2, tkinter.END)

def change_theta(num, window, circuit, key):
    global theta
    theta = num * np.pi
    
    if key == "x":
        circuit.rx(theta, 0)
    elif key == "y":
        circuit.ry(theta, 0)
    elif key == "z":
        circuit.rz(theta, 0)    
    window.destroy()
    
def user_input(circuit, key):
    #take user input for the rotation angle for parameterized gates Rx, Ry, Rz
    
    #initialize and define the properties of the input window
    get_input = tkinter.Tk()
    get_input.title("Get Theta")
    get_input.geometry('400x160')
    get_input.configure(bg=background)  # Set the background color of the input window to black
    get_input.resizable(0, 0)
    
    #set values for theta as pi/4, pi/2 pi 2pi and negative of the same angles
    val1= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="PI/4", command=lambda: change_theta(0.25, get_input, circuit, key))
    val1.grid(row=0, column=0, padx=5, pady=5)
    
    val2= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="PI/2", command=lambda: change_theta(0.5, get_input, circuit, key))
    val2.grid(row=0, column=1, padx=5, pady=5)
    
    val3= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="PI", command=lambda: change_theta(1, get_input, circuit, key))
    val3.grid(row=0, column=2, padx=5, pady=5)
    
    val4= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="2PI", command=lambda: change_theta(2, get_input, circuit, key))
    val4.grid(row=0, column=3, padx=5, pady=5)
    
    nval1= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="-PI/4", command=lambda: change_theta(-0.25, get_input, circuit, key))
    nval1.grid(row=1, column=0, padx=5, pady=5)
    
    nval2= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="-PI/2", command=lambda: change_theta(-0.5, get_input, circuit, key))
    nval2.grid(row=1, column=1, padx=5, pady=5)
    
    nval3= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="-PI", command=lambda: change_theta(-1, get_input, circuit, key))
    nval3.grid(row=1, column=2, padx=5, pady=5)
    
    nval4= tkinter.Button(get_input, height=2,width=7, bg=buttons, fg=background, font=("Arial", 15), text="-2PI", command=lambda: change_theta(-2, get_input, circuit, key))
    nval4.grid(row=1, column=3, padx=5, pady=5)

def clear():
    """Clears the display and re-enables the gate buttons"""
    #check if the buttons are disabled and if they are then enable them
    display.delete(0, tkinter.END)
    initalize_circuit()
    if X_gate['state'] == DISABLED:
        gates = [X_gate, Y_gate, Z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, hadamard, t_gate, td_gate]
        for gate in gates:
            gate.config(state='normal')

def visualize_circuit():
    try:
        visualize_transition(circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        pass

#run main
root.mainloop()