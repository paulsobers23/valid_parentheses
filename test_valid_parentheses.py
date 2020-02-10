from valid_parentheses import *
import pytest

def test_valid_parentheses():
  assert valid_parentheses("()") == True
  assert valid_parentheses("()[]{}") == True
  assert valid_parentheses("(]") == False
  assert valid_parentheses("([)]") == False
  assert valid_parentheses("{[]}") == True