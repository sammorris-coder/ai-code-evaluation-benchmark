from benchmark.test_cases import TEST_CASES


def test_all_five_functions_have_test_cases():
    assert len(TEST_CASES) == 5

    for function_name, cases in TEST_CASES.items():
        assert cases, f"{function_name} has no test cases"


def test_every_case_has_input_and_expected_result():
    for function_name, cases in TEST_CASES.items():
        for case in cases:
            assert "input" in case, function_name

            has_expected = "expected" in case
            has_exception = "expected_exception" in case

            assert has_expected != has_exception, (
                f"Invalid expected result definition for {function_name}"
            )


def test_all_expected_exceptions_are_value_errors():
    for cases in TEST_CASES.values():
        for case in cases:
            if "expected_exception" in case:
                assert case["expected_exception"] is ValueError
