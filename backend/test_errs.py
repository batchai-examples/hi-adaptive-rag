import pytest
from backend.errs import Internal, BadRequest, Unauthorized, Forbidden, NotFound, Conflict, ErrorCode

# Test cases for the error classes in backend.errs

def test_internal_error():
    """Test Internal error with default code."""
    error = Internal(detail="Internal server error")
    assert error.status_code == 500
    assert error.detail == "Internal server error"
    assert error.code == ErrorCode.NONE

def test_internal_error_with_custom_code():
    """Test Internal error with custom error code."""
    error = Internal(detail="Internal server error", code=ErrorCode.INVALID_PROPERTY)
    assert error.status_code == 500
    assert error.detail == "Internal server error"
    assert error.code == ErrorCode.INVALID_PROPERTY

def test_bad_request_error():
    """Test BadRequest error with default code."""
    error = BadRequest(detail="Bad request")
    assert error.status_code == 400
    assert error.detail == "Bad request"
    assert error.code == ErrorCode.NONE

def test_bad_request_error_with_custom_code():
    """Test BadRequest error with custom error code."""
    error = BadRequest(detail="Bad request", code=ErrorCode.INVALID_ENUM)
    assert error.status_code == 400
    assert error.detail == "Bad request"
    assert error.code == ErrorCode.INVALID_ENUM

def test_unauthorized_error():
    """Test Unauthorized error with default code."""
    error = Unauthorized(detail="Unauthorized access")
    assert error.status_code == 401
    assert error.detail == "Unauthorized access"
    assert error.code == ErrorCode.NONE

def test_forbidden_error():
    """Test Forbidden error with default code."""
    error = Forbidden(detail="Access forbidden")
    assert error.status_code == 403
    assert error.detail == "Access forbidden"
    assert error.code == ErrorCode.NONE

def test_not_found_error():
    """Test NotFound error with default code."""
    error = NotFound(detail="Resource not found")
    assert error.status_code == 404
    assert error.detail == "Resource not found"
    assert error.code == ErrorCode.NONE

def test_conflict_error():
    """Test Conflict error with default code."""
    error = Conflict(detail="Conflict occurred")
    assert error.status_code == 409
    assert error.detail == "Conflict occurred"
    assert error.code == ErrorCode.NONE

def test_error_code_enum():
    """Test ErrorCode enum values."""
    assert ErrorCode.NONE == "NONE"
    assert ErrorCode.INVALID_ENUM == "INVALID_ENUM"
    assert ErrorCode.INVALID_PROPERTY == "INVALID_PROPERTY"

def test_internal_error_invalid_code():
    """Test Internal error with invalid code (not part of ErrorCode)."""
    with pytest.raises(TypeError):
        Internal(detail="Invalid code", code="INVALID_CODE")
