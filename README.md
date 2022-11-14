# Overview

A very simple very specific example where python can do tight loops faster than C# (.NET core) using the Numba library.

Project Euler 5: https://projecteuler.net/problem=5

# Run Dotnet Core

Build and run

`(cd dnc/cs && dotnet run)`


# Python

Create virtual env

`python3 -m venv numba/.venv`

Install requirements

`source numba/.venv/bin/activate`

`pip install -r numba/requirements`

`chmod +x numba/main.py`

Run

`numba/main.py`
