import os                                          # os module: used to build the full path of the HTML file
import unittest                                    # unittest: Python's built-in testing framework
from selenium import webdriver                     # webdriver: controls the Chrome browser
from selenium.webdriver.common.by import By        # By: locator types (ID, NAME, XPATH, ...)


class CalculatorTest(unittest.TestCase):           # Test class; inheriting TestCase makes each test_ method a test case

    @classmethod                                   # Decorator: the next method belongs to the class, not one object
    def setUpClass(cls):                           # Runs ONCE before all tests
        cls.driver = webdriver.Chrome()            # Start Chrome and keep the driver for all tests
        cls.driver.set_window_size(1280, 1050)     # Set the browser window size (width, height in pixels)
        cls.url = "file://" + os.path.abspath("calculator/index.html")  # Full file URL of the calculator page

    def setUp(self):                               # Runs BEFORE every test
        self.driver.get(self.url)                  # Reload the page so each test starts with empty boxes

    def calc(self, a, b, op):                      # Helper used by many tests: performs one calculation
        """Enter two numbers, click an operator button and return the result text."""
        d = self.driver                            # Short name for the driver
        d.find_element(By.ID, "num1").send_keys(str(a))  # Find the first box by id and type number a
        d.find_element(By.ID, "num2").send_keys(str(b))  # Find the second box by id and type number b
        d.find_element(By.ID, op).click()          # Click the operator button whose id is op (add/sub/mul/div)
        return d.find_element(By.ID, "result").text  # Read and return the text shown in the result area

    def test_1_page_title(self):                   # Test 1: page title
        self.assertEqual(self.driver.title, "Simple Calculator")  # Pass if the tab title matches exactly

    def test_2_addition(self):                     # Test 2: addition
        self.assertEqual(self.calc(12, 8, "add"), "Result: 20")  # 12 + 8 must show "Result: 20"

    def test_3_subtraction(self):                  # Test 3: subtraction
        self.assertEqual(self.calc(20, 5, "sub"), "Result: 15")  # 20 - 5 must show "Result: 15"

    def test_4_multiplication(self):               # Test 4: multiplication
        self.assertEqual(self.calc(6, 7, "mul"), "Result: 42")   # 6 x 7 must show "Result: 42"

    def test_5_division(self):                     # Test 5: division
        self.assertEqual(self.calc(15, 4, "div"), "Result: 3.75")  # 15 / 4 must show "Result: 3.75"

    def test_6_divide_by_zero(self):               # Test 6: negative test - divide by zero
        self.assertEqual(self.calc(10, 0, "div"), "Error: Cannot divide by zero")  # Must show the error message

    def test_7_empty_input(self):                  # Test 7: negative test - no numbers entered
        self.driver.find_element(By.ID, "add").click()  # Click + without typing anything
        self.assertEqual(self.driver.find_element(By.ID, "result").text,
                         "Please enter both numbers")  # Must ask for both numbers

    def test_8_clear_button(self):                 # Test 8: Clear button
        self.calc(3, 4, "add")                     # First do a calculation so there is something to clear
        self.driver.find_element(By.ID, "clear").click()  # Click Clear
        self.assertEqual(self.driver.find_element(By.ID, "num1").get_attribute("value"), "")  # First box must be empty
        self.assertEqual(self.driver.find_element(By.ID, "result").text, "")  # Result area must be empty

    @classmethod                                   # Class-level method again
    def tearDownClass(cls):                        # Runs ONCE after all tests
        cls.driver.quit()                          # Close the browser and end the WebDriver session


if __name__ == "__main__":                         # True only when this file is run directly (python test_calculator.py)
    unittest.main(verbosity=2)                     # Run all tests; verbosity=2 prints each test name and result