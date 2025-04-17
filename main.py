# main.py

from parser import parse_lean_file
from data_model import ProofStep, LeanLine


def main():
    proof_steps = parse_lean_file("examples/example_file.lean")

    for step in proof_steps:
        print("Proof Step:")
        print(f"Comment: {step.latex_comment}")
        for line in step.lean_code:
            print(f"Lean Line: {line.lean_line}")
            print(f"Goal Before: {line.goal_before}")
            print(f"Goal After: {line.goal_after}")
        print()

    

if __name__ == "__main__":
    main()