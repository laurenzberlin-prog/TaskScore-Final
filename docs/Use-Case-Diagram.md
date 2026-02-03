# Use Case Model – TaskScore

```mermaid
flowchart LR

User((User))

Login[Login]
Register[Register]
AddTask[Create Task]
DeleteTask[Delete Task]
ViewTasks[View Tasks]
ToggleTask[Mark Task as Done]
ViewPlan[View Weekly Plan]
ViewProgress[View Progress]
Logout[Logout]

User --> Login
User --> Register
User --> AddTask
User --> DeleteTask
User --> ViewTasks
User --> ToggleTask
User --> ViewPlan
User --> ViewProgress
User --> Logout