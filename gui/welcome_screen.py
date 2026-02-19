import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


class WelcomeScreen(tk.Frame):

    """
    WelcomeScreen is the initial GUI screen displayed when the application starts.
    
    This screen serves as the entry point for users to begin the IBM Code of Conduct 
    & Ethics Quiz. It displays:
    - The quiz title
    - The IBM company logo
    - A description of the quiz
    - A name input field 
    - Start and Exit buttons
    
    The screen uses callbacks to communicate with the main application controller (main.py),
    allowing the user's choice (start or exit) to trigger appropriate actions in the
    application flow.
    
    Attributes:
        start_callback (function): Callback function called when the "Start Quiz" button is clicked
        exit_callback (function): Callback function called when the "Exit" button is clicked
        name_var (tk.StringVar): Variable that stores the user's name input
        name_entry (ttk.Entry): Entry widget for the user to input their name
        logo_photo (PhotoImage): Reference to the IBM logo image 
    """
    def __init__(self, parent, start_callback, exit_callback):

        """
         
        Initialise the WelcomeScreen with all UI components.
        
        Args:
            parent (tk.Widget): The parent widget that will contain this frame
            start_callback (function): Function to call when "Start Quiz" is clicked
                                     Receives the user's name as a parameter
            exit_callback (function): Function to call when "Exit" is clicked
                                     Takes no parameters
        """
        self.start_callback = start_callback
        self.exit_callback = exit_callback

        self.grid_columnconfigure(0, weight=1)
        ttk.Label(self, text="IBM Code of Conduct & Ethics Quiz",  font=("Segoe UI", 20, "bold"),).grid(
            row=0, column=0, pady=(24, 8), sticky="n"
        )

        # Load and display logo - resized to 100x100
        logo_path = "Images/IBM_Logo.png"
        try:
            logo_image = PhotoImage(file=logo_path)
            # Resize the logo to 100x100 pixels
            logo_image = logo_image.subsample(2, 2)  # Reduces size by half (225 -> ~112)
            self.logo_photo = logo_image
            image_label = tk.Label(self, image=self.logo_photo)
            image_label.grid(row=1, column=0, pady=(8, 12))
        except tk.TclError as e:
            print(f"Error loading logo: {e}")

        description = ("Reinforce your understanding of IBM's ethical standards, including conflicts of interest, "
                "data confidentiality, responsible use of technology, and reporting unethical behaviour.")
        ttk.Label(self, text=description, wraplength=700, justify="center").grid(row=2, column=0, pady=(0, 16), padx=24)

        # User input Box :
        self.name_var = tk.StringVar()
        ttk.Label(self, text="Your name :").grid(row=3, column=0, pady=(8, 4))
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=40)
        self.name_entry.grid(row=4, column=0, pady=(0, 16))

        # Buttons : 
        btns = ttk.Frame(self)
        btns.grid(row=5, column=0, pady=(8, 24))
        ttk.Button(btns, text="Start Quiz", command=self.on_start).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Exit", command=self.exit_callback).grid(row=0, column=1, padx=6)
    
    # Call backs : 
    def on_start(self):
    
        name = self.name_var.get().strip()
        self.start_callback(name)


    def focus_default(self):
        '''
         This auto-focuses the name entry field, allowing users to immediately start typing without clicking.
        '''
        self.name_entry.focus_set()