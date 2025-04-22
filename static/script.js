let currentActiveButton = null;

function toggleCode(id) {
    const block = document.getElementById(id);
    if (block.style.display === "none" || block.style.display === "") {
        block.style.display = "block";
    } else {
        block.style.display = "none";
    }
}


function setGoalFromElement(id, button_element) {
    const goalText = document.getElementById(id).innerText;
    setGoal(goalText, button_element);
}


function setGoal(goal_string, button_element) {
    const goalArea = document.getElementById("goal-display");
    goalArea.innerHTML = `<div>${goal_string}</div>`;

    // Remove the previous marked button
    if (currentActiveButton) {
        currentActiveButton.classList.remove("active-goal-button");
    }

    // Mark the new button as active
    if (button_element) {
        button_element.classList.add("active-goal-button");
        currentActiveButton = button_element;
    }
}
