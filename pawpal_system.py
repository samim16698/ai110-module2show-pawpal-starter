from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


class Owner:
    def __init__(self, name: str, email: str, phoneNumber: str, preferences: str):
        """Initialize the owner's profile and pet list."""
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.preferences = preferences
        self.pets: List["Pet"] = []

    def updateProfile(self, name: Optional[str] = None, email: Optional[str] = None,
                      phoneNumber: Optional[str] = None, preferences: Optional[str] = None):
        """Update the owner's profile fields when new values are provided."""
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if phoneNumber is not None:
            self.phoneNumber = phoneNumber
        if preferences is not None:
            self.preferences = preferences

    def add_pet(self, pet: "Pet"):
        """Add a pet to the owner and link it back to the owner."""
        if pet not in self.pets:
            self.pets.append(pet)
        pet.owner = self
        return pet

    def addTask(self, description: str, time: str, frequency: str, pet: Optional["Pet"] = None):
        """Create a task for the owner's first pet when none is specified."""
        if pet is None:
            if not self.pets:
                raise ValueError("No pets available to assign this task.")
            pet = self.pets[0]
        return pet.add_task(description=description, time=time, frequency=frequency)

    def add_task(self, description: str, time: str, frequency: str, pet: Optional["Pet"] = None):
        """Delegate task creation to the main add task method."""
        return self.addTask(description, time, frequency, pet)

    def editTask(self, task: "Task", description: Optional[str] = None,
                 time: Optional[str] = None, frequency: Optional[str] = None):
        """Update an existing task's details when new values are provided."""
        if task is None:
            return None
        if description is not None:
            task.description = description
        if time is not None:
            task.time = time
        if frequency is not None:
            task.frequency = frequency
        return task

    def get_all_tasks(self) -> List["Task"]:
        """Return all tasks assigned to the owner's pets."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def get_tasks_by_pet(self, pet: "Pet") -> List["Task"]:
        """Return the tasks for the specified pet if it belongs to the owner."""
        if pet in self.pets:
            return pet.tasks
        return []


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    owner: Optional[Owner] = None
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, description: str, time: str, frequency: str, completed: bool = False) -> "Task":
        """Create and attach a new task to the pet."""
        task = Task(description=description, time=time, frequency=frequency, completed=completed)
        task.pet = self
        self.tasks.append(task)
        return task

    def displayInfo(self) -> str:
        """Return a short display string describing the pet."""
        return f"{self.name} the {self.breed} {self.species}"

    def updateInfo(self, name: Optional[str] = None, species: Optional[str] = None,
                   breed: Optional[str] = None, age: Optional[int] = None):
        """Update the pet's profile details for any provided values."""
        if name is not None:
            self.name = name
        if species is not None:
            self.species = species
        if breed is not None:
            self.breed = breed
        if age is not None:
            self.age = age


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False
    due_date: Optional[datetime] = None
    pet: Optional["Pet"] = None

    def __post_init__(self):
        """Set an initial due date when one is not provided."""
        if self.due_date is None:
            self.due_date = self._get_initial_due_date()

    def _get_initial_due_date(self) -> datetime:
        """Create an initial due date from the task's time string."""
        current_date = datetime.now().date()
        hour, minute = map(int, self.time.split(":", 1))
        return datetime.combine(current_date, datetime.min.time()).replace(hour=hour, minute=minute)

    def _get_next_due_date(self) -> datetime:
        """Return the next due date for a recurring task based on its frequency."""
        if self.due_date is None:
            return self._get_initial_due_date()
        interval = timedelta(days=1) if self.frequency.lower() == "daily" else timedelta(days=7)
        return self.due_date + interval

    def createTask(self):
        """Return the task instance."""
        return self

    def editTask(self, description: Optional[str] = None, time: Optional[str] = None,
                 frequency: Optional[str] = None):
        """Update the task's description, time, or frequency."""
        if description is not None:
            self.description = description
        if time is not None:
            self.time = time
        if frequency is not None:
            self.frequency = frequency

    def deleteTask(self):
        """Return None to indicate the task is removed."""
        return None

    def mark_complete(self):
        """Mark the task complete and create the next recurring occurrence when applicable."""
        if self.completed:
            return
        self.completed = True
        if self.frequency.lower() in {"daily", "weekly"} and self.pet is not None:
            next_task = self.pet.add_task(
                description=self.description,
                time=self.time,
                frequency=self.frequency,
                completed=False,
            )
            next_task.due_date = self._get_next_due_date()

    def markComplete(self):
        """Alias for marking the task complete."""
        self.mark_complete()


class Scheduler:
    def __init__(self, taskList: Optional[List[Task]] = None, availableTime: int = 0,
                 dailyPlan: Optional[List[Task]] = None):
        """Initialize the scheduler with task and plan state."""
        self.taskList: List[Task] = taskList or []
        self.availableTime = availableTime
        self.dailyPlan: List[Task] = dailyPlan or []

    def generate_schedule(self, owner: Optional[Owner] = None) -> List[Task]:
        """Generate a daily schedule from the owner's tasks."""
        if owner is None:
            self.taskList = []
            self.dailyPlan = []
            return self.dailyPlan

        tasks = owner.get_all_tasks()
        self.taskList = tasks
        self.dailyPlan = tasks
        self.detect_conflicts(tasks)
        return self.dailyPlan

    def generateDailyPlan(self, owner: Optional[Owner] = None) -> List[Task]:
        """Return a daily plan using the owner's tasks."""
        return self.generate_schedule(owner)

    def sort_by_time(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """Return a new list of tasks sorted by their scheduled time value."""
        task_list = tasks if tasks is not None else self.dailyPlan
        return sorted(task_list, key=lambda task: task.time)

    def sortTasks(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """Sort tasks by time, defaulting to the daily plan."""
        task_list = tasks if tasks is not None else self.dailyPlan
        return sorted(task_list, key=lambda task: task.time)

    def filterTasks(self, tasks: Optional[List[Task]] = None, completed: bool = False) -> List[Task]:
        """Filter tasks by completion status, defaulting to the daily plan."""
        task_list = tasks if tasks is not None else self.dailyPlan
        return [task for task in task_list if task.completed is completed]

    def filter_by(self, tasks: Optional[List[Task]] = None, completed: Optional[bool] = None,
                  pet_name: Optional[str] = None) -> List[Task]:
        """Return tasks that match the optional completion and pet-name filters."""
        task_list = tasks if tasks is not None else self.dailyPlan
        filtered_tasks: List[Task] = []
        for task in task_list:
            matches_completion = completed is None or task.completed is completed
            pet_match = True
            if pet_name not in (None, ""):
                pet_attr = getattr(task, "pet", None)
                pet_name_attr = getattr(task, "pet_name", None)
                pet_match = False
                if pet_attr is not None:
                    pet_match = getattr(pet_attr, "name", None) == pet_name
                elif pet_name_attr is not None:
                    pet_match = pet_name_attr == pet_name
            if matches_completion and pet_match:
                filtered_tasks.append(task)
        return filtered_tasks

    def detect_conflicts(self, tasks: Optional[List[Task]] = None) -> List[tuple[Task, Task]]:
        """Scan tasks for identical scheduled times and print a warning for each conflict."""
        task_list = tasks if tasks is not None else self.dailyPlan
        seen_times = {}
        conflicts: List[tuple[Task, Task]] = []

        for task in task_list:
            try:
                time_key = self._parse_time(task.time)
            except ValueError:
                continue

            if time_key in seen_times:
                first_task = seen_times[time_key]
                conflicts.append((first_task, task))
                print(f"Warning: conflicting tasks at {task.time}: {first_task.description} and {task.description}")
            else:
                seen_times[time_key] = task

        return conflicts

    def _parse_time(self, time_value: str) -> int:
        """Convert a HH:MM time string into minutes for simple conflict checks."""
        hour, minute = map(int, time_value.split(":", 1))
        return hour * 60 + minute

    def displayPlan(self) -> List[Task]:
        """Return the current daily plan."""
        return self.dailyPlan
