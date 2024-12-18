import pytest
from datetime import datetime
from backend.misc import (
    parse_datetime,
    format_datetime,
    guess_mime_type,
    detect_encoding,
    read_file_text,
    write_file_text,
    transfer_file,
    transfer_stream,
    parse_data_url,
    get_str_header,
    get_int_header,
    get_bool_header,
    get_client_ip,
    get_client_port,
    get_client_proto,
    get_client_proxy_chain,
    basename,
    normalize_path
)
from errs import BadRequest

# Test cases for the functions in backend/misc.py

def test_parse_datetime():
    """
    Test the parse_datetime function with various inputs.
    """
    # Happy path
    assert parse_datetime(datetime(2021, 1, 1)) == datetime(2021, 1, 1)
    assert parse_datetime(1609459200) == datetime(2021, 1, 1)
    assert parse_datetime(1609459200.0) == datetime(2021, 1, 1)
    assert parse_datetime("2021-01-01T00:00:00") == datetime(2021, 1, 1)

    # Edge cases
    assert parse_datetime(None) is None

    # Negative case
    with pytest.raises(BadRequest):
        parse_datetime("invalid datetime")

def test_format_datetime():
    """
    Test the format_datetime function.
    """
    assert format_datetime(datetime(2021, 1, 1)) == "2021-01-01T00:00:00"
    assert format_datetime(None) is None

def test_guess_mime_type():
    """
    Test the guess_mime_type function.
    """
    assert guess_mime_type("example.txt") == "text/plain"
    assert guess_mime_type("example.pdf") == "application/pdf"
    assert guess_mime_type("unknown.ext") == "application/octet-stream"

def test_detect_encoding():
    """
    Test the detect_encoding function.
    """
    assert detect_encoding(b'Hello, world!') == 'utf-8'
    assert detect_encoding(b'\x80\x81\x82') == 'utf-8'  # Example of invalid UTF-8

async def test_read_file_text(mocker):
    """
    Test the read_file_text function.
    """
    mock_fs = mocker.Mock()
    mock_fs.open.return_value.__aenter__.return_value.read.return_value = b'Hello, world!'
    
    text, encoding = await read_file_text(mock_fs, "dummy_path")
    assert text == 'Hello, world!'
    assert encoding == 'utf-8'

async def test_write_file_text(mocker):
    """
    Test the write_file_text function.
    """
    mock_fs = mocker.Mock()
    await write_file_text(mock_fs, "dummy_path", "Hello, world!")
    mock_fs.open.assert_called_once_with("dummy_path", mode="wb")

async def test_transfer_file(mocker):
    """
    Test the transfer_file function.
    """
    mock_src_fs = mocker.Mock()
    mock_dst_fs = mocker.Mock()
    mock_src_fs.open.return_value.__aenter__.return_value.read.side_effect = [b'Hello, ', b'world!']
    
    bytes_transferred, head = await transfer_file(mock_src_fs, "src_path", mock_dst_fs, "dst_path")
    assert bytes_transferred == 13
    assert head == b'Hello, '

def test_parse_data_url():
    """
    Test the parse_data_url function.
    """
    mime_type, encoding, data = parse_data_url("data:text/plain;base64,SGVsbG8sIFdvcmxkIQ==")
    assert mime_type == "text/plain"
    assert encoding == "base64"
    assert data == b'Hello, World!'

    # Negative case
    with pytest.raises(ValueError):
        parse_data_url("invalid_data_url")

def test_get_str_header():
    """
    Test the get_str_header function.
    """
    class MockRequest:
        headers = {"X-Custom-Header": "value"}

    req = MockRequest()
    assert get_str_header(req, "X-Custom-Header", "default") == "value"
    assert get_str_header(req, "Non-Existent-Header", "default") == "default"

def test_get_int_header():
    """
    Test the get_int_header function.
    """
    class MockRequest:
        headers = {"X-Custom-Int-Header": "42"}

    req = MockRequest()
    assert get_int_header(req, "X-Custom-Int-Header", 0) == 42
    assert get_int_header(req, "Non-Existent-Header", 0) == 0

def test_get_bool_header():
    """
    Test the get_bool_header function.
    """
    class MockRequest:
        headers = {"X-Custom-Bool-Header": "true"}

    req = MockRequest()
    assert get_bool_header(req, "X-Custom-Bool-Header", False) is True
    assert get_bool_header(req, "Non-Existent-Header", False) is False

def test_get_client_ip():
    """
    Test the get_client_ip function.
    """
    class MockRequest:
        headers = {"x-forwarded-for": "192.168.1.1"}
        client = None

    req = MockRequest()
    assert get_client_ip(req) == "192.168.1.1"

def test_get_client_port():
    """
    Test the get_client_port function.
    """
    class MockRequest:
        headers = {}
        client = type('obj', (object,), {'port': 8080})

    req = MockRequest()
    assert get_client_port(req) == 8080

def test_get_client_proto():
    """
    Test the get_client_proto function.
    """
    class MockRequest:
        headers = {}
        client = type('obj', (object,), {'url': type('obj', (object,), {'scheme': 'http'})})

    req = MockRequest()
    assert get_client_proto(req) == "http"

def test_get_client_proxy_chain():
    """
    Test the get_client_proxy_chain function.
    """
    class MockRequest:
        headers = {"x-forwarded-for": "192.168.1.1, 192.168.1.2"}

    req = MockRequest()
    assert get_client_proxy_chain(req) == ["192.168.1.1", "192.168.1.2"]

def test_basename():
    """
    Test the basename function.
    """
    assert basename("/path/to/file.txt") == "to/file.txt"
    assert basename("") == ""

def test_normalize_path():
    """
    Test the normalize_path function.
    """
    assert normalize_path("/path/to/../file.txt") == "path/to"
    assert normalize_path("/path/./to/file.txt") == "path/to/file.txt"
    assert normalize_path("") == ""
