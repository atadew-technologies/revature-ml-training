# Create a Task (POST /tasks):

Endpoint to create a new task.
The task should have fields like id, title, description, completed (boolean), and due_date.
Use Pydantic models for request validation.
Read Tasks (GET /tasks): 
 
# Endpoint to retrieve all tasks.
Add query parameters to filter tasks based on completion status (e.g., /tasks?completed=true).
Read a Single Task (GET /tasks/{task_id}):

# Endpoint to retrieve a specific task by id. 
Update a Task (PUT /tasks/{task_id}): 

# Endpoint to update an existing task's title, description, completion status, or due date.
Delete a Task (DELETE /tasks/{task_id}):

# Endpoint to delete a task by id.
Mark a Task as Completed (PATCH /tasks/{task_id}/complete):

# Endpoint to mark a task as completed.
# Error Handling:

Implement basic error handling for scenarios like task not found, invalid input, etc.
Data Persistence:

