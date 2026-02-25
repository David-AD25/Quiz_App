"""
CSV Data Repository Module

This module is for the file handling operations for the quiz application.
It reads quiz questions from CSV and saves quiz results to CSV.
"""

import csv
from logic.models import Question, Result


class CSVRepository:
    """
    Manages reading and writing quiz data to CSV files.
    
    This class acts as a data persistence layer, handling:
    - Loading quiz questions from a CSV file
    - Saving quiz results to a CSV file
    - Loading historical quiz results
    
    The CSV format uses a custom separator (default "||") to split multiple choices
    into individual options, since CSV traditionally uses commas for separators.
    
    Attributes:
        questions_path (str): File path to the questions CSV file
        results_path (str): File path to the results CSV file
        field_sep (str): Separator used to split multiple fields 
    

    """
    
    def __init__(self, questions_path: str, results_path: str, field_sep: str = "||"):
        """
        Initialize the CSV repository with file paths.
        
        Args:
            questions_path (str): Path to the CSV file containing quiz questions
            results_path (str): Path to the CSV file for storing quiz results
            field_sep (str): Separator used to split multiple answer choices.
                           Default is "||" to avoid conflicts with CSV commas.
                           Example: "Option A||Option B||Option C"
        """
        self.questions_path = questions_path
        self.results_path = results_path
        self.field_sep = field_sep

    def load_questions(self):
        """
        Load all quiz questions from the CSV file.
        
        Reads questions from the CSV file and validates each one using Question.is_valid().
        Only valid questions are added to the returned list. 
        
        Expected CSV columns:
            - id: Unique identifier for the question
            - text: The question text
            - choices: Answer options separated by field_sep (e.g., "A||B||C||D")
            - correct_index: Index of correct answer (0-indexed)
            - category: (Optional) Topic of the question
            - difficulty: (Optional) Difficulty level
        
        Returns:
            list[Question]: List of valid Question objects. Empty list if file not found
                           or if no valid questions exist.
        
        """
        questions = []
        try:
            # Open the questions CSV file for reading
            with open(self.questions_path, newline="", encoding="utf-8") as f:
                # DictReader automatically treats first row as header column names
                reader = csv.DictReader(f)
                
                for row in reader:
                    # Split the choices field using the separator 
                    choices = row["choices"].split(self.field_sep) if row.get("choices") else []
                    
                    try:
                        # Create a Question object from the CSV row
                        q = Question(
                            id=row.get("id", ""),
                            text=row.get("text", ""),
                            options=[c for c in choices if c],  # Filter out empty strings
                            correct_index=int(row.get("correct_index", -1)),
                            category=row.get("category") or None,  # Empty string becomes None
                            difficulty=row.get("difficulty") or None,  # Empty string becomes None
                        )
                        
                        #  add the question if it passes validation
                        # (has text, has options, correct_index is valid)
                        if q.is_valid():
                            questions.append(q)
                    except Exception:
                        # Skip rows that can't be parsed (malformed data)
                        continue
                        
        except FileNotFoundError:
            # If file doesn't exist, return empty list (no questions to load)
            pass
        
        return questions

    def append_result(self, r: Result):
        """
        Save a quiz result to the results CSV file.
        
        This method:
        1. Creates the results CSV file with headers if it doesn't exist
        2. Appends the new result as a row to the file
        
        Uses the Result.to_dict() method to convert Result object to dictionary
        for CSV writing.
        
        Args:
            r (Result): The Result object to save containing user_name, score,
                       total_questions, time_taken, and timestamp
        
       
        """
        # Try to create the file with headers if it doesn't exist
        try:
            with open(self.results_path, "x", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, 
                    fieldnames=["user_name", "score", "total_questions", "time_taken", "timestamp"]
                )
                # Write the header row
                writer.writeheader()
        except FileExistsError:
            # File already exists, so skip header creation
            pass
        
        # Append the result as a new row
        with open(self.results_path, "a", newline="", encoding="utf-8") as f:
            # "a" mode appends to the file
            writer = csv.DictWriter(
                f,
                fieldnames=["user_name", "score", "total_questions", "time_taken", "timestamp"]
            )
            # Write the result data as a single row
            writer.writerow(r.to_dict())

    def load_results(self):
        """
        Load all saved quiz results from the CSV file.
        
        Reads each row from the results CSV and converts it back into Result objects.
         Returns empty list if file doesn't exist.
        
        Returns:
            list[Result]: List of Result objects loaded from the file.
                         Empty list if file not found or no results exist.
        
       
        """
        results = []
        try:
            # Open the results CSV file for reading
            with open(self.results_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    try:
                        # Convert CSV row back into Result object
                        # Handle type conversions: score and total_questions are integers,
                        # time_taken is a float, user_name can be None
                        results.append(
                            Result(
                                user_name=row.get("user_name") or None,  # Empty string → None
                                score=int(row.get("score", 0)),           # Convert to int
                                total_questions=int(row.get("total_questions", 0)),  # Convert to int
                                time_taken=float(row.get("time_taken", 0.0)),  # Convert to float
                                timestamp=row.get("timestamp") or "",  # Keep as string or empty
                            )
                        )
                    except Exception:
                        # Skip rows that can't be converted (malformed data)
                        continue
                        
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            pass
        
        return results