addTask = document.getElementById("add-task");

checkboxes = document.getElementsByClassName("checkbox");

cancelTask = document.getElementById("cancel-task-editor");

for (let checkbox of checkboxes) {
    checkbox.addEventListener("change", (event) => {
        // Prevent form from submitting a GET/POST request
        event.preventDefault();

        const taskId = checkbox.dataset.taskId;
        const status = checkbox.dataset.status;

        const data = {
            taskId: taskId,
            status: status
        };
        console.log(data);

        // Send the PATCH request with the data
        fetch("/", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            // After getting a response back, log the JSON
            .then((response) => response.json())
            .then((data) => console.log(data));
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
});
