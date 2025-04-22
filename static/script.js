let currentActiveButton = null;
let goalButtons = [];
let goalButtonIndex = -1;


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
        
        // keep track of the current button index (for keyboard navigation)
        const newIndex = goalButtons.indexOf(button_element);
        goalButtonIndex = newIndex;
    }
}



// load all goal buttons on page load
window.addEventListener('load', () => {
    goalButtons = Array.from(document.querySelectorAll('.goal-button'));
});

// keyboard navigation for goal buttons
document.addEventListener('keydown', (e) => {
    if (goalButtons.length === 0) return;

    if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (goalButtonIndex < goalButtons.length - 2) {
            goalButtonIndex = goalButtonIndex + 2;
        }
    }

    if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (goalButtonIndex > 1) {
            goalButtonIndex = goalButtonIndex - 2;
        }
    }

    if (e.key === 'ArrowRight') {
        e.preventDefault();
        if (goalButtonIndex < goalButtons.length - 1) {
            goalButtonIndex = goalButtonIndex + 1;
        }
    }

    if (e.key === 'ArrowLeft') {
        e.preventDefault();
        if (goalButtonIndex > 0) {
            goalButtonIndex = goalButtonIndex - 1;
        }
    }

    goalButtons[goalButtonIndex].click();
});