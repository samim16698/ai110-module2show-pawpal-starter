from dataclasses import dataclass, field
from typing import List, Optional


class User:
    def __init__(self, name: str, email: str, phoneNumber: str, preferences: str):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.preferences = preferences

    def updateProfile(self):
        pass

    def addTask(self):
        pass

    def editTask(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    owner: Optional[User] = None

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
    def __init__(self, taskList: List[Task], availableTime: int, dailyPlan: List[Task]):
        self.taskList = taskList
        self.availableTime = availableTime
        self.dailyPlan = dailyPlan

    def generateDailyPlan(self):
        pass

    def sortTasks(self):
        pass

    def filterTasks(self):
        pass

    def displayPlan(self):
        pass
