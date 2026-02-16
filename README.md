# IBM Code of Conduct & Ethics Quiz

---

## Introduction

### Organisational Context

IBM is an American‑founded technology company founded in 1911. It is a leading provider of software and services in hybrid cloud, artificial intelligence, and enterprise and strategic consulting services. IBM places a strong emphasis on ethical conduct, compliance, and professional responsibility. To support this, IBM maintains a comprehensive Code of Conduct and a set of ethical guidelines that govern employee behaviour, decision‑making, and interactions with clients, partners, and colleagues.

---

### Project Overview

This project develops an **IBM Code of Conduct & Ethics Quiz**, designed for internal use at IBM. The aim of the application is to provide IBMers with an accessible and interactive way to reinforce their understanding of IBM’s ethical standards, including topics such as conflicts of interest, data confidentiality, responsible use of technology, and reporting unethical behaviour.

The application allows users to answer multiple‑choice questions, receive immediate feedback on their performance, and have results securely stored for review or export. In terms of relevance, by testing knowledge through a structured quiz, the application supports ongoing compliance awareness and helps promote a consistent ethical culture across the organisation.

---

### Technical and Non‑Technical Perspective

From a non‑technical standpoint, the application effectively highlights how software solutions can be used to support ethical considerations, governance, and professional standards within a large enterprise.

From a technical standpoint, the application follows a professional development lifecycle. It is designed, built iteratively, tested, deployed, and documented. The project is developed in **Python** and uses a graphical user interface created via the **Tkinter** library. Additionally, the application incorporates object‑oriented principles, alongside automated testing and continuous integration.





## Design Section

### GUI Design 

The graphical user interface (GUI) has been designed to provide a clear and accessible user experience for IBM employees. It  prioritises simplicity, clarity, and ease of navigation while also maintaining a professional appearance appropriate for an enterprise environment.

Figam GUI Design Link - https://www.figma.com/design/jSgJQLkl1BMuzE6WGKZbGs/Quiz_App?node-id=0-1&p=f&t=8du06XqQwQSVRu5d-0

The application follows a linear user journey consisting of four primary screens:

- **Welcome Screen**
  - Displays application title and welcome message.
  - Provides users with options to start the quiz by entering a username and submitting, or to exit the application via the exit button.

![Welcome Screen](Images/Design_Screens/Welcome_Screen.png)


- **Quiz Screen**

  - Displays a multiple‑choice question follwed by the question number at a time.
  - Uses radio buttons for answer selection.
  - Prevents submission unless an answer is selected.
  - Provides a **Submit** button to confirm the selected answer.
  - Includes a **Next** button that changes the question. Otherwise, it remains inactive until submission.

![Quiz Screen](Images/Design_Screens/Quiz_Screen_Question.png)

**Answer / Feedback**

- Provides immediate visual feedback indicating whether the selected answer is correct or incorrect.
- Ensures feedback is shown before users can continue, reinforcing learning outcomes.

![Answer/Feedback](Images/Design_Screens/Quiz_Screen_Answer.png)


- **Results Screen**

  - Displays the outcome of the completed quiz.
  - Acts as the final stage of the quiz user journey.

  - **Current Results View**
    - Displays the user’s name entered at the start of the quiz.
    - Shows the user’s final score - percentage  of correct answers.
    - Displays the total time taken to complete the quiz.
    - Ensures results are presented in a clear and readable format.
    - Includes a button to access stored quiz results or to exit the application.

    ![Current Result](Images/Design_Screens/Results_Screen.png)

  - **Stored Results View**
    - Displays when the user selects the **Results_File** button.
    - Loads and presents previously stored quiz results from CSV file.
    - Shows historical data such as user names, scores, completion dates and times.
    - Allows users or administrators to review past quiz attempts.

    ![Stored Results ](Images/Design_Screens/Stored_Results.png)



---


### Functional Requirements

- The application must provide a welcome interface that allows users to start the quiz or exit the application.
- The application must allow users to enter their name prior to starting the quiz.
- The application must present ethics‑based multiple‑choice questions related to IBM’s Code of Conduct.
- The application must display one question at a time during the quiz.

- **Question Handling**

  - The system must present a dedicated **Question Screen** where users can select a single answer using radio buttons.
  - The system must prevent users from submitting a question unless an answer has been selected.
  - The system must record the user’s selected answer upon submission.

- **Answer/Feedback**

  - The system must indicate whether the selected answer is correct or incorrect, after submission.
  - The system must display feedback before allowing the user to proceed to the next question.
  - The system must allow users to navigate sequentially through the quiz using a *Next* button.

- **Results Handling**

  - The system must display a **Results Screen** upon quiz completion.
  - The Results Screen must show the user’s name, final score, and total time taken to complete the quiz.
  - The system must store quiz results in persistent storage.
  - The system must provide a *Results File* button to allow users to view previously stored quiz results.
  - The system must load and display past quiz results data when the *Results File* button is selected.

- **Data Management**

  - The system must read quiz questions from a persistent data source, CSV file.
  - The system must handle missing or invalid data without crashing.



---

### Non‑Functional Requirements

- **Performance**
  - The application must load the first quiz question within **1.5 seconds** after the user selects “Start Quiz”.
  - Each screen transition (e.g., Question → Feedback → Next Question) must complete within **500 milliseconds** on a standard workstation (8GB RAM, 2GHz CPU).

- **Usability**
  - All interactive elements (buttons, radio buttons, input fields) must have a minimum size of **40×40 px** to support accessibility and ease of use.
  
  
- **Accessibility**
  - The user interface must use a minimum font size of **12pt** for readability.
  - Buttons and radio buttons must have a minimum interactive size of **32×32 pixels**.
  - Text and background colour contrast must be at least **3:1**.
  - All error or validation messages must be clearly displayed for a minimum of **3 seconds** before navigating away.

- **Reliability**
  - The system must not lose quiz results during a normal session; stored results must persist across restarts.
  - CSV write operations must complete successfully **100% of the time** under normal operating conditions.

- **Data Integrity**
  - Quiz results must be written to the CSV file in **under 200 milliseconds** after quiz completion.
  - Partial or corrupted rows in the results CSV must be skipped gracefully without crashing the application.

- **Security**
  - The application must not store any sensitive personal data beyond the user’s optional display name.
  - The CSV file must contain only: name, score, time taken, and timestamp — no additional fields.

- **Portability**
  - The application must run without modification on Windows, macOS, and Linux systems using **Python 3.10+** and their built‑in Tkinter libraries.

- **Maintainability**
  - Core quiz logic must be separated from the GUI so that at least **80% of logic functions** can be unit‑tested without opening the interface.
  - All classes and functions must contain docstrings following **PEP 257** conventions.

- **Testability**
  - The system must provide at least **10 automated unit tests** with a minimum **75% code coverage** for logic-related modules.
  - All input validation functions must produce consistent outputs. (testable under pytest).



---




### Tech Stack Outline

- **Programming Language: Python**

  - The core language used to develop the quiz application.


- **GUI Framework: Tkinter**

  - Built‑in Python library used to create the graphical interface.
  - Provides buttons, labels, radio buttons, and layout managers needed for the quiz screens.


- **Data Storage: CSV Files**

  - Allows persistent storage that is easy to read or edit.
  - Used to store quiz results and  quiz questions.
  - Supports exporting results.

- **Version Control: Git & GitHub**

  - Git is used for tracking changes and maintaining a clear development history.

- **Testing Framework: pytest**

  - Enables automated testing of core quiz logic and input validation functions.
  - Allows the core quiz logic to be tested independently from the GUI, ensuring that functions like scoring and validation can be tested reliably without opening the Tkinter interface.

- **Continuous Integration: GitHub Actions**

  - Runs automated tests on every commit or pull request.
  - Helps maintain code quality and ensures new updates do not break existing functionality.

### Class Diagram
  - Below is the class diagram : 

  ![Class Diagram](Images/Class_Diagram.png)




