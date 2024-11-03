addTask = document.getElementById("add-task");

checkboxes = document.getElementsByClassName("checkbox");

cancelTask = document.getElementById("cancel-task-editor");

// If the add task button is clicked
addTask.addEventListener("click", (event) => {
    taskEditor = document.getElementById("task-editor");

    // Show the task editor so that the user can create a new task
    taskEditor.removeAttribute("hidden");
});

cancelTask.addEventListener("click", (event) => {
    taskEditor = document.getElementById("task-editor");

    // Hide the task editor
    taskEditor.setAttribute("hidden", "");
})
