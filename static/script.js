function toggleCode(id) {
    const block = document.getElementById(id);
    if (block.style.display === "none" || block.style.display === "") {
        block.style.display = "block";
    } else {
        block.style.display = "none";
    }
}


function setGoalFromElement(id) {
    const goalText = document.getElementById(id).innerText;
    setGoal(goalText);
}


function setGoal(goal_string) {
    const goalArea = document.getElementById("goal-display");
    goalArea.innerHTML = `
        <div>${goal_string}</div>
    `;
}
