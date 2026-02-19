import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox
# Importing Screen classes : 
from .gui import question_screen, results_screen, stored_results_screen, welcome_screen
# Importing logic classes : 
from .logic import models, quiz, validate
# Importing data class : 
from .data import repository




class App(tk.Tk):
    def __init__(self, questions_path="data/questions.csv", results_path="data/results.csv"):
        super().__init__()

        
        self.title("IBM Code of Conduct & Ethics Quiz")
        self.geometry("900x600")
        self.minsize(760, 480)

        # Shared container for all screens, Instead of creating multiple windows, you just swap out what's inside this container.
        self.container = ttk.Frame(self, padding=10)
        self.container.pack(fill="both", expand=True)

        # Data + logic dependencies:
        self.repo = repository(questions_path, results_path) # Handles loading/saving questions and results from CSV files

        self.quiz: quiz | None = None # hold the Quiz object once the user starts PROBLEM !!!!
        
        self.current_user: str = "" 

        self.show_welcome()



    # --- Navigation helpers ---
    def clear(self):
        """
        Docstring for clear : 

        Function, which clears everything currently in the container 
        
        """
        for widgets in self.container.winfo_children():
            widgets.destroy()

    

    def show_welcome(self):
        """
        Docstring for show_welcome: 
        
        Loads the Welcome screen and puts it in the container. Passing two functions start_quiz_flow() and exit_app() 
        into the Welcome screen so it knows what to do when the user clicks a button. 
        """ 
        self._clear()
        screen = welcome_screen(
            parent=self.container,
            start_callback=self.start_quiz_flow,
            exit_callback=self._exit_app
        )
        screen.pack(fill="both", expand=True)
        screen.focus_default()



    def start_quiz_flow(self, name: str):
        """
        Docstring for start_quiz_flow
        
        :param name: Username
        Save their name

        Load questions from the CSV
        Create a Quiz object with those questions
        Start the quiz 
        Show the first question screen
        
        """
        self.current_user = name.strip()
        questions = self.repo.load_questions()
        if not questions:
            messagebox.showwarning("No questions", "No questions available. Please add questions to continue.")
            return
        self.quiz = quiz(questions=questions)
        self.quiz.start()
        self.show_question()

        

    def show_question(self):
        self._clear()
        assert self.quiz is not None
        q = self.quiz.get_current_question()
        screen = question_screen(
            parent=self.container,
            submit_callback=self._submit_answer_and_feedback,
            next_callback=self._go_next_or_finish
        )
        screen.pack(fill="both", expand=True)
        screen.set_question(q)
        screen.show_question_mode()
        screen.bind_keys()
        screen.focus_default()

    def _submit_answer_and_feedback(self, selected_idx: int):
        assert self.quiz is not None
        self.quiz.submit_answer(selected_idx)
        q = self.quiz.get_current_question()
        # Show feedback (correct vs selected)
        screen = self.container.winfo_children()[0]  # current QuestionScreen
        # call screen method safely
        if hasattr(screen, "show_feedback_mode"):
            screen.show_feedback_mode(correct_index=q.correct_index, selected_index=selected_idx)

    def _go_next_or_finish(self):
        assert self.quiz is not None
        if self.quiz.next_question():
            self.show_question()
        else:
            result = self.quiz.finish(user_name=self.current_user)
            self.show_results(result)

    def show_results(self, result):
        self._clear()
        # persist result
        try:
            self.repo.append_result(result)
        except Exception as ex:
            messagebox.showerror("Save failed", f"Could not save results: {ex}")

        screen = results_screen(
            parent=self.container,
            view_results_callback=self.show_stored_results
        )
        screen.pack(fill="both", expand=True)
        screen.display(result)
        screen.focus_default()

    def show_stored_results(self):
        self._clear()
        results = self.repo.load_results()
        screen = stored_results_screen(
            parent=self.container,
            back_callback=lambda: self.show_results(self.repo.load_results()[-1]) if self.repo.load_results() else self.show_welcome()
        )
        screen.pack(fill="both", expand=True)
        screen.display(results)
        screen.focus_default()

    def _exit_app(self):
        self.destroy()

if __name__ == "__main__":
    App().mainloop()

