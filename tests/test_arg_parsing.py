import pytest
import sys

from pathlib import Path
from typing import List

# Make sure project root in path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from components.arg_parsing import parse_args

### TEST TEMPLATES ###

def template_api_key_success(args, expected):
    assert expected == parse_args(args).api_key

def template_system_exit(args: List[str], exit_code: int):
    with pytest.raises(SystemExit) as err:
        parse_args(args)
    assert err.type == SystemExit
    assert err.value.code == exit_code

### TESTS ###

def test_api_key_one_arg_str_numbers_normal():
    template_api_key_success(["12345"], "12345")

def test_api_key_one_arg_str_letters_normal():
    template_api_key_success(["abcde"], "abcde")

def test_api_key_one_arg_str_numbers_and_letters_normal():
    template_api_key_success(["7d6d5f"], "7d6d5f")

def test_fail_too_many_args():
    template_system_exit(["a", "b", "c"], 2)

def test_fail_not_enough_args():
    template_system_exit([], 2)


