checkboxes = document.getElementsByClassName("checkbox");
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
