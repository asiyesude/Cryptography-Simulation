# Cryptography-Simulation
A Python-based cybersecurity project simulating secure military communication protocols. This application uses a symmetric shift encryption algorithm to obscure classified messages and decrypt them using a predefined security key.

## Core Features
- **Encryption Engine:** Converts plaintext into a secure, unreadable ciphertext format using a mathematical shift algorithm based on ASCII values.
- **Decryption Engine:** Reverses the algorithmic shift to restore the original message, strictly requiring the correct security key.
- **Data Integrity:** The algorithm ensures that only alphabetic characters are manipulated, preserving numeric data (e.g., coordinates, distances) and punctuation for structural integrity.

##  Tech Stack
- **Language:** Python 3
- **Environment:** Visual Studio Code / Terminal
- **Concepts:** Cybersecurity, Cryptography, Algorithmic Thinking

##  How to Run
The main algorithm is located in the `main.py` file. Execute the script in any Python terminal and input the message you wish to encrypt/decrypt.
