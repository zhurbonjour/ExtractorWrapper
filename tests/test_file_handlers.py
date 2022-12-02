import pytest
from src import file_handlers


@pytest.mark.parametrize("filepath, reg_exp, expected_result",
                         [('/home/alexeyz/PycharmProjects/ExtractorWrapper/домены.rtf', "123", []),
                          ])
def test_check_values_in_file(filepath, reg_exp, expected_result):
    assert file_handlers.check_values_in_file(filepath, reg_exp) == \
           expected_result


@pytest.mark.parametrize("filepath, reg_exp, expected_exception",
                         [("qwerty", "123", FileNotFoundError),
                          (123, 123, OSError)])
def test_check_values_in_file_exceptions(filepath, reg_exp, expected_exception):
    with pytest.raises(expected_exception):
        file_handlers.check_values_in_file(filepath, reg_exp)
