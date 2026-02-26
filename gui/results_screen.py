from tkinter import ttk

class ResultsScreen(ttk.Frame):

    """
    ResultsScreen displays the final quiz results to the user.
    
    This screen is displayed after the user completes the quiz, it shows:
    - User's name (or a dash if no name was entered)
    - Final score (correct answers out of total questions)
    - Time taken to complete the quiz
    - A button to view all previous quiz attempts
    
    Attributes:
        view_results_callback (function): Callback function to view historical results
        name_lbl (ttk.Label): Label displaying the user's name
        score_lbl (ttk.Label): Label displaying the quiz score
        time_lbl (ttk.Label): Label displaying the time taken
    """
     
    def __init__(self, parent, view_results_callback):
        """
        Initialises the ResultsScreen with result display labels and navigation button.
        
        Args:
            parent (tk.Widget): The parent widget that will contain this frame
            view_results_callback (function): Callback function triggered when user clicks
                                             the "View Previous Results" button
        """
        super().__init__(parent)
        self.view_results_callback = view_results_callback

        self.columnconfigure(0, weight=1)
        ttk.Label(self, text="Results", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, pady=(16, 8), sticky="w")

        self.name_lbl = ttk.Label(self, text="")
        self.score_lbl = ttk.Label(self, text="")
        self.time_lbl = ttk.Label(self, text="")
        self.name_lbl.grid(row=1, column=0, sticky="w")
        self.score_lbl.grid(row=2, column=0, sticky="w")
        self.time_lbl.grid(row=3, column=0, sticky="w")

        actions = ttk.Frame(self)
        actions.grid(row=4, column=0, pady=(12, 0), sticky="w")
        ttk.Button(actions, text="Results File (View Previous Results)", command=self.on_view_results).grid(row=0, column=0, padx=4)

    def display(self, result):
        """
        Populate the result labels with actual quiz results.
        
        This method takes a Result object and updates the three labels to show:
        - User's name (or '—' if no name was provided)
        - Final score in format: correct answers / total questions
        - Time taken in seconds
        
        Args:
            result (Result): A Result object containing user_name, score, 
                           total_questions, and time_taken attributes
        
        """
        self.name_lbl.config(text=f"Name: {result.user_name or '—'}")
        self.score_lbl.config(text=f"Score: {result.score}/{result.total_questions}")
        # Convert seconds to minutes and seconds
        minutes = int(result.time_taken // 60)
        seconds = int(result.time_taken % 60)
        self.time_lbl.config(text=f"Time taken: {minutes}m {seconds}s")

    def on_view_results(self):
        """
        Handle the "View Previous Results" button click event.
        
        Triggers the view_results_callback, which navigates to the StoredResultsScreen
        to display all previous quiz attempts and their scores.
        """
        self.view_results_callback()

    def focus_default(self):
        """
        Set keyboard focus to the "View Previous Results" button.
        
        This allows users to navigate and interact with the button using the keyboard
        without needing to use the mouse.
        """
        # Focuses on the View Results button
        self.nametowidget(self.children[list(self.children.keys())[-1]]).focus_set()






