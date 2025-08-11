from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

BASE_URL = "http://18.158.60.215/"

def make_driver():
    opts = Options()
    for arg in [
        "--headless",  # run without opening a browser window
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]:
        opts.add_argument(arg)
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

def generate_and_get_answer(driver, operation_value):
    driver.get(BASE_URL)
    Select(driver.find_element(By.ID, "operation")).select_by_value(operation_value)
    driver.find_element(By.ID, "generate").click()

    # Wait for the exercise to be generated
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "exercise")))

    exercise_text = driver.find_element(By.ID, "exercise").text
    nums = list(map(int, re.findall(r"\d+", exercise_text)))
    op_symbol = None
    for token in exercise_text.split():
        if token in ["+", "-", "×", "÷"]:
            op_symbol = token
            break
    if op_symbol == "+":
        answer = nums[0] + nums[1]
    elif op_symbol == "-":
        answer = nums[0] - nums[1]
    elif op_symbol == "×":
        answer = nums[0] * nums[1]
    elif op_symbol == "÷":
        answer = nums[0] // nums[1]
    else:
        raise AssertionError(f"Unknown operator: {op_symbol}")
    return answer

def submit_answer(driver, value):
    answer_input = driver.find_element(By.ID, "userAnswer")
    answer_input.clear()
    answer_input.send_keys(str(value))
    driver.find_element(By.ID, "check").click()

    # Wait for the feedback to be shown
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "feedback")))

    feedback = driver.find_element(By.ID, "feedback").text
    return feedback

# Test for correct addition answer
def test_add_correct():
    driver = make_driver()
    try:
        correct_answer = generate_and_get_answer(driver, "add")
        feedback = submit_answer(driver, correct_answer)
        assert "✅ Correct answer! Well done!" in feedback, f"Expected '✅ Correct answer! Well done!', got: {feedback}"
    finally:
        driver.quit()

# Test for incorrect addition answer
def test_add_incorrect():
    driver = make_driver()
    try:
        correct_answer = generate_and_get_answer(driver, "add")
        feedback = submit_answer(driver, correct_answer + 1)
        assert "❌ Incorrect. Try again." in feedback, f"Expected '❌ Incorrect. Try again.', got: {feedback}"
    finally:
        driver.quit()

# Test for correct multiplication answer
def test_multiply_correct():
    driver = make_driver()
    try:
        correct_answer = generate_and_get_answer(driver, "mul")
        feedback = submit_answer(driver, correct_answer)
        assert "✅ Correct answer! Well done!" in feedback, f"Expected '✅ Correct answer! Well done!', got: {feedback}"
    finally:
        driver.quit()

# Test for missing number input
def test_missing_number():
    driver = make_driver()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "generate").click()
        # Wait for the exercise to load
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "exercise")))

        driver.find_element(By.ID, "check").click()
        feedback = driver.find_element(By.ID, "feedback").text
        assert "⚠️ Please enter a number" in feedback, f"Expected '⚠️ Please enter a number', got: {feedback}"
    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_correct()
    test_add_incorrect()
    test_multiply_correct()
    test_missing_number()
