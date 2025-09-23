# Interview Q&A – Lab 31: CLI Applications with argparse

1. **Q:** What is argparse in Python?  
   **A:** A module for parsing command-line arguments and generating help text.

2. **Q:** What does `ArgumentParser()` do?  
   **A:** Creates a parser object for defining and handling arguments.

3. **Q:** How do you define an argument?  
   **A:** With `parser.add_argument('--name', type=str, help='...')`.

4. **Q:** How are arguments parsed?  
   **A:** Using `parser.parse_args()` which returns an object with attributes.

5. **Q:** What happens if no argument is passed?  
   **A:** The code should handle it with a default behavior (e.g., greet Stranger).

6. **Q:** How do you see usage instructions?  
   **A:** Run the script with `--help` or `-h`.

7. **Q:** Why is argparse better than sys.argv?  
   **A:** Provides validation, automatic help, and cleaner handling.

8. **Q:** Can argparse handle multiple arguments?  
   **A:** Yes, you can define many with `add_argument`.

9. **Q:** What are positional vs optional arguments?  
   **A:** Positional must be provided, optional use flags like `--name`.

10. **Q:** How would you extend this script?  
    **A:** Add more arguments (e.g., `--age`), subcommands, or default values.
