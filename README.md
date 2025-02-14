# 🎲 Truly Random  

**Truly Random** is a Quantum Random Number Generator (QRNG) that leverages the power of quantum mechanics to generate **unpredictable, truly random numbers**. Unlike classical random number generators, which rely on deterministic algorithms, this project uses quantum states, ensuring a higher level of randomness.  

## 🚀 How It Works  
The QRNG generates a random number between **0 and 2ⁿ**, where **n** is the number of qubits specified by the user. Quantum mechanics introduces **true randomness**, making the results impossible to predict.  

## 🛠️ Technologies Used  
- **Quantum Computing:** Qiskit (for quantum randomness)  
- **Backend:** Python & Flask (to serve the API)  

## 🔧 Setup & Usage  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/truly-random.git
   cd truly-random
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the API server:**
   ```bash
   python app.py
   ```
4. **Generate a random number:**
- Send a request to the API, specifying the number of qubits.
- Example: GET /generate?n=5 will return a number between 0 and 31 (2⁵)

## 📌 Features
✅ Generates truly random numbers using quantum mechanics
✅ Simple API for seamless integration into applications
✅ Customizable qubit count for different randomness ranges

## 📜 License
This project is licensed under the MIT License.
