# Lab 31: CLI Applications with argparse

## Objectives
- Understand the basics of creating CLI applications in Python.
- Learn how to use the argparse module to parse command-line arguments.
- Develop a simple CLI application that greets users.
- Explore argparse’s automatic help text generation.

## Steps
1. Import `argparse`.
2. Create a parser with `argparse.ArgumentParser()`.
3. Add an argument `--name`.
4. Parse arguments and greet user accordingly.
5. Test script with and without arguments.
6. View automatic help text.

## Example Usage
```bash
python greet.py --name Alice
# Output: Hello, Alice!

python greet.py
# Output: Hello, Stranger!

python greet.py --help
# Displays usage and options
```

## Summary
This lab introduced CLI applications in Python using `argparse`.  
You learned to define arguments, parse them, handle optional inputs, and generate help text automatically.  
