addTask = document.getElementById("add-task");

checkboxes = document.getElementsByClassName("checkbox");

cancelTask = document.getElementById("cancel-task-editor");

for (let checkbox of checkboxes) {
    checkbox.addEventListener("click", (event) => {
        // Prevent form from submitting a GET/POST request
        event.preventDefault();

        const taskId = document.getElementById("task-id").innerHTML;
        const status = document.getElementById("status").value;

        const data = {
            taskId: taskId,
            status: status,
        };
        console.log(data);

        // Send the PATCH request
        fetch("/", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
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
