from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import re
# from webdriver_manager.core.utils import ChromeType

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]

for option in options:
    chrome_options.add_argument(option)

def test_site():
    url = "http://18.195.170.226//"    

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get(url)

     
    operation_select = driver.find_element(By.ID, "operation")
    operation_select.send_keys("add")   
    generate_button = driver.find_element(By.ID, "generate")
    generate_button.click()

     
    exercise_text = driver.find_element(By.ID, "exercise").text
    print(f"תרגיל נוצר: {exercise_text}")
    
     
    numbers = re.findall(r'\d+', exercise_text)   
    if len(numbers) == 2:
        num1, num2 = map(int, numbers)   
        operator = exercise_text.split()[1]   
    
        if operator == "+":
            correct_answer = num1 + num2
        elif operator == "-":
            correct_answer = num1 - num2
        elif operator == "*":
            correct_answer = num1 * num2
        elif operator == "/":
            correct_answer = num1 / num2
        else:
            print(f"לא זוהה תרגיל: {exercise_text}")
            driver.quit()
            return

        print(correct_answer)
 
        answer_input = driver.find_element(By.ID, "userAnswer")
        answer_input.send_keys(str(correct_answer))   
        check_button = driver.find_element(By.ID, "check")
        check_button.click()

      
        feedback = driver.find_element(By.ID, "feedback").text
        print(f"פידבק: {feedback}")

      
        assert "נכון" in feedback, f"פידבק לא נכנס, קיבלת: {feedback}"

    else:
        print(f"לא נמצא תרגיל תקני: {exercise_text}")
    
    
    driver.quit()

 
test_site()
