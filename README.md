# VIT Bhopal SGPA and CGPA Calculator

This is a simple Python command-line program that helps students calculate SGPA and CGPA using the VIT-style 10-point grading system.

## What It Does

The program can:

- calculate SGPA for one semester
- calculate CGPA from semester SGPAs
- calculate CGPA from subject-wise grades across multiple semesters

## Grade Mapping

- `S = 10`
- `A = 9`
- `B = 8`
- `C = 7`
- `D = 6`
- `E = 5`
- `F = 0`
- `N = 0`

## Requirements

- Python 3 installed

Check Python version:

```bash
python --version
```

## How to Run

Open a terminal in the project folder and run:

```bash
python g2.py
```

If `python` does not work on your system, try:

```bash
py g2.py
```

## How to Use

When the program starts, it shows 3 options:

1. Calculate SGPA from subject grades
2. Calculate CGPA from semester SGPAs
3. Calculate CGPA from all course grades

Enter the option number and then provide the required details.

### Option 1

Enter:

- number of subjects
- subject name
- subject credits
- subject grade

### Option 2

Enter:

- number of semesters
- SGPA of each semester
- credits of each semester

### Option 3

Enter:

- number of semesters
- number of subjects in each semester
- subject name
- subject credits
- subject grade

## Input Rules

- subjects and semesters must be positive whole numbers
- credits must be positive numbers
- SGPA must be between `0` and `10`
- grades must be one of `S, A, B, C, D, E, F, N`

## Output

The program displays:

- total credits
- total grade points or weighted points
- SGPA or CGPA
- approximate percentage for CGPA

## Note

The percentage is shown as:

`CGPA x 10`

This is only an approximate value.
