import streamlit as st
from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, email="", phoneNumber="", preferences="")

if "pet" not in st.session_state:
    st.session_state.pet = Pet(name=pet_name, species=species, breed="Unknown", age=0)

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_time = st.text_input("Task time (HH:MM)", value="08:00")
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.owner.updateProfile(name=owner_name)

    pet = next((existing_pet for existing_pet in st.session_state.owner.pets if existing_pet.name == pet_name), None)
    if pet is None:
        pet = Pet(name=pet_name, species=species, breed="Unknown", age=0)
        st.session_state.owner.add_pet(pet)
    else:
        pet.updateInfo(name=pet_name, species=species)

    pet.add_task(
        description=task_title,
        time=task_time,
        frequency=priority,
    )
    st.session_state.tasks.append(
        {"title": task_title, "time": task_time, "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.session_state.owner.updateProfile(name=owner_name)

    pet = next((existing_pet for existing_pet in st.session_state.owner.pets if existing_pet.name == pet_name), None)
    if pet is None:
        pet = Pet(name=pet_name, species=species, breed="Unknown", age=0)
        st.session_state.owner.add_pet(pet)
    else:
        pet.updateInfo(name=pet_name, species=species)

    schedule = st.session_state.scheduler.generate_schedule(st.session_state.owner)
    sorted_schedule = st.session_state.scheduler.sort_by_time(schedule)
    conflicts = st.session_state.scheduler.detect_conflicts(sorted_schedule)

    if sorted_schedule:
        st.success("Sorted schedule:")
        for task in sorted_schedule:
            st.write(f"- {task.description} at {task.time} ({task.frequency})")
    else:
        st.info("No tasks available yet.")

    if conflicts:
        st.warning("Some tasks overlap at the same time. Please review the schedule.")
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
