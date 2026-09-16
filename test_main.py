import unittest
from unittest.mock import patch

import main


class TestCalculatorOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(main.subtract(7, 3), 4)

    def test_multiply(self):
        self.assertEqual(main.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(main.divide(9, 3), 3)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            main.divide(9, 0)


class TestInputValidation(unittest.TestCase):
    def test_is_numeric_accepts_integer_decimal_and_negative_values(self):
        for value in ("12", "3.14", "-7"):
            with self.subTest(value=value):
                self.assertTrue(main.is_numeric(value))

    def test_is_numeric_rejects_non_numeric_values(self):
        for value in ("", "abc", "12 apples"):
            with self.subTest(value=value):
                self.assertFalse(main.is_numeric(value))


class TestCalculatorCli(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input", side_effect=["10", "+", "5"])
    def test_main_prints_calculation_result(self, mock_input, mock_print):
        main.main()

        mock_print.assert_any_call("Result: 15.0")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["ten"])
    def test_main_rejects_non_numeric_first_input(self, mock_input, mock_print):
        main.main()

        mock_print.assert_any_call("Error: first input must be numeric")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["10", "+", "five"])
    def test_main_rejects_non_numeric_second_input(self, mock_input, mock_print):
        main.main()

        mock_print.assert_any_call("Error: second input must be numeric")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["10", "%", "5"])
    def test_main_rejects_unsupported_operation(self, mock_input, mock_print):
        main.main()

        mock_print.assert_any_call("Error: unsupported operation")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["10", "/", "0"])
    def test_main_reports_division_by_zero(self, mock_input, mock_print):
        main.main()

        mock_print.assert_any_call("Error: Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
