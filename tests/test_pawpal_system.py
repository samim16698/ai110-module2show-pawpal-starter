import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_can_be_marked_complete():
    task = Task(description="Feed Bella", time="08:00", frequency="Daily")

    task.mark_complete()

    assert task.completed is True


def test_pet_can_store_and_list_tasks():
    pet = Pet(name="Bella", species="Dog", breed="Labrador", age=3)

    pet.add_task(description="Walk", time="18:00", frequency="Daily")

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Walk"


def test_owner_can_access_all_tasks_across_pets():
    owner = Owner(name="Mina", email="mina@example.com", phoneNumber="123", preferences="quiet")
    pet1 = Pet(name="Bella", species="Dog", breed="Labrador", age=3)
    pet2 = Pet(name="Milo", species="Cat", breed="Siamese", age=2)

    owner.add_pet(pet1)
    owner.add_pet(pet2)
    pet1.add_task(description="Feed", time="08:00", frequency="Daily")
    pet2.add_task(description="Play", time="17:00", frequency="Daily")

    all_tasks = owner.get_all_tasks()

    assert len(all_tasks) == 2
    assert [task.description for task in all_tasks] == ["Feed", "Play"]


def test_scheduler_can_generate_schedule_from_owner():
    owner = Owner(name="Mina", email="mina@example.com", phoneNumber="123", preferences="quiet")
    pet = Pet(name="Bella", species="Dog", breed="Labrador", age=3)
    owner.add_pet(pet)
    pet.add_task(description="Feed", time="08:00", frequency="Daily")
    pet.add_task(description="Walk", time="18:00", frequency="Daily")

    scheduler = Scheduler()
    schedule = scheduler.generate_schedule(owner)

    assert [task.description for task in schedule] == ["Feed", "Walk"]
