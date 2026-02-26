"""
Quiz Logic Module

Handles the core quiz logic including question progression,
answer tracking, timing, and score calculation.
"""

import time
from typing import List
from datetime import datetime, timezone
from .models import Question, Result


class Quiz:
    """
    Manages a quiz session from start to finish.
    
    Tracks the current question, user answers, timing, and quiz state.
    Provides methods to navigate through questions, submit answers, and
    calculate the final score.
    
    Attributes:
        questions (List[Question]): List of all questions in the quiz
        current_index (int): Index of the current question 
        user_answers (List[int | None]): List of answer indexes
        start_time (float | None): timestamp when quiz started
        end_time (float | None): timestamp when quiz ended
        is_active (bool): Whether the quiz is currently running

    """
    
    def __init__(self, questions: List[Question]):
        """
        Initialize a quiz with questions.
        
        Args:
            questions (List[Question]): List of Question objects to display
        """
        self.questions = questions
        self.current_index = 0
        # Sets up the quiz with an empty answer list
        self.user_answers: List[int | None] = [None] * len(questions)
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.is_active = False

    def start(self):
        """
        Start the quiz and begin timing.
        
        Resets the quiz state, records the start time, and marks the quiz as active.
        """
        self.current_index = 0
        self.user_answers = [None] * len(self.questions)
        self.start_time = time.time()
        self.end_time = None
        self.is_active = True

    def get_current_question(self) :
        """
        Get the question currently being displayed.
        
        Returns:
            Question: The Question object at the current index
        """
        return self.questions[self.current_index]

    def submit_answer(self, selected_index: int):
        """
        Records the user's answer for the current question.
        
        Args:
            selected_index (int): The index of the option the user selected 
        """
        self.user_answers[self.current_index] = selected_index

    def next_question(self):
        """
        Move to the next question in the quiz.
        
        Returns:
            bool: True if there is a next question and we moved to it,
                  False if we're on the last question
        """
        if self.current_index + 1 < len(self.questions):
            self.current_index += 1
            return True
        return False

    def calculate_score(self) :
        """
        Calculate the number of correct answers.
        
        Compares each user answer against the correct answer for each question.
        Skips unanswered questions (None values).
        
        Returns:
            int: Number of questions answered correctly
        """
        score = 0
        # zip pairs each answer with its corresponding question
        for ans, q in zip(self.user_answers, self.questions):
            if ans is not None and ans == q.correct_index:
                score += 1
        return score

    def finish(self, user_name: str | None) :
        """
        End the quiz and create a result record.
        
        Records the end time, calculates the final score and time taken,
        and returns a Result object with all quiz data.
        
        Args:
            user_name (str | None): The user's name (can be None or empty)
        
        Returns:
            Result: A Result object containing the quiz outcome
        
       
        """
        self.end_time = time.time()
        self.is_active = False
        
        # Calculate time in seconds, rounded to 2 decimal places
        time_taken = round(self.end_time - (self.start_time or self.end_time), 2)
        
        # Create ISO 8601 formatted timestamp (e.g., "2024-02-20T14:30:00Z")
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        return Result(
            user_name=user_name,
            score=self.calculate_score(),
            total_questions=len(self.questions),
            time_taken=time_taken,
            timestamp=ts
        )