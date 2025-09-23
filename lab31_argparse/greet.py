import argparse

# Create the parser
parser = argparse.ArgumentParser(description='A simple greeting application.')

# Add an argument
parser.add_argument('--name', type=str, help='The name of the person to greet.')

# Parse the argument
args = parser.parse_args()

# Use the parsed arguments
if args.name:
    print(f'Hello, {args.name}!')
else:
    print('Hello, Stranger!')
