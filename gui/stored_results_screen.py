import tkinter as tk
from tkinter import ttk



class StoredResultsScreen(ttk.Frame):
    """
    StoredResultsScreen displays all historical quiz attempts in a simplified table format.
    
    Columns:
    - Name
    - Score (e.g., 8/10)
    - Date & Time (e.g., 2024-02-20 14:30)
    - Time Taken in seconds (e.g., 245s)
    """
    
    def __init__(self, parent, exit_callback):
        """
        Initialize the StoredResultsScreen with a table for displaying past results.
        
        Args:
            parent (tk.Widget): The parent widget that will contain this frame
            exit_callback (function): Callback function triggered when user clicks the Exit button
        """
        super().__init__(parent)
        self.exit_callback = exit_callback
        
        # Configure layout 
        self.columnconfigure(0, weight=1)
    
        ttk.Label(self, text="Stored Results", font=("Segoe UI", 18, "bold")).grid(
            row=0, column=0, pady=(16, 8), sticky="w"
        )
        
        # Table widget to display all past results
        self.table = ttk.Treeview(
            self, 
            columns=("name", "score", "timestamp", "time_taken"), 
            show="headings", 
            height=12
        )
        
        # Set up column headings and formatting
        for col, text in (("name", "Name"), ("score", "Score"), ("timestamp", "Date & Time"), 
                         ("time_taken", "Time Taken")):
            self.table.heading(col, text=text)
            self.table.column(col, width=150, anchor="w")
        
        self.table.grid(row=1, column=0, sticky="nsew")
        
       
        self.rowconfigure(1, weight=1)
        
        # Exit button container
        actions = ttk.Frame(self)
        actions.grid(row=2, column=0, pady=(10, 0), sticky="w")
        ttk.Button(actions, text="Exit", command=self.on_exit).grid(row=0, column=0)

    def display(self, results):
        """
        Populate the table with historical quiz results.
        
        Args:
            results (list[Result]): List of Result objects containing historical quiz attempts
        """
        # Clear all existing rows from the table
        for row_id in self.table.get_children():
            self.table.delete(row_id)
        
        # Insert each result as a new row in the table
        for r in results:
            # Convert seconds to min and sec 
            minutes = int(r.time_taken // 60)
            seconds = int(r.time_taken % 60) 
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

    def on_exit(self):
        """
        Handle the Exit button click event.
        """
        self.exit_callback()

    def focus_default(self):
        """
        Set keyboard focus to the results table.
        """
        self.table.focus_set()

