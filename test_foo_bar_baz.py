import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here

def basic_test_cases():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(3) == "1 2 3 Foo"
    assert foo_bar_baz(4) == "1 2 3 Foo 4"
    assert foo_bar_baz(5) == "1 2 3 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 3 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"


def test_divisibility_cases():
    assert foo_bar_baz(10).split()[-1] == "Bar"
    assert foo_bar_baz(9).split()[-1] == "Foo"
    assert foo_bar_baz(30).split()[-1] == "Baz"


def test_edge_cases():
    assert foo_bar_baz(0) == ""  # should give back an empty string
    assert foo_bar_baz(1) == "1"  # should give back 1


def test_large_input_case():
    result = foo_bar_baz(100)
    assert len(result.split()) == 100
    
def testing_output_format():
    result = foo_bar_baz(10)
    assert isinstance(result, str)
    assert "  " not in result

if __name__ == "__main__":
    pytest.main()