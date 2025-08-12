from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

BASE_URL = "http://3.70.135.128/"

def make_driver():
    opts = Options()
    for arg in [
        "--headless",
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
    time.sleep(0.2)

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
        raise AssertionError(f"אופרטור לא מזוהה: {op_symbol}")
    return answer

def submit_answer(driver, value):
    answer_input = driver.find_element(By.ID, "userAnswer")
    answer_input.clear()
    answer_input.send_keys(str(value))
    driver.find_element(By.ID, "check").click()
    time.sleep(0.2)
    return driver.find_element(By.ID, "feedback").text
 
def test_add_correct():
    d = make_driver()
    try:
        correct_answer = generate_and_get_answer(d, "add")
        feedback = submit_answer(d, correct_answer)
        assert "תשובה נכונה" in feedback, f"ציפיתי ל'תשובה נכונה', קיבלתי: {feedback}"
    finally:
        d.quit()

 
def test_add_incorrect():
    d = make_driver()
    try:
        correct_answer = generate_and_get_answer(d, "add")
        feedback = submit_answer(d, correct_answer + 1)
        assert "לא נכון" in feedback, f"ציפיתי ל'לא נכון', קיבלתי: {feedback}"
    finally:
        d.quit()

 
def test_multiply_correct():
    d = make_driver()
    try:
        correct_answer = generate_and_get_answer(d, "mul")
        feedback = submit_answer(d, correct_answer)
        assert "תשובה נכונה" in feedback, f"ציפיתי ל'תשובה נכונה', קיבלתי: {feedback}"
    finally:
        d.quit()

if __name__ == "__main__":
    test_add_correct()
    test_add_incorrect()
    test_multiply_correct()