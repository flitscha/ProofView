function toggleCode(id) {
    const block = document.getElementById(id);
    if (block.style.display === "none" || block.style.display === "") {
        block.style.display = "block";
    } else {
        block.style.display = "none";
    }
}
