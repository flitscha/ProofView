# ProofView
Convert a Lean proof with Latex comments, to an interactive HTML document.


## What It Does
This tool parses a Lean4 proof file containing special LaTeX-style comments (written using `/-  -/`) and generates an interactive HTML file where:
- You can **expand each comment** to see the related Lean code.
- You can **click buttons next to each line** to view the current proof goals at that point.
- You can **navigate goals** using your keyboard’s arrow keys.
- All math is rendered using MathJax (LaTeX-style).

It can be useful to present mathematical proofs more clearly:  
By always showing the **current goals and assumptions**, it may be easier to follow a complex proof.


## How To Use
1. Annotate your `.lean` proof file using block comments `/- ... -/` with LaTeX/MathJax content.
2. Run the script:
```bash
python3 src/main.py path/to/your_proof.lean
```
Optional flags:
- `--project_root` Path to your Lean project (needed if you're using mathlib).
- `--output` Name of the output HTML file.
- `--language` en or de (default: en).
- `--title` Custom title for the HTML page.


## Example
The repository contains an example Lean file:  
`src/examples/example_file.lean`  
You can try it out directly:
```bash
python3 src/main.py src/examples/example_file.lean
```
This will create an output.html file with the interactive proof view.


## Requirements
- Make sure lean4 is installed and that it works with the file you want to convert. (Goals are displayed correctly, no error messages)
- obviously you also need python.


## Warning
When using larger proofs or mathlib, the first time you run the script, Lean will need to load mathlib, which can take several minutes depending on your system.
