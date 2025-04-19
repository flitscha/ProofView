import asyncio

from parser import parse_lean_file
from data_model import ProofStep, LeanLine
from lean_client_interface import LeanSession
from add_metadata import add_goals_to_proof_steps
from export_html import generate_and_save_html


async def main():
    proof_steps = parse_lean_file("examples/example_file.lean")
    lean_session = LeanSession("examples/example_file.lean")
    await lean_session.start()

    await add_goals_to_proof_steps(lean_session, proof_steps)

    """
    for step in proof_steps:
        print("Proof Step:")
        print(f"Comment: {step.latex_comment}")
        for line in step.lean_code:
            print(f"Lean Line: {line.lean_line}")
            print(f"Goal Before: {line.goal_before}")
            print(f"Goal After: {line.goal_after}")
        print()"""
        
    html = generate_and_save_html(proof_steps, output_file="output.html")

if __name__ == "__main__":
    asyncio.run(main())