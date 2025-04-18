# add_metadata.py


async def add_goals_to_proof_steps(lean_session, proof_steps):
    """
    enrich the proof steps with goal information
    In each lean-line, add the goal before and after the line
    """
    for step in proof_steps:
        for line in step.lean_code:
            goal_before = await lean_session.get_goal_at_position(line.line_number, 1)
            goal_after = await lean_session.get_goal_at_position(line.line_number, len(line.lean_line))
            line.goal_before = goal_before
            line.goal_after = goal_after