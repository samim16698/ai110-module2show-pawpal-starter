# PawPal+ Project Reflection

## 1. System Design

Three core actions that a user should be able to perform are:
    - enter owner and pet info (especially basic info)
    - generate a schedule for a pet
    - add/edit tasks

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Answer: MY UML design includes four classes such as: user, pet, task and planner. The user represents the pet owner and basic information like name, email, phone number and user preferences. The pet class represents each pet being booked and stores information such as name, breed, age and owner. The task class represents activities such as feeding, walking or grooming and tracks duration and priority of these tasks. While the planner class deals with organizing tasks, sorting and generating a daily plan for the user. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

--- Updated the skeleton in pawpal_system.py to reflect the UML relationships more clearly:

- Added a pets collection to User for the “User has Pets” relationship.
- Added a tasks collection to Pet for the “Pet has Tasks” relationship.
- Made Planner’s task-related fields more flexible with default empty 

This keeps the file as a class skeleton while making the relationships explicit.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers the scheduled time of each task and organizes tasks in chronological order. It also considers task priority and detects when two tasks are scheduled at the same time so the user can resolve conflicts. These constraints were the most important because they help create a clear and practical daily schedule while keeping the scheduling logic simple and easy to maintain.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff in my scheduler is that it currently detects conflicts only when two tasks are scheduled for the exact same time, rather than checking whether their full time ranges overlap. This is a simpler approach because the project only stores a single time string for each task, not a start and end time, so the scheduler does not yet have enough information to reason about durations. This is still a reasonable tradeoff for this project because it gives users a lightweight warning for obvious scheduling conflicts without making the code more complex than necessary. It keeps the feature useful and easy to understand while leaving room to add more detailed overlap detection later if the app grows.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help brainstorm my initial system design, generate class skeletons, improve my UML diagram, create test cases, debug failing tests, and update the Streamlit interface. The most helpful prompts were asking the AI to explain errors, suggest test cases, and update the UML so it matched my final implementation.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

--- I did not automatically accept every AI suggestion. Before keeping code changes, I reviewed them to make sure they matched the assignment instructions and only modified the requested files. I also verified the suggestions by running the application, using pytest, and checking that the tests passed before accepting the changes.

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task sorting, task filtering, recurring task behavior, conflict detection, and schedule generation. These tests were important because they verified that the scheduler organized tasks correctly, handled recurring tasks as expected, warned about scheduling conflicts, and generated a valid daily schedule without errors.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

--- : I am confident that the scheduler works correctly because the automated tests passed successfully and the application behaved as expected during manual testing. If I had more time, I would test additional edge cases such as empty task lists, invalid time formats, multiple pets with many overlapping tasks, and more complex recurring schedules.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

am most satisfied with successfully connecting the backend scheduling logic to the Streamlit interface. It was rewarding to see the application generate schedules, display conflict warnings, and pass all automated tests. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had more time, I would make the scheduler better at handling task times and overlapping tasks. I would also improve the app layout so it is easier to add pets, add tasks, and view the schedule.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is that planning the classes first makes the code easier to build later. I also learned that AI is helpful for suggestions and debugging, but I still need to review and test the code myself.
