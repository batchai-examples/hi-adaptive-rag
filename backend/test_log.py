import logging
import pytest
from backend.log import get_logger, init_loggers, LogConfig, app_logger

# Test cases for the logging functionality

class TestLogging:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test case."""
        # Clear existing handlers to avoid duplicate logs
        app_logger.handlers.clear()
        yield
        app_logger.handlers.clear()

    def test_get_logger_with_auto_level(self):
        """Test get_logger function with 'auto' level."""
        logger = get_logger("test_auto")
        assert logger.level == logging.NOTSET  # Default level should be NOTSET

    def test_get_logger_with_specific_level(self):
        """Test get_logger function with a specific logging level."""
        logger = get_logger("test_specific", logging.DEBUG)
        assert logger.level == logging.DEBUG  # Level should be set to DEBUG

    def test_init_loggers_with_valid_config(self):
        """Test init_loggers function with a valid LogConfig."""
        config = LogConfig(level="DEBUG", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logger = init_loggers(config)
        assert logger.level == logging.DEBUG  # Logger level should be set to DEBUG
        assert len(logger.handlers) == 1  # One handler should be added

    def test_init_loggers_with_invalid_level(self):
        """Test init_loggers function with an invalid logging level."""
        config = LogConfig(level="INVALID_LEVEL", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        with pytest.raises(ValueError):
            init_loggers(config)  # Should raise ValueError due to invalid level

    def test_init_loggers_with_empty_format(self):
        """Test init_loggers function with an empty format string."""
        config = LogConfig(level="INFO", format="")
        logger = init_loggers(config)
        assert logger.level == logging.INFO  # Logger level should be set to INFO
        assert len(logger.handlers) == 1  # One handler should be added
        assert logger.handlers[0].formatter._fmt == ""  # Formatter should be empty

    def test_get_logger_with_invalid_name(self):
        """Test get_logger function with an invalid logger name."""
        with pytest.raises(TypeError):
            get_logger(None)  # Should raise TypeError due to None name
