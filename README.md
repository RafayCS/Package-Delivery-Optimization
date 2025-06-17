# Package-Delivery-Optimization
This project simulates a package delivery system. It uses a hash table and a route optimization algorithm to deliver 40 packages across different locations in the most efficient way.

## Features

- Loads package data from `Package File.csv`
- Uses a hash table to store and look up packages quickly
- Implements a Nearest Neighbor algorithm to optimize delivery routes
- Handles special delivery rules (e.g., delayed packages, wrong address for package #9)
- Calculates total mileage of all trucks
- Lets users check the status of any package at any time

## Files

- `main.py` — Runs the application and controls the logic
- `hash_table.py` — Custom hash table with chaining for collision handling
- `package.py` — Package class with status tracking and time-based updates
- `truck.py` — Truck class for delivery route management
- `Package File.csv` — CSV file with package data

## How to Use

1. Run `main.py`
2. Follow the prompts:
   - Type `time` to check package statuses
   - Enter a time in `HH:MM:SS` format
   - Choose to view a single package or all packages

## Special Rules

- **Package #9** has the wrong address until 10:20 AM.

## Requirements

- Python 3.x

No external libraries are needed.

## About me
- Author: Rafay Abubakar 
- Email: rafayabubakar456@gmail.com 
- Github: github.com/RafayCS

















   - 
