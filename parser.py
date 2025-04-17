# parser.py

from data_model import ProofStep, LeanLine


def parse_lean_file(filepath):
    steps = [] # list of ProofStep objects
    current_comment = ""
    current_lean_lines = [] # list of LeanLine objects

    state = "lean_code" # state of the parser. Can be "comment", "lean_code"

    def append_step():
        # append the data of the last step to the list of steps
        current_step = ProofStep(
            latex_comment=current_comment,
            lean_code=current_lean_lines,
        )
        steps.append(current_step)
    
    # open the file and read it line by line
    with open(filepath, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped == "":
                continue # skip empty lines
            
            # start of a comment. Switch the state to "comment"
            if stripped.startswith("/-"):
                state = "comment"
                current_comment = [stripped.removeprefix("/-").strip()]
                current_lean_lines = []
                # append the data of the last step to the list of steps
                append_step()
                continue
            
            # comment state
            if state == "comment":
                if stripped.endswith("-/"):
                    current_comment.append(stripped.removesuffix("-/").strip())
                    state = "lean_code"
                else:
                    current_comment.append(stripped)
                continue
            
            # lean_code state
            if state == "lean_code":
                current_line = LeanLine(
                    lean_line=stripped,
                    goal_before=[],
                    goal_after=[],
                )
                current_lean_lines.append(current_line)
                continue
    append_step() # append the last step to the list of steps
    return steps