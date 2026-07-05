from pawpal_system import Owner, Pet, Scheduler

owner = Owner("Samiha", "samiha@example.com", "123-456-7890", "Morning reminders")

cat = Pet("Milo", "Cat", "Tabby", 3)
dog = Pet("Luna", "Dog", "Golden Retriever", 5)

owner.add_pet(cat)
owner.add_pet(dog)

cat.add_task("Feed Milo", "18:00", "Daily")
dog.add_task("Walk Luna", "08:00", "Daily")
cat.add_task("Play with Milo", "12:00", "Daily")
dog.add_task("Bath Luna", "16:00", "Daily")

scheduler = Scheduler()
all_tasks = owner.get_all_tasks()

sorted_tasks = scheduler.sort_by_time(all_tasks)
filtered_tasks = scheduler.filter_by(sorted_tasks, completed=False)

print("Sorted tasks:")
for task in sorted_tasks:
    print(f"- {task.description} at {task.time}")

print("\nFiltered tasks:")
for task in filtered_tasks:
    print(f"- {task.description} at {task.time}")