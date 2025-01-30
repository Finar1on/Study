import pytest

from decorators import log


def test_console_logging_success(console_log, capsys):
    result = console_log(2, 3, c=4)

    captured = capsys.readouterr()
    assert "Log file isn't assigned, log to console instead..." in captured.out
    assert "func success | Args: (2, 3) | Kwargs: {'c': 4}" in captured.out
    assert result == 9


def test_console_logging_error(console_log, capsys):

    @log()
    def error_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError) as exc_info:
        error_func()

    captured = capsys.readouterr()
    assert "error_func FAILED: Test error" in captured.out
    assert "Test error" in str(exc_info.value)


def test_file_logging_error():
    @log(filename="logs")
    def error_func():
        raise TypeError("Something wrong")

    with pytest.raises(TypeError):
        error_func()

    with open("logs") as f:
        content = f.read()
        assert "error_func FAILED: Something wrong" in content
