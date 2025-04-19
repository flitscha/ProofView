from data_model import ProofStep, LeanLine
from pathlib import Path


def generate_proof_html_content(proof_steps: list[ProofStep]) -> str:
    html = ""
    for i, step in enumerate(proof_steps):
        html += f'<div class="proof-step">\n'
        html += f'  <div class="comment" onclick="toggleCode(\'code-{i}\')">{step.latex_comment}</div>\n'
        html += f'  <div class="lean-line" id="code-{i}">\n'
        for line in step.lean_code:
            html += f'    <pre>{line.lean_line}</pre>\n'
        html += f'  </div>\n'
        html += f'</div>\n'
    return html



def generate_and_save_html(proof_steps, output_file="output.html"):
    template_path = Path("templates/base.html")
    with open(template_path, "r", encoding="utf-8") as f:
        base_template = f.read()

    html_content = generate_proof_html_content(proof_steps)
    final_html = base_template.replace("{{ proof_steps }}", html_content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    return final_html

