import tkinter as tk
from tkinter import ttk
from typing import Literal
from ..logic.models import Question

class QuestionScreen(tk.Frame):

    """
    QuestionScreen displays a quiz question with multiple choice options.
    
    This screen has two distinct modes:
    - 'question' mode: User can select a multiple choice answer and click Submit
    - 'feedback' mode: Options are locked, feedback (✓/✗) is displayed and Next button is enabled
    
    The screen transitions between these modes based on user actions, providing a smooth
    quiz experience with immediate feedback on answer correctness.
    
    Attributes:
        submit_callback (function): Called when user submits an answer with selected index
        next_callback (function): Called when user clicks Next to go to the next question
        state (str): Current mode - either "question" or "feedback"
        question (Question): The current question object being displayed
        selected (tk.IntVar): Tracks which option the user selected (-1 = none selected)
        _radio_widgets (list): Stores all radio buttons for enabling/disabling
        _option_labels (list): Stores feedback labels (✓/✗) for each option
    """
    def __init__(self, parent, submit_callback, next_callback):
        """
        Initialize the QuestionScreen with UI components and callbacks.
        
        Args:
            parent (tk.Widget): The parent widget that will contain this frame
            submit_callback (function): Function to call when user submits answer (receives index)
            next_callback (function): Function to call when user clicks Next 
        """
        super().__init__(parent)
        self.submit_callback = submit_callback
        self.next_callback = next_callback

        # State management
        self.state: Literal["question", "feedback"] = "question"
        self.question: Question | None = None
        self.selected = tk.IntVar(value=-1)
        self._radio_widgets: list[ttk.Radiobutton] = []
        self._option_labels: list[ttk.Label] = []

        # Layout configuration 
        self.columnconfigure(0, weight=1)

        # Row 0: Question title label
        self.title_lbl = ttk.Label(self, text="Question", font=("Segoe UI", 16, "bold"))
        self.title_lbl.grid(row=0, column=0, pady=(12, 8), sticky="w")

        # Row 1: Question text
        self.q_text = ttk.Label(self, text="", wraplength=800, justify="left")
        self.q_text.grid(row=1, column=0, pady=(0, 12), sticky="w")

        # Row 2: Options container (will be populated dynamically)
        self.options_frame = ttk.Frame(self)
        self.options_frame.grid(row=2, column=0, sticky="w")

        # Row 3: Status message (feedback text)
        self.status_lbl = ttk.Label(self, text="", foreground="#0A66C2")
        self.status_lbl.grid(row=3, column=0, pady=(8, 0), sticky="w")

        # Row 4: Action buttons (Submit or Next)
        self.actions = ttk.Frame(self)
        self.actions.grid(row=4, column=0, pady=(16, 8), sticky="e")
        self.submit_btn = ttk.Button(self.actions, text="Submit", command=self.on_submit)
        self.next_btn = ttk.Button(self.actions, text="Next", command=self.on_next)


    def set_question(self, q: Question):
        """
        Load a new question onto the screen.
        
        This method updates the question text, resets the selection, and renders all
        answer options. 
        
        Args:
            q (Question): The Question object containing text and multiple choice options
        """
        self.question = q
        self.title_lbl.config(text=f"Question")
        self.q_text.config(text=q.text)
        self.selected.set(-1)  # Reset selection to nothing
        self._render_options(q.options)

    def show_question_mode(self):
        """
        Switch to question mode, allowing user to select and submit an answer.
        
        In this mode:
        - Radio buttons are enabled and clickable
        - Status label is cleared
        - Submit button is visible
        - Next button is hidden
        """
        self.state = "question"
        self.lock_inputs(False)
        self.status_lbl.config(text="")
        self.submit_btn.grid(row=0, column=0, padx=4)
        self.next_btn.grid_forget()

    def show_feedback_mode(self, correct_index: int, selected_index: int):
        """
        Switch to feedback mode, showing whether the answer was correct.
        
        In this mode:
        - Radio buttons are disabled (user cannot change selection)
        - ✓ appears next to correct answer(s)
        - ✗ appears next to user's incorrect selection (if wrong)
        - Status message indicates if answer was Correct or Incorrect
        - Submit button is hidden
        - Next button is visible for progression
        
        Args:
            correct_index (int): Index of the correct answer option
            selected_index (int): Index of the option user selected
        """
        self.state = "feedback"
        self.lock_inputs(True)
        
        # Display feedback symbols for each option
        for i, lbl in enumerate(self._option_labels):
            if i == selected_index == correct_index:
                # User selected the correct answer
                lbl.config(text="✓", foreground="green")
            elif i == selected_index and selected_index != correct_index:
                # # User selected the wrong answer
                lbl.config(text="✗", foreground="red")
            elif i == correct_index:
                # The correct answer (show even if user was wrong)
                lbl.config(text="✓", foreground="green")
            else:
                # Other options get no marking
                lbl.config(text="")
        
        # Display overall feedback message
        self.status_lbl.config(
            text=("Correct!" if selected_index == correct_index else "Incorrect. Review the correct answer above.")
        )
        self.submit_btn.grid_forget()
        self.next_btn.grid(row=0, column=0, padx=4)

    def lock_inputs(self, locked: bool):
        """
        Enable or disable all radio button options.
        
        Args:
            locked (bool): If True, disables all radio buttons. If False, enables them.
        """
        for rb in self._radio_widgets:
            rb.config(state="disabled" if locked else "normal")

    def get_selection(self) -> int | None:
        """
        Retrieve the currently selected option index.
        
        Returns:
            int: The index of the selected option, or None if nothing is selected
        """
        val = self.selected.get()
        return val if val >= 0 else None

    # Events
    def on_submit(self):
        """
        Handles the Submit button click event.
        
        Validates that user has actually selected an answer. If valid, calls the submit_callback
        with the selected index. If not, displays an error message and focuses the
        first option to guide the user.
        """
        sel = self.get_selection()
        if sel is None:
            self.status_lbl.config(text="Please select an answer before submitting.")
            if self._radio_widgets:
                self._radio_widgets[0].focus_set()
            return
        self.submit_callback(sel)

    def on_next(self):
        """
        Handle the Next button click event.
        
        Called when user is in feedback mode and ready to proceed to the next question.
        Triggers the next_callback to advance the quiz.
        """
        self.next_callback()

    # Widgets Rendering  
    def _render_options(self, options: list[str]):
        """
        Dynamically create radio buttons for each answer option.
        
        This method:
        1. Clears any previously rendered options
        2. Creates a radio button for each option text
        3. Creates a placeholder label next to each button for feedback symbols (✓/✗)
        4. Stores references to both for later use (locking, feedback display)
        
        Args:
            options (list[str]): List of answer option texts to display
        """
        # Clear previous options
        for w in self.options_frame.winfo_children():
            w.destroy()
        self._radio_widgets.clear()
        self._option_labels.clear()

        # Create UI for each option
        for i, opt in enumerate(options):
            # Create a frame to hold the radio button and feedback label side by side
            row = ttk.Frame(self.options_frame)
            row.pack(anchor="w", pady=2)
            
            # Create the radio button for this option
            rb = ttk.Radiobutton(row, text=opt, value=i, variable=self.selected)
            rb.pack(side="left")
            
            # Create placeholder label for feedback (✓ or ✗ will appear here)
            fb = ttk.Label(row, width=2)
            fb.pack(side="left", padx=(8, 0))
            
            # Store references for later use
            self._radio_widgets.append(rb)
            self._option_labels.append(fb)