import pytest
import sys
import os

class TestExample:
    def test_always_passes(self):
        assert True
    
    def test_basic_math(self):
        assert 1 + 1 == 2
        assert 2 * 3 == 6
        assert 10 / 2 == 5
    
    def test_string_operations(self):
        test_string = "Hello, World!"
        assert len(test_string) == 13
        assert test_string.lower() == "hello, world!"
        assert "World" in test_string

if __name__ == "__main__":
    pytest.main([__file__])
