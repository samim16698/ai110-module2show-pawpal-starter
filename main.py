from pawpal_system import Owner, Pet, Scheduler

owner = Owner("Samiha", "samiha@example.com", "123-456-7890", "Morning reminders")

cat = Pet("Milo", "Cat", "Tabby", 3)
dog = Pet("Luna", "Dog", "Golden Retriever", 5)

owner.add_pet(cat)
owner.add_pet(dog)

cat.add_task("Feed breakfast", "8:00 AM", "Daily")
dog.add_task("Morning walk", "9:00 AM", "Daily")
cat.add_task("Give medication", "7:00 PM", "Daily")

scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)
sorted_schedule = scheduler.sortTasks(schedule)

print("Today's Schedule")
print("----------------")

for task in sorted_schedule:
    print(f"{task.time} - {task.description} ({task.frequency})")