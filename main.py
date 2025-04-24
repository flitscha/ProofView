import asyncio
import argparse

from parser import parse_lean_file
from data_model import ProofStep, LeanLine
from lean_client_interface import LeanSession
from add_metadata import add_goals_to_proof_steps
from export_html import generate_and_save_html


async def main():
    parser = argparse.ArgumentParser(description="Convert Lean file with LaTeX comments into interactive HTML.")
    parser.add_argument("lean_file", help="Path to the Lean file to process.")
    parser.add_argument("--project_root", help="Path to the Lean project root (for mathlib etc.).", default=None)
    parser.add_argument("--output", help="Name of the output HTML file.", default="output.html")
    parser.add_argument(
        "--language",
        choices=["en", "de"],
        help="Language of the HTML file ('en' = English, 'de' = German).",
        default="en"
    )
    parser.add_argument("--title", help="Title of the HTML file.", default="Lean Proof")
    args = parser.parse_args()

    # clean up the arguments
    if not args.output.endswith(".html"):
        args.output += ".html"
    
    if args.title == "Lean Proof" and args.language == "de":
        args.title = "Lean-Beweis"

    # create the html file
    proof_steps = parse_lean_file(args.lean_file)
    lean_session = LeanSession(args.lean_file, args.project_root)
    await lean_session.start()
    await add_goals_to_proof_steps(lean_session, proof_steps)
    html = generate_and_save_html(proof_steps, output_file=args.output, language=args.language, title=args.title)
    print("html generated successfully")


if __name__ == "__main__":
    asyncio.run(main())