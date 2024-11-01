addTask = document.getElementById("add-task");

checkboxes = document.getElementsByClassName("checkbox");

cancelTask = document.getElementById("cancel-task-editor");

for (let checkbox of checkboxes) {
    checkbox.addEventListener("click", (event) => {
        task = checkbox.parentNode;

        // If the task is not finished, set it to a finished task. Otherwise, set it to an unfinished task
        task.className =
            task.className === "unfinished-task"
                ? "finished-task"
                : "unfinished-task";
    });
}

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
