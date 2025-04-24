import os

from data_model import ProofStep, LeanLine
from pathlib import Path
from syntax_highlighter import highlight_goal

def generate_proof_html_content(proof_steps: list[ProofStep]) -> str:
    html = ""
    for i, step in enumerate(proof_steps):
        html += f'<div class="proof-step">\n'
        html += f'  <div class="comment" onclick="toggleCode(\'code-{i}\')">{step.latex_comment}</div>\n'
        html += f'  <div class="lean-line" id="code-{i}">\n'

        for j, line in enumerate(step.lean_code):
            # each lean-line is a div with a button on each side
            html += f'    <div class="lean-line-row">\n'
            html += f'      <button class="goal-button" onclick="setGoalFromElement(\'goal-before-{i}-{j}\', this)"></button>\n'
            html += f'      <pre>{line.lean_line}</pre>\n'
            html += f'      <button class="goal-button" onclick="setGoalFromElement(\'goal-after-{i}-{j}\', this)"></button>\n'
            html += f'    </div>\n'

            # hidden goal divs to access, if the button is clicked
            html += f'    <div id="goal-before-{i}-{j}" class="hidden-goal">{highlight_goal(line.goal_before)}</div>\n'
            html += f'    <div id="goal-after-{i}-{j}" class="hidden-goal">{highlight_goal(line.goal_after)}</div>\n'
        
        html += f'  </div>\n'
        html += f'</div>\n'
    return html



def generate_and_save_html(proof_steps, output_file="output.html", language="en", title="Lean Proof"):
    # read the base template and the css and js files
    project_root = Path(os.path.dirname(os.path.abspath(__file__))).parent
    base = (project_root / "src" / "templates" / "base.html").read_text(encoding="utf-8")
    css = (project_root / "src" / "static" / "style.css").read_text(encoding="utf-8")
    js = (project_root / "src" / "static" / "script.js").read_text(encoding="utf-8")
    content = generate_proof_html_content(proof_steps)

    if language == "de":
        goal_hint = "Wählen Sie eine Position aus, um ein Ziel anzuzeigen."
        goal_title = "Ziele"
    else:
        goal_hint = "Select a position to view a goal."
        goal_title = "Goals"

    # replace the placeholders in the base template with the actual content
    final_html = (
        base
        .replace("/* CSS */", css)
        .replace("{{ JS }}", js)
        .replace("{{ CONTENT }}", content)
        .replace("{{ TITLE }}", title)
        .replace("{{ GOAL_TITLE }}", goal_title)
        .replace("{{ GOAL_HINT }}", goal_hint)
    )

    if language == "de":
        final_html = final_html.replace("no goals", "keine Ziele")

    # write the final html to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    return final_html

