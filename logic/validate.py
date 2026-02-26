"""
Validation Module for Quiz Application

This module contains functions for validating user input and formatting data.
"""


def validate_selected_answer(idx: int | None, num_options: int) -> bool:
    """
    Validate that a user has selected a valid answer option.
    
    This function checks two things:
    1. An answer was actually selected (idx is not None)
    2. The selected index is within the valid range of options
    
    Args:
        idx (int | None): The index of the selected option, or None if nothing was selected
        num_options (int): Total number of answer options available
    
    Returns:
        bool: True if the answer is valid, False otherwise
    

    """
    # Check if user selected something (not None) AND if the index is within valid range
    # 0 <= idx < num_options ensures the index is a valid position in the options list
    return idx is not None and 0 <= idx < num_options


def check_answer(selected: int, correct: int) -> bool:
    """
    Check if a user's answer is correct.
    
    Compares the user's selected answer index with the correct answer index.
    
    Args:
        selected (int): The index of the option the user selected
        correct (int): The index of the correct answer
    
    Returns:
        bool: True if the selected answer matches the correct answer, False otherwise
    
 
    """
    return selected == correct


def format_time(seconds: float) -> str:
    """
    Convert seconds into min and sec. 
    
    
    Args:
        seconds (float): Time duration in seconds (e.g., 245.5 for 4 minutes 5 seconds)
    
    Returns:
        str: Formatted time string
             - "MM:SS" if under 1 hour (e.g., "04:05")
             - "HH:MM:SS" if 1 hour or more (e.g., "01:04:05")
   
    
    """

    seconds = int(seconds)
    
    # divmod(a, b) returns both quotient and remainder
    # divmod(245, 60) returns (4, 5) meaning 4 minutes and 5 seconds
    m, s = divmod(seconds, 60)
    
    # divide minutes by 60 to get hours and remaining minutes
    # divmod(4, 60) returns (0, 4) meaning 0 hours and 4 minutes
    h, m = divmod(m, 60)
    
    # Format the time string:
    # {h:02d} means: integer with leading zeros to make it 2 digits (01, 02, 03... 23)
    # If h is 0, we don't need to show hours, so just show minutes:seconds
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"