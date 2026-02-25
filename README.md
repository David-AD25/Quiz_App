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
    - Shows the user’s final score in the format :  number of correct answers/ total number of questions. E.g 8/10
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
  - All controls must be fully keyboard-operable

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

--- 
### Class Diagram
  - Below is the class diagram : 

  ![Class Diagram](Images/Class_Diagram.png)



## Development 

  ### GUI Layer

   ### Welcome Screen 
   - WelcomeScreen is the initial GUI screen displayed when the application starts.

   ``` python
    class WelcomeScreen(tk.Frame):
    def __init__(self, parent, start_callback, exit_callback):
        super().__init__(parent, bg='#D3AF37')
        self.start_callback = start_callback
        self.exit_callback = exit_callback

   ```

  - Class Inheritance & Initialisation - Inheriting from tk.Frame makes the screen a self-contained, reusable component. Storing callbacks as instance variables is crucial for communication between the UI and application logic, allowing the screen to respond to user actions.

  ``` python
      self.grid_columnconfigure(0, weight=1)
  ```
  - This configures the layout of the screen. 

  
  ``` python
      ttk.Button(btns, text="Start Quiz", command=self.on_start).grid(row=0, column=0, padx=6)
  ```
  - The command=self.on_start parameter connects the button click to an event handler. Without this, clicking the button does nothing and no communication occurs with the rest of the application.

  ``` python
      def on_start(self):
    name = self.name_var.get().strip()
    self.start_callback(name)
  ```
  - This method retrieves user input and passes it to the main controller via the callback. It's the critical "exit point" where the welcome screen transitions to the quiz. 

  ``` python 
  try:
    logo_image = PhotoImage(file=logo_path)
  except tk.TclError as e:
    print(f"Error loading logo: {e}")
  ```
  - This error handling prevents the application from crashing if the image file is missing or corrupted, it demonstrates proffesional programming and makes the program robust. 

  ---
### Question Screen 
- Displays a quiz question with multiple choice options and supports two distinct modes: question mode where users select answers, and feedback mode where answers are revealed.

``` python
class QuestionScreen(tk.Frame):
    def __init__(self, parent, submit_callback, next_callback):
        super().__init__(parent)
        self.submit_callback = submit_callback
        self.next_callback = next_callback
        self.state: Literal["question", "feedback"] = "question"
        self.selected = tk.IntVar(value=-1)
```
- Class Inheritance & Initialisation - Inheriting from tk.Frame makes the screen a self-contained, reusable component that manages both the question display and answer collection. Storing callbacks as instance variables (submit_callback and next_callback) allows for communication between the UI and the main application controller. The state variable tracks which mode the screen is in, and selected tracks which option the user picked. 


``` python 
def set_question(self, q: Question):
    self.question = q
    self.q_text.config(text=q.text)
    self.selected.set(-1)
    self._render_options(q.options)
```

- This method loads a new question onto the screen by updating the question text and rendering all answer options. It resets the selection to -1 (nothing selected) to ensure users start fresh with each new question.


``` python
def show_question_mode(self):
    self.state = "question"
    self.lock_inputs(False)
    self.status_lbl.config(text="")
    self.submit_btn.grid(row=0, column=0, padx=4)
    self.next_btn.grid_forget()
```

- This method switches the screen to question mode by unlocking radio buttons, clearing status messages, and showing the Submit button while hiding the Next button. This mode allows users to freely select and change their answer before submitting.


``` python
def show_feedback_mode(self, correct_index: int, selected_index: int):
    self.state = "feedback"
    self.lock_inputs(True)
    for i, lbl in enumerate(self._option_labels):
        if i == selected_index == correct_index:
            lbl.config(text="✓", foreground="green")
        elif i == selected_index and selected_index != correct_index:
            lbl.config(text="✗", foreground="red")
        elif i == correct_index:
            lbl.config(text="✓", foreground="green")

```
- This method switches to feedback mode by locking the radio buttons and displaying visual feedback symbols. A green checkmark (✓) appears next to the correct answer, and a red X (✗) appears next to the user's answer if it was wrong. 


``` python

def lock_inputs(self, locked: bool):
    for rb in self._radio_widgets:
        rb.config(state="disabled" if locked else "normal")
```
- This method enables or disables all radio buttons based on the locked parameter.

``` python
# Input validation
def on_submit(self):
    sel = self.get_selection()
    if sel is None:
        self.status_lbl.config(text="Please select an answer before submitting.")
        if self._radio_widgets:
            self._radio_widgets[0].focus_set()
        return
    self.submit_callback(sel)
```
- This method validates that the user has actually selected an answer before allowing submission. If no answer is selected, it displays an error message and focuses the first option to guide the user. If valid, it calls the submit callback to pass the selected index to the main controller, demonstrating proper error handling and user guidance.


``` python
def _render_options(self, options: list[str]):
    for w in self.options_frame.winfo_children():
        w.destroy()
    self._radio_widgets.clear()
    self._option_labels.clear()
    
    for i, opt in enumerate(options):
        row = ttk.Frame(self.options_frame)
        row.pack(anchor="w", pady=2)
        rb = ttk.Radiobutton(row, text=opt, value=i, variable=self.selected)
        rb.pack(side="left")
        fb = ttk.Label(row, width=2)
        fb.pack(side="left", padx=(8, 0))
        self._radio_widgets.append(rb)
        self._option_labels.append(fb)
```
- This method creates radio buttons for each answer option. It first clears any previously rendered options, then creates a row for each option containing both a radio button and a placeholder label for feedback symbols.

---
### Results Screen 
-  ResultsScreen displays the final quiz results to the user after completing the quiz. It shows the user's name, final score, and time taken, along with a button to view all previous quiz attempts.

``` python 
class ResultsScreen(ttk.Frame):
    def __init__(self, parent, view_results_callback):
        super().__init__(parent)
        self.view_results_callback = view_results_callback
        
        self.name_lbl = ttk.Label(self, text="")
        self.score_lbl = ttk.Label(self, text="")
        self.time_lbl = ttk.Label(self, text="")

```

- Inheriting from ttk.Frame makes the results screen a self-contained and reusable component. Storing view_results_callback as an instance variable allows the screen to communicate with the main controller when the user wants to view past results. Three empty labels (name_lbl, score_lbl, time_lbl) are created to hold the result information, which will be populated after the quiz completes.

``` python 
def display(self, result):
    self.name_lbl.config(text=f"Name: {result.user_name or '—'}")
    self.score_lbl.config(text=f"Score: {result.score}/{result.total_questions}")
    self.time_lbl.config(text=f"Time taken: {result.time_taken}s")
```

- This method takes a Result object and populates the three labels with the actual quiz results. It displays the user's name, the final score  and the time taken in seconds. This separation of data and display allows the screen to be reusable for different quiz results without needing to recreate the UI.

``` python 
actions = ttk.Frame(self)
actions.grid(row=4, column=0, pady=(12, 0), sticky="w")
ttk.Button(actions, text="Results File (View Previous Results)", command=self.on_view_results).grid(row=0, column=0, padx=4)
```

- Creates a container frame (actions) to hold View Previous Results button. The command=self.on_view_results parameter connects the button to an event handler. Using a container frame makes the code more reusable, and easier to add new features to the system at a later date. 

``` python
def on_view_results(self):
    self.view_results_callback()
```

- This event handler calls the view_results_callback when the user clicks the "View Previous Results" button, allowing the screen to trigger navigation to the stored results.

---
### stored Results Screen 

- StoredResultsScreen displays all past quiz attempts in a table format, allowing users to review their past performance with key metrics including name, score, date/time, and time taken to complete the quiz.


``` python 
self.table = ttk.Treeview(
    self, 
    columns=("name", "score", "timestamp", "time_taken"), 
    show="headings", 
    height=12
)

```

- I used Tkinter's Treeview widget with four columns to display results in a clean, organized table format. The Treeview is ideal for displaying structured data because it supports multiple columns and sorting capabilities. The height=12 parameter allows 12 rows to be visible at once, this provides an efficient way to display a results without overwhelming the user interface.


``` python 
for col, text in (("name", "Name"), ("score", "Score"), ("timestamp", "Date & Time"), 
                 ("time_taken", "Time Taken")):
    self.table.heading(col, text=text)
    self.table.column(col, width=150, anchor="w")

```
- This loop creates four columns for the table. For each column, it does two things: (1) sets the heading text that appears at the top (like "Name", "Score", "Date & Time", "Time Taken"), and (2) configures the column width to 150 pixels and aligns the text to the left.

``` python 

def display(self, results):
    for r in results:
        # Convert seconds to minutes and seconds 
        minutes = r.time_taken // 60
        seconds = r.time_taken % 60
        time_formatted = f"{minutes}m {seconds}s"
        
        self.table.insert(
            "", 
            "end", 
            values=(
                r.user_name or "—",
                f"{r.score}/{r.total_questions}",
                r.timestamp,
                time_formatted
            )
        )

```

-  This method populates a table with all previous quiz attempts by iterating through a list of Result objects. Each result is inserted as a row showing the user's name  score in "correct/total" format, the full date and time of the quiz, and the time taken converted from seconds to a readable "Xm Ys" format. The time conversion uses integer division (//) to get minutes and the modulo operator (%) to get remaining seconds. 



``` python 

def on_exit(self):
    self.exit_callback()

 ```
- This method allows users to close the application and complete their session after reviewing past results.


``` python 

def focus_default(self):
    self.table.focus_set()
``` 

-  Allows users to navigate through rows using arrow keys without requiring a mouse click

--- 
### Logic Layer

**Models**

This module contains the core data classes used throughout the application:
- Question: Represents a single quiz question with options and correct answer
- Result: Represents the outcome of a completed quiz attempt

--- 
#### **Question Class - Data Structure for Quiz Questions**
``` python 
@dataclass(frozen=True)
class Question:
    id: str
    text: str
    options: List[str]
    correct_index: int
``` 
- **@dataclass(frozen=True)** decorator automatically creates a class for storing data while making it immutable (cannot be changed after creation). This ensures questions remain exactly as they are once loaded from the CSV file. The frozen property prevents accidental modifications and protects data integrity. 

``` python 
# Validation
def is_valid(self) -> bool:
    return bool(self.text.strip()) and len(self.options) >= 2 and 0 <= self.correct_index < len(self.options)
``` 
- **The is_valid()** method checks three  conditions: (1) the question text is not empty, (2) there are at least 2 answer options, and (3) the correct answer index is within bounds. This validation catches data errors before the quiz starts, preventing crashes or undefined behavior during gameplay. 

---
#### **Result Class - Data Structure for Quiz Results**

```python
@dataclass(frozen=True)
class Result:
    user_name: Optional[str]
    score: int
    total_questions: int
    time_taken: float
    timestamp: str
```

- **Immutable Result Storage** - Similar to Question, Result uses `@dataclass(frozen=True)` to create an immutable record of how a user performed on the quiz. This ensures results cannot be accidentally modified after being created, maintaining historical accuracy and preventing data corruption.

```python
def to_dict(self) -> dict:
    return {
        "user_name": self.user_name or "",
        "score": self.score,
        "total_questions": self.total_questions,
        "time_taken": self.time_taken,
        "timestamp": self.timestamp,
    }
```

- **Converting to Dictionary Format** - The `to_dict()` method converts the Result object into a dictionary, making it easy to save to CSV files or JSON. The `self.user_name or ""` handles the case where a user didn't enter their name by converting None to an empty string, ensuring consistent data when persisting to files.

---
### Quiz Logic - The Quiz class manages the entire quiz flow, tracking questions, answers, timing, and score calculation.



#### **Starting the Quiz**

```python
def start(self):
    self.current_index = 0
    self.user_answers = [None] * len(self.questions)
    self.start_time = time.time()
    self.end_time = None
    self.is_active = True
```

- **Initialize Quiz State** - Resets the quiz to the beginning by clearing previous answers, setting the current question to 0, and recording the exact start time using `time.time()`. The `is_active = True` flag indicates the quiz is running. This method is called when the user clicks "Start Quiz" on the welcome screen.

---

#### **Getting and Submitting Answers**

```python
def get_current_question(self) :
    return self.questions[self.current_index]

def submit_answer(self, selected_index: int):
    self.user_answers[self.current_index] = selected_index
```

- **Current Question & Answer Recording** - `get_current_question()` returns the question the user is currently viewing by using `current_index` as an array index. `submit_answer()` stores which option the user selected in the `user_answers` array at the same index position. This parallel array structure keeps answers aligned with their questions.

---

#### **Navigation Through Questions**

```python
def next_question(self) -> bool:
    if self.current_index + 1 < len(self.questions):
        self.current_index += 1
        return True
    return False
```

- **Question Navigation** - Checks if there are more questions remaining before advancing. Returns `True` if successful (move to next question), or `False` if at the last question (quiz should end). The conditional `self.current_index + 1 < len(self.questions)` prevents moving past the final question.

---

#### **Score Calculation**

```python
def calculate_score(self) -> int:
    score = 0
    for ans, q in zip(self.user_answers, self.questions):
        if ans is not None and ans == q.correct_index:
            score += 1
    return score
```

- **Comparing Answers with Correct Answers** - Loops through user answers paired with their corresponding questions using `zip()`. For each answer, checks if it matches the question's `correct_index`. The `ans is not None` condition handles skipped questions. Returns the total count of correct answers.

---

#### **Finishing the Quiz and Creating Results**

```python
def finish(self, user_name: str | None):
    self.end_time = time.time()
    self.is_active = False
    time_taken = round(self.end_time - (self.start_time or self.end_time), 2)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return Result(
        user_name=user_name,
        score=self.calculate_score(),
        total_questions=len(self.questions),
        time_taken=time_taken,
        timestamp=ts
    )
```

- **Quiz Completion and Result Generation** - Records the end time and calculates elapsed time by subtracting `start_time` from `end_time` (in seconds). Creates a UTC timestamp for when the quiz was completed. Packages all data into a Result object: user's name, calculated score, total questions, time taken (in seconds, raw format), and timestamp. This Result object is then passed to the results display screens.

---

#### **The Quiz Flow**

```
1. start() → Record time, reset answers, set is_active = True
2. Loop:
   - get_current_question() → Display question
   - User selects answer
   - submit_answer() → Record selection
   - next_question() → Move to next (returns True) or end (returns False)
3. finish() → Calculate score, record end time, return Result
```

## Validation logic 

**Validation Module** - Pure utility functions for validating user input and formatting time data.


#### **Validating User Answer Selection**

```python
def validate_selected_answer(idx: int | None, num_options: int) -> bool:
    return idx is not None and 0 <= idx < num_options
```

- **Checking Valid Selection** - Ensures the user actually selected an answer and that the selection is within valid bounds. The function checks two conditions: (1) `idx is not None` confirms a selection was made (not empty), and (2) `0 <= idx < num_options` ensures the index points to an actual option. This prevents crashes from out-of-range indices. 
---

#### **Checking Answer Correctness**

```python
def check_answer(selected: int, correct: int) -> bool:
    return selected == correct
```

- **Answer Comparison** - Compares the user's selected answer index directly with the correct answer index.

---

#### **Formatting Time for Display**

```python
def format_time(seconds: float) -> str:
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"
```

- **Converting Seconds to Readable Format** - Transforms raw seconds into a human-readable time string (MM:SS if under 1 hour, or HH:MM:SS if 1+ hours). The `divmod()` function efficiently splits time into components: `divmod(seconds, 60)` extracts minutes and remaining seconds, then `divmod(minutes, 60)` extracts hours and remaining minutes. The format specifier `{h:02d}` adds leading zeros (e.g., "04:05" instead of "4:5"). The conditional `if h` omits hours from display when they're zero, keeping short quiz times compact (e.g., "02:15" instead of "00:02:15").

---

#### **Summary**

These validation functions are **stateless utilities** used throughout the application: answer validation before submission prevents errors, answer checking determines correctness for feedback, and time formatting displays quiz duration in a user-friendly format.

## CSV Repository
**CSV Repository** - Handles all file I/O operations for loading quiz questions and saving/loading quiz results from CSV files.



#### **Loading Questions from CSV**

```python
def load_questions(self):
    choices = row["choices"].split(self.field_sep) if row.get("choices") else []
    q = Question(
        id=row.get("id", ""),
        text=row.get("text", ""),
        options=[c for c in choices if c],
        correct_index=int(row.get("correct_index", -1)),
        category=row.get("category") or None,
        difficulty=row.get("difficulty") or None,
    )
    if q.is_valid():
        questions.append(q)
```

- **Reading and Validating Questions** - Opens the questions CSV file and reads each row as a dictionary using `csv.DictReader`. For each row, it splits the choices field using the custom separator (default "||") to extract individual answer options. Creates a Question object and validates it using `is_valid()` before adding to the list. Invalid or malformed rows are skipped silently. Returns an empty list if the file doesn't exist, allowing the app to start even without questions.

---

#### **Saving Quiz Results**

```python
def append_result(self, r: Result):
    try:
        with open(self.results_path, "x", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[...])
            writer.writeheader()
    except FileExistsError:
        pass
    with open(self.results_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[...])
        writer.writerow(r.to_dict())
```

- **Smart File Creation and Appending** - Uses two-step approach: first tries to create the file with headers using mode "x" (exclusive creation), and if the file already exists, catches the exception and skips header creation. Then appends the result using mode "a" (append). This ensures headers are written exactly once while allowing multiple results to be added over time. Converts the Result object to a dictionary using `to_dict()` for CSV writing.

---

#### **Loading Historical Results**

```python
def load_results(self):
    results.append(
        Result(
            user_name=row.get("user_name") or None,
            score=int(row.get("score", 0)),
            total_questions=int(row.get("total_questions", 0)),
            time_taken=float(row.get("time_taken", 0.0)),
            timestamp=row.get("timestamp") or "",
        )
    )
```

- **Reconstructing Results from CSV** - Reads the results CSV file and converts each row back into a Result object. Handles type conversions: converts score and total_questions to integers, time_taken to float, and treats empty user_name as None. Malformed rows are skipped to prevent crashes. Returns an empty list if the file doesn't exist, allowing the stored results screen to display gracefully even with no history.



