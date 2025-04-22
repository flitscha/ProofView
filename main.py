import asyncio

from parser import parse_lean_file
from data_model import ProofStep, LeanLine
from lean_client_interface import LeanSession
from add_metadata import add_goals_to_proof_steps
from export_html import generate_and_save_html


async def main():
    #file = "examples/task1.lean"
    file = "examples/example_file.lean"
    #file = "/mnt/c/daten/programmieren/lean/Math/Math/Topology_Homework/task1.lean"
    proof_steps = parse_lean_file(file)
    lean_session = LeanSession(file)
    await lean_session.start()

    await add_goals_to_proof_steps(lean_session, proof_steps)

    html = generate_and_save_html(proof_steps, output_file="output.html")
    print("html generated successfully")

if __name__ == "__main__":
    asyncio.run(main())