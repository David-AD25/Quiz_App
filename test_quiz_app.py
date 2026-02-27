"""
Unit Tests for IBM Code of Conduct & Ethics Quiz Application

This test suite validates core business logic including:
- Validation functions (answer validation, time formatting)
- Quiz logic (state management, score calculation)
- Model validation (Question and Result objects)
- Data persistence (CSV operations)

Run with: python -m pytest test_quiz_app.py -v
"""

import pytest
from logic.validate import validate_selected_answer, check_answer, format_time
from logic.models import Question, Result
from logic.quiz import Quiz


# VALIDATION FUNCTION TESTS


class TestValidateSelectedAnswer:
    """Test cases for validate_selected_answer() function"""
    
    def test_valid_selection_first_option(self):
        """Test that selecting the first option (0) is valid"""
        result = validate_selected_answer(0, 4)
        assert result is True
    
    def test_valid_selection_last_option(self):
        """Test that selecting the last option is valid"""
        result = validate_selected_answer(3, 4)
        assert result is True
    
    def test_valid_selection_middle_option(self):
        """Test that selecting a middle option is valid"""
        result = validate_selected_answer(2, 4)
        assert result is True
    
    def test_invalid_selection_none(self):
        """Test that None (no selection) is invalid"""
        result = validate_selected_answer(None, 4)
        assert result is False
    
    def test_invalid_selection_out_of_range_high(self):
        """Test that selection beyond available options is invalid"""
        result = validate_selected_answer(5, 4)
        assert result is False
    
    def test_invalid_selection_negative(self):
        """Test that negative index is invalid"""
        result = validate_selected_answer(-1, 4)
        assert result is False
    
    def test_valid_selection_with_two_options(self):
        """Test that selection works with minimum 2 options"""
        result = validate_selected_answer(1, 2)
        assert result is True


class TestCheckAnswer:
    """Test cases for check_answer() function"""
    
    def test_correct_answer_first_option(self):
        """Test that correct answer (index 0) returns True"""
        result = check_answer(0, 0)
        assert result is True
    
    def test_correct_answer_third_option(self):
        """Test that correct answer (index 2) returns True"""
        result = check_answer(2, 2)
        assert result is True
    
    def test_incorrect_answer_selected_0_correct_1(self):
        """Test that incorrect answer returns False"""
        result = check_answer(0, 1)
        assert result is False
    
    def test_incorrect_answer_selected_2_correct_3(self):
        """Test that incorrect answer (different indices) returns False"""
        result = check_answer(2, 3)
        assert result is False
    
    def test_multiple_correct_scenarios(self):
        """Test multiple correct answers"""
        assert check_answer(0, 0) is True
        assert check_answer(1, 1) is True
        assert check_answer(2, 2) is True


class TestFormatTime:
    """Test cases for format_time() function"""
    
    def test_format_30_seconds(self):
        """Test formatting 30 seconds as 00:30"""
        result = format_time(30)
        assert result == "00:30"
    
    def test_format_5_minutes_0_seconds(self):
        """Test formatting 300 seconds as 05:00"""
        result = format_time(300)
        assert result == "05:00"
    
    def test_format_4_minutes_5_seconds(self):
        """Test formatting 245 seconds as 04:05"""
        result = format_time(245)
        assert result == "04:05"
    
    def test_format_2_minutes_0_seconds(self):
        """Test formatting 120 seconds as 02:00"""
        result = format_time(120)
        assert result == "02:00"
    
    def test_format_with_decimal_seconds(self):
        """Test that decimal seconds are truncated"""
        result = format_time(245.5)
        assert result == "04:05"
    
    def test_format_1_hour(self):
        """Test formatting 1 hour as 01:00:00"""
        result = format_time(3600)
        assert result == "01:00:00"
    
    def test_format_1_hour_4_minutes_5_seconds(self):
        """Test formatting 1h 4m 5s as 01:04:05"""
        result = format_time(3845)
        assert result == "01:04:05"
    
    def test_format_zero_seconds(self):
        """Test formatting 0 seconds as 00:00"""
        result = format_time(0)
        assert result == "00:00"
    
    def test_format_59_seconds(self):
        """Test formatting 59 seconds as 00:59"""
        result = format_time(59)
        assert result == "00:59"


# ============================================================================
# MODEL TESTS
# ============================================================================

class TestQuestion:
    """Test cases for Question model"""
    
    def test_valid_question(self):
        """Test that a valid question passes validation"""
        q = Question(
            id="q001",
            text="What does IBM stand for?",
            options=["International Business Machines", "Internet Business Management"],
            correct_index=0
        )
        assert q.is_valid() is True
    
    def test_invalid_question_empty_text(self):
        """Test that question with empty text fails validation"""
        q = Question(
            id="q002",
            text="",
            options=["Option A", "Option B"],
            correct_index=0
        )
        assert q.is_valid() is False
    
    def test_invalid_question_single_option(self):
        """Test that question with only 1 option fails validation"""
        q = Question(
            id="q003",
            text="Question text?",
            options=["Only option"],
            correct_index=0
        )
        assert q.is_valid() is False
    
    def test_invalid_question_correct_index_out_of_range(self):
        """Test that question with invalid correct_index fails validation"""
        q = Question(
            id="q004",
            text="Question text?",
            options=["Option A", "Option B"],
            correct_index=5
        )
        assert q.is_valid() is False
    
    def test_invalid_question_negative_correct_index(self):
        """Test that negative correct_index fails validation"""
        q = Question(
            id="q005",
            text="Question text?",
            options=["Option A", "Option B"],
            correct_index=-1
        )
        assert q.is_valid() is False
    
    def test_question_with_four_options(self):
        """Test that question with 4 options is valid"""
        q = Question(
            id="q006",
            text="What does IBM stand for?",
            options=["Option A", "Option B", "Option C", "Option D"],
            correct_index=2
        )
        assert q.is_valid() is True


class TestResult:
    """Test cases for Result model"""
    
    def test_result_to_dict(self):
        """Test that Result converts to dictionary correctly"""
        result = Result(
            user_name="David",
            score=8,
            total_questions=10,
            time_taken=245.0,
            timestamp="2024-02-20T14:30:00Z"
        )
        result_dict = result.to_dict()
        
        assert result_dict["user_name"] == "David"
        assert result_dict["score"] == 8
        assert result_dict["total_questions"] == 10
        assert result_dict["time_taken"] == 245.0
        assert result_dict["timestamp"] == "2024-02-20T14:30:00Z"
    
    def test_result_to_dict_empty_name(self):
        """Test that empty name becomes empty string in dict"""
        result = Result(
            user_name="",
            score=5,
            total_questions=10,
            time_taken=300.0,
            timestamp="2024-02-20T12:00:00Z"
        )
        result_dict = result.to_dict()
        assert result_dict["user_name"] == ""
    
    def test_result_with_perfect_score(self):
        """Test Result with perfect score"""
        result = Result(
            user_name="Alice",
            score=10,
            total_questions=10,
            time_taken=120.0,
            timestamp="2024-02-20T13:45:00Z"
        )
        assert result.score == result.total_questions
        assert result.to_dict()["score"] == 10



# QUIZ LOGIC TESTS


class TestQuiz:
    """Test cases for Quiz class"""
    
    def setup_method(self):
        """Create sample questions for each test"""
        self.questions = [
            Question(
                id="q001",
                text="What does IBM stand for?",
                options=["International Business Machines", "Internet Business Management"],
                correct_index=0
            ),
            Question(
                id="q002",
                text="Is ethics important?",
                options=["Yes", "No"],
                correct_index=0
            ),
            Question(
                id="q003",
                text="What is the correct answer?",
                options=["Option A", "Option B", "Option C"],
                correct_index=2
            ),
        ]
    
    def test_quiz_initialization(self):
        """Test that Quiz initializes correctly"""
        quiz = Quiz(self.questions)
        assert quiz.current_index == 0
        assert quiz.is_active is False
        assert len(quiz.user_answers) == 3
    
    def test_quiz_start(self):
        """Test that quiz.start() sets up state correctly"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        assert quiz.is_active is True
        assert quiz.current_index == 0
        assert quiz.start_time is not None
    
    def test_get_current_question(self):
        """Test getting the current question"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        current = quiz.get_current_question()
        assert current.id == "q001"
        assert current.text == "What does IBM stand for?"
    
    def test_submit_answer(self):
        """Test submitting an answer"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        quiz.submit_answer(0)  # Select first option
        assert quiz.user_answers[0] == 0
    
    def test_next_question(self):
        """Test moving to next question"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        result = quiz.next_question()
        assert result is True
        assert quiz.current_index == 1
    
    def test_next_question_on_last(self):
        """Test that next_question returns False on last question"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        # Move to last question
        quiz.current_index = 2
        result = quiz.next_question()
        assert result is False
        assert quiz.current_index == 2  # Should not move
    
    def test_calculate_score_all_correct(self):
        """Test score calculation when all answers correct"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        quiz.submit_answer(0)  # Correct for q001
        quiz.next_question()
        quiz.submit_answer(0)  # Correct for q002
        quiz.next_question()
        quiz.submit_answer(2)  # Correct for q003
        
        score = quiz.calculate_score()
        assert score == 3
    
    def test_calculate_score_all_incorrect(self):
        """Test score calculation when all answers incorrect"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        quiz.submit_answer(1)  # Wrong for q001
        quiz.next_question()
        quiz.submit_answer(1)  # Wrong for q002
        quiz.next_question()
        quiz.submit_answer(0)  # Wrong for q003
        
        score = quiz.calculate_score()
        assert score == 0
    
    def test_calculate_score_mixed(self):
        """Test score calculation with mixed correct/incorrect"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        quiz.submit_answer(0)  # Correct for q001
        quiz.next_question()
        quiz.submit_answer(1)  # Wrong for q002
        quiz.next_question()
        quiz.submit_answer(2)  # Correct for q003
        
        score = quiz.calculate_score()
        assert score == 2
    
    def test_finish_creates_result(self):
        """Test that finish() creates a Result object"""
        quiz = Quiz(self.questions)
        quiz.start()
        
        quiz.submit_answer(0)
        
        result = quiz.finish(user_name="TestUser")
        
        assert isinstance(result, Result)
        assert result.user_name == "TestUser"
        assert result.total_questions == 3
        assert result.score == 1
        assert result.time_taken >= 0



# INTEGRATION TESTS


class TestIntegration:
    """Integration tests combining multiple components"""
    
    def test_complete_quiz_flow(self):
        """Test a complete quiz from start to finish"""
        questions = [
            Question(
                id="q001",
                text="Test question 1?",
                options=["Correct", "Wrong"],
                correct_index=0
            ),
            Question(
                id="q002",
                text="Test question 2?",
                options=["Wrong", "Correct"],
                correct_index=1
            ),
        ]
        
        # Create and start quiz
        quiz = Quiz(questions)
        quiz.start()
        
        # Answer question 1 correctly
        q1 = quiz.get_current_question()
        assert validate_selected_answer(0, len(q1.options))
        quiz.submit_answer(0)
        assert check_answer(0, q1.correct_index)
        
        # Move to question 2
        assert quiz.next_question()
        
        # Answer question 2 correctly
        q2 = quiz.get_current_question()
        assert validate_selected_answer(1, len(q2.options))
        quiz.submit_answer(1)
        assert check_answer(1, q2.correct_index)
        
        # Finish quiz
        result = quiz.finish(user_name="TestUser")
        
        # Verify result
        assert result.score == 2
        assert result.total_questions == 2
        assert result.user_name == "TestUser"
        assert result.timestamp is not None
        assert result.time_taken >= 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])