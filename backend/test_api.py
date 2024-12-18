import pytest
from fastapi.testclient import TestClient
from backend.api import fastapi_app
from pydantic import ValidationError

client = TestClient(fastapi_app)

# Test cases for the FastAPI application

def test_submit_question_happy_path():
    """
    Test the /rest/v1/question endpoint with a valid question.
    This represents a happy path scenario where the input is valid.
    """
    response = client.post("/rest/v1/question", json={"question": "What is the capital of France?"})
    assert response.status_code == 200
    assert response.json()["question"] == "What is the capital of France?"
    assert "answer" in response.json()

def test_submit_question_with_empty_string():
    """
    Test the /rest/v1/question endpoint with an empty question.
    This tests the validation of the input, expecting a 422 Unprocessable Entity response.
    """
    response = client.post("/rest/v1/question", json={"question": ""})
    assert response.status_code == 422
    assert "detail" in response.json()

def test_submit_question_with_whitespace():
    """
    Test the /rest/v1/question endpoint with a question that is only whitespace.
    This tests the validation of the input, expecting a 422 Unprocessable Entity response.
    """
    response = client.post("/rest/v1/question", json={"question": "   "})
    assert response.status_code == 422
    assert "detail" in response.json()

def test_submit_question_with_invalid_data_type():
    """
    Test the /rest/v1/question endpoint with an invalid data type for the question.
    This tests the validation of the input, expecting a 422 Unprocessable Entity response.
    """
    response = client.post("/rest/v1/question", json={"question": 12345})
    assert response.status_code == 422
    assert "detail" in response.json()

def test_submit_question_internal_server_error():
    """
    Test the /rest/v1/question endpoint to simulate an internal server error.
    This tests the error handling of the application.
    """
    # Assuming we can trigger an internal error by sending a specific question
    response = client.post("/rest/v1/question", json={"question": "Trigger internal error"})
    assert response.status_code == 500
    assert "detail" in response.json()

def test_submit_question_with_special_characters():
    """
    Test the /rest/v1/question endpoint with a question containing special characters.
    This tests the application's ability to handle various characters in the input.
    """
    response = client.post("/rest/v1/question", json={"question": "What is 2 + 2?"})
    assert response.status_code == 200
    assert response.json()["question"] == "What is 2 + 2?"
    assert "answer" in response.json()
