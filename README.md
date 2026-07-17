# is_lab — Information Security Lab programs

Educational lab programs demonstrating classical ciphers and simple cryptographic concepts.

## Overview

This repository contains short, interactive CLI demos used for learning basic information security concepts:
- Classical ciphers (Caesar, Affine, Hill, Vigenère)
- SHA-256 hashing comparison demo
- Basic RSA key generation, encryption/decryption and signing (demonstration only)
- Simple shell utilities and a file copy example

These scripts are intended for classroom or personal learning use only and are not suitable for production or real security needs.

## Contents

- `ciphers/` — Caesar, Affine, Hill, Vigenère cipher demos (Python)
- `rsa.py` — RSA generation / encryption / decryption demo (requires `sympy`)
- `rsa_sign.py` — RSA signing and verification demo (requires `sympy`, uses `hashlib`)
- `sha.py` — SHA-256 hashing demo and bit-difference counter
- `filecopy.py` — simple file copy using low-level `os` calls
- `shell/` — small shell scripts (display files, integrity demo, simple login simulation)

## Requirements

- Python 3.8+ recommended
- `sympy` (only for `rsa.py` and `rsa_sign.py`)
- Unix-like shell for the shell scripts (bash)

Install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install sympy
```

## Usage

Run Python scripts directly:
```bash
python3 ciphers/caesar.py
python3 ciphers/affine.py
python3 ciphers/hill.py
python3 ciphers/vigenere.py

python3 sha.py
python3 filecopy.py

python3 rsa.py         # interactive RSA demo
python3 rsa_sign.py    # RSA signing demo
```

Run shell scripts:
```bash
chmod +x shell/*.sh
./shell/displayfiles.sh
./shell/integrity.sh
./shell/userlogin.sh
```

## Security disclaimer

These are demonstration programs for learning. They:
- Use small/insecure key sizes in many examples (for teaching)
- Are interactive and not hardened for production
- Should not be used to encrypt or sign any real or sensitive data

