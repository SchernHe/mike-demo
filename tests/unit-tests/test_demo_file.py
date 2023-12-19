from mike_demo.demo_file import combine_two_string


def test_combine_two_strings_default_separator():
    """Two strings are combined with the default separator."""
    expected_result = "test-demo"
    result = combine_two_string("test", "demo")

    assert expected_result == result
