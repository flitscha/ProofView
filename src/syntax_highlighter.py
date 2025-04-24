import re


def highlight_goal(goal_str: str) -> str:
    """
    param goal_str: The goal string to be highlighted.
    return: The highlighted goal string as HTML.
    """

    # make the case-line green
    html = re.sub(
        r"^(case\s+[^\n]+)", 
        r'<span class="goal-case">\1</span>', 
        goal_str, 
        flags=re.MULTILINE
    )

    # everything before the first colon on a line becomes orange (goal-id)
    html = re.sub(
        r"^(?!\s*⊢)(.*?)(\s*:\s*)(.*)$",  # not the goal line (⊢)
        r'<span class="goal-id">\1</span>\2\3',
        html,
        flags=re.MULTILINE
    )

    # make turnstile ⊢ blue
    html = html.replace("⊢", '<span class="goal-turnstile">⊢</span>')

    return f'<pre class="goal-pre">{html}</pre>'
