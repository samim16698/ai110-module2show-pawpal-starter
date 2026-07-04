from dataclasses import dataclass, field
from typing import List, Optional


class Owner:
    def __init__(self, name: str, email: str, phoneNumber: str, preferences: str):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.preferences = preferences
        self.pets: List["Pet"] = []

    def updateProfile(self, name: Optional[str] = None, email: Optional[str] = None,
                      phoneNumber: Optional[str] = None, preferences: Optional[str] = None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if phoneNumber is not None:
            self.phoneNumber = phoneNumber
        if preferences is not None:
            self.preferences = preferences

    def add_pet(self, pet: "Pet"):
        if pet not in self.pets:
            self.pets.append(pet)
        pet.owner = self
        return pet

    def addTask(self, description: str, time: str, frequency: str, pet: Optional["Pet"] = None):
        if pet is None:
            if not self.pets:
                raise ValueError("No pets available to assign this task.")
            pet = self.pets[0]
        return pet.add_task(description=description, time=time, frequency=frequency)

    def add_task(self, description: str, time: str, frequency: str, pet: Optional["Pet"] = None):
        return self.addTask(description, time, frequency, pet)

    def editTask(self, task: "Task", description: Optional[str] = None,
                 time: Optional[str] = None, frequency: Optional[str] = None):
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
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def get_tasks_by_pet(self, pet: "Pet") -> List["Task"]:
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
        task = Task(description=description, time=time, frequency=frequency, completed=completed)
        self.tasks.append(task)
        return task

    def displayInfo(self) -> str:
        return f"{self.name} the {self.breed} {self.species}"

    def updateInfo(self, name: Optional[str] = None, species: Optional[str] = None,
                   breed: Optional[str] = None, age: Optional[int] = None):
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

    def createTask(self):
        return self

    def editTask(self, description: Optional[str] = None, time: Optional[str] = None,
                 frequency: Optional[str] = None):
        if description is not None:
            self.description = description
        if time is not None:
            self.time = time
        if frequency is not None:
            self.frequency = frequency

    def deleteTask(self):
        return None

    def mark_complete(self):
        self.completed = True

    def markComplete(self):
        self.mark_complete()


class Scheduler:
    def __init__(self, taskList: Optional[List[Task]] = None, availableTime: int = 0,
                 dailyPlan: Optional[List[Task]] = None):
        self.taskList: List[Task] = taskList or []
        self.availableTime = availableTime
        self.dailyPlan: List[Task] = dailyPlan or []

    def generate_schedule(self, owner: Optional[Owner] = None) -> List[Task]:
        if owner is None:
            self.taskList = []
            self.dailyPlan = []
            return self.dailyPlan

        tasks = owner.get_all_tasks()
        self.taskList = tasks
        self.dailyPlan = tasks
        return self.dailyPlan

    def generateDailyPlan(self, owner: Optional[Owner] = None) -> List[Task]:
        return self.generate_schedule(owner)

    def sortTasks(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        task_list = tasks if tasks is not None else self.dailyPlan
        return sorted(task_list, key=lambda task: task.time)

    def filterTasks(self, tasks: Optional[List[Task]] = None, completed: bool = False) -> List[Task]:
        task_list = tasks if tasks is not None else self.dailyPlan
        return [task for task in task_list if task.completed is completed]

    def displayPlan(self) -> List[Task]:
        return self.dailyPlan
