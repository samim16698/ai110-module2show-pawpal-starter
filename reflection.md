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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff in my scheduler is that it currently detects conflicts only when two tasks are scheduled for the exact same time, rather than checking whether their full time ranges overlap. This is a simpler approach because the project only stores a single time string for each task, not a start and end time, so the scheduler does not yet have enough information to reason about durations. This is still a reasonable tradeoff for this project because it gives users a lightweight warning for obvious scheduling conflicts without making the code more complex than necessary. It keeps the feature useful and easy to understand while leaving room to add more detailed overlap detection later if the app grows.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
