from dataclasses import dataclass
from typing import  List

"""
Data Models for the Quiz Application

This module contains the core data classes used throughout the application:
- Question: Represents a single quiz question with options and correct answer
- Result: Represents the outcome of a completed quiz attempt
"""

@dataclass(frozen=True)

class Question:
    """
    Represents a single quiz question with multiple choice options.
    
    A Question is an immutable data structure (frozen=True means it cannot be modified 
    after creation) that stores all information needed to display a question and 
    check if an answer is correct.
    
    Attributes:
        id (str): Unique identifier for each question
        text (str): The question text displayed to the user 
        options (List[str]): List of answer choices 
        correct_index (int): Index of the correct answer in the options list 
        
    """
    id: str
    text: str
    options: List[str]
    correct_index: int



    def is_valid(self):
        """
        Validate that each question is properly formatted.
        
        Checks three conditions:
        1. The question text is not empty 
        2. There are at least 2 answer options
        3. The correct_index points to an actual option (is within bounds)
        
        This method is useful for catching data entry errors before the quiz starts.
        
        Returns:
            bool: True if the question meets all validation criteria, False otherwise
        
        
        """
        return bool(self.text.strip()) and len(self.options) >= 2 and 0 <= self.correct_index < len(self.options)

@dataclass(frozen=True)
class Result:
    """
    Represents the outcome of a completed quiz attempt.
    
    A Result is an immutable data structure that stores all information about the 
    user's quiz performance, including their score, time taken, and when they 
    completed it.
    
    Attributes:
        user_name (str): Name of the person who took the quiz
        score (int): Number of questions answered correctly
        total_questions (int): Total number of questions in the quiz 
        time_taken (float): Time taken to complete the quiz in seconds 
        timestamp (str): Date and time when the quiz was completed 
                        
    """
    user_name: str
    score: int
    total_questions: int
    time_taken: float
    timestamp: str

    def to_dict(self) :

           """
    Represents the outcome of a completed quiz attempt.
    
    A Result is an immutable data structure that stores all information about how 
    a user performed on a quiz, including their score, time taken, and when they 
    completed it.
    
    Attributes:
        user_name (Optional[str]): Name of the person who took the quiz
                                  Can be None or empty if the user skipped entering their name
        score (int): Number of questions answered correctly (e.g., 8)
        total_questions (int): Total number of questions in the quiz (e.g., 10)
        time_taken (float): Time taken to complete the quiz in seconds (e.g., 245.5)
        timestamp (str): Date and time when the quiz was completed 
                        (e.g., "2024-02-20 14:30")
    
    Example:
        >>> result = Result(
        ...     user_name="David",
        ...     score=8,
        ...     total_questions=10,
        ...     time_taken=245.0,
        ...     timestamp="2024-02-20 14:30"
        ... )
        >>> result.score
        8
    """
    
    user_name: str
    score: int
    total_questions: int
    time_taken: float
    timestamp: str
    
    def to_dict(self) -> dict:
        """
        Convert the Result object to a dictionary format.

        """
        return {
            "user_name": self.user_name or "",
            "score": self.score,
            "total_questions": self.total_questions,
            "time_taken": self.time_taken,
            "timestamp": self.timestamp,
        }