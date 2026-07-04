from dataclasses import dataclass, field
from typing import List, Optional


class User:
    def __init__(self, name: str, email: str, phoneNumber: str, preferences: str):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.preferences = preferences
        self.pets: List["Pet"] = []

    def updateProfile(self):
        pass

    def addTask(self, task: "Task", pet: Optional["Pet"] = None):
        pass

    def editTask(self, task: "Task"):
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    owner: Optional[User] = None
    tasks: List["Task"] = field(default_factory=list)

    def displayInfo(self):
        pass

    def updateInfo(self):
        pass


@dataclass
class Task:
    taskName: str
    taskType: str
    duration: int
    priority: str
    completedStatus: bool = False

    def createTask(self):
        pass

    def editTask(self):
        pass

    def deleteTask(self):
        pass

    def markComplete(self):
        pass


class Planner:
    def __init__(self, taskList: Optional[List[Task]] = None, availableTime: int = 0, dailyPlan: Optional[List[Task]] = None):
        self.taskList: List[Task] = taskList or []
        self.availableTime = availableTime
        self.dailyPlan: List[Task] = dailyPlan or []

    def generateDailyPlan(self):
        pass

    def sortTasks(self):
        pass

    def filterTasks(self):
        pass

    def displayPlan(self):
        pass
