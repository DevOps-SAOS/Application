import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "http://localhost"



EXPR_RE = re.compile(r'(\d+)\s*([+\-×÷])\s*(\d+)')

def make_driver():
    opts = Options()
    for arg in [
        "--headless=new",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]:
        opts.add_argument(arg)
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=opts
    )

def _wait(driver, timeout=5):
    return WebDriverWait(driver, timeout)

def generate_and_get_answer(driver, operation_value):
    driver.get(BASE_URL)
    wait = _wait(driver)

  
    Select(wait.until(EC.presence_of_element_located((By.ID, "operation")))).select_by_value(operation_value)
    wait.until(EC.element_to_be_clickable((By.ID, "generate"))).click()

    def exercise_text_ready(d):
        text = d.find_element(By.ID, "exercise").text.strip()
        return text if text else None

    exercise_text = wait.until(exercise_text_ready)

  
    m = EXPR_RE.search(exercise_text)
    assert m, f"פורמט תרגיל לא מזוהה: {exercise_text}"
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "×":
        answer = a * b
    elif op == "÷":
        assert b != 0, "חילוק באפס"
        answer = a // b
    else:
        raise AssertionError(f"אופרטור לא מזוהה: {op}")

    return answer

def submit_answer(driver, value):
    wait = _wait(driver)
    answer_input = wait.until(EC.presence_of_element_located((By.ID, "userAnswer")))
    answer_input.clear()
    answer_input.send_keys(str(value))
    wait.until(EC.element_to_be_clickable((By.ID, "check"))).click()

    def feedback_ready(d):
        txt = d.find_element(By.ID, "feedback").text.strip()
        return txt if txt else None

    return wait.until(feedback_ready)

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
