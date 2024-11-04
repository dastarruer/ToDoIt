# ToDoIt
## Video Description: https://youtu.be/gpzWr6wI1kg
## Overview
ToDoIt is a Flask app that allows users to register, login, and add their own tasks. These tasks can be either complete, or uncomplete, but they can never be deleted. While it is a pretty bare-bones to-do list app, this was really for me to learn about handling multiple users, which I'm pleased to report has turned out well. Because I'm lazy, I will only be documenting `tasks.db`.
## `tasks.db`
The users and their tasks are stored in this database. It uses `sqlite3`, which I chose because it's the only SQL version I know thus far. 
### `users`
This table stores the user's `id`, `username`, and `hash` (an encrypted password).  
The `id` column is handy for remembering which user is logged in currently, and fetching the user's current tasks.  
`username` is actually pretty useless, but I felt it should be included in the signup process as a formality.  
`hash` is just a security measure that ensures that the user is who they say they are. Of course, this is also just another formality. 
### `tasks`
This table is where all tasks are stored. Each task is given an `id`, a `user_id`, a `title`, a `description`, and a column called `completed`.  
`id` is a unique identifier that allows the backend to easily search for a certain task in order to change its `completed` column.  
`user_id` is a foreign key that references `id` in the `users` table. This allows the app to display all the tasks that the current user has.  
The `title` and `description` columns are self-explanatory; they are simply the title and the description that the user gives the task.  
Lastly, the `completed` column have the status of the task; a `1` for completed, and `0` for uncompleted.