import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here

def basic_test_cases():
    assert False != True
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

def negative_input():
    assert foo_bar_baz(-7) == "" # Should be an empty string

def test_edge_cases():
    assert foo_bar_baz(0) == ""  # should give back an empty string
    assert foo_bar_baz(1) == "1"  # should give back 1

def case_invalid_inputs():
    with pytest.raises(TypeError):
        foo_bar_baz("777")
    with pytest.raises(TypeError):
        foo_bar_baz(3.14512)
    with pytest.raises(TypeError):
        foo_bar_baz(None)
    with pytest.raises(TypeError):
        foo_bar_baz([])
    with pytest.raises(TypeError):
        foo_bar_baz({})

def test_HUGE_input_case():
    result = foo_bar_baz(1000)
    assert len(result.split()) == 1000
    
def testing_output_format():
    result = foo_bar_baz(10)
    assert isinstance(result, str)
    assert "  " not in result
    assert result.strip() == result

def test_big_input():
    result = foo_bar_baz(50)  # Ensure length is correct
    assert len(result.split()) == 50  
    assert result.split()[-1] == "Bar"  # Last number (50) should be "Bar"

    result_100 = foo_bar_baz(100)
    assert len(result_100.split()) == 100  # Should have exactly 100 space-separated values
    assert result_100.split()[-1] == "Bar"  # Last number (100) should be "Bar"

if __name__ == "__main__":
    pytest.main()