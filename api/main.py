from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)



# Set up the template directory for rendering HTML files
templates = Jinja2Templates(directory="templates")

# Define a Pydantic model for the request body
class QubitRequest(BaseModel):
    num_qubits: int

# Route for serving the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    # Render and return the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

# Route for generating a quantum random number
@app.post("/random_number")
async def generate_random_number(request: QubitRequest):
    num_qubits = request.num_qubits

    # Ensure the number of qubits is between 1 and 15
    if num_qubits < 1 or num_qubits > 15:
        raise HTTPException(status_code=400, detail="Number of qubits must be between 1 and 15")

    # Generate the random number using the QRNG function with the specified number of qubits
    random_number = QRNG(num_qubits)
    # Return the generated number as a JSON response
    return {"random_number": random_number}

# Function to generate a quantum random number using Qiskit
def QRNG(num_bits: int):
    # Initialize a quantum circuit with the specified number of qubits and classical bits
    qc = QuantumCircuit(num_bits, num_bits)

    # Apply a Hadamard gate to each qubit to create superposition
    for qubit in range(num_bits):
        qc.h(qubit)

    # Measure the qubits and store the results in the classical bits
    qc.measure(range(num_bits), range(num_bits))

    # Create an instance of the AerSimulator
    simulator = AerSimulator()
    
    # Transpile the circuit for the simulator
    compiled_circuit = transpile(qc, simulator)
    
    # Run the simulation and get the result
    sim_result = simulator.run(compiled_circuit).result()
    
    # Get the counts of the measurement results
    counts = sim_result.get_counts()
    
    # Extract the binary string from the results and convert it to a decimal number
    random_number = int(list(counts.keys())[0], 2)
    
    return random_number
