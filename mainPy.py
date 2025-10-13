from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import random

waitTime = random.randint(3, 5)

print("Welcome to McMan!\nUse this program to autocomplete your survey, and get your offer!")
print("Don't worry about capital letters, we have that covered! :)")
while True:
    part1 = input("Enter your first code: ").strip().upper()
    part2 = input("Enter your second code: ").strip().upper()
    part3 = input("Enter your third code: ").strip().upper()

    if len(part1) == len(part2) == len(part3) == 4:
        print("Your code is " + " - ".join([part1, part2, part3]))
        while True:
            confirm = input("Is this code correct? (y/n): ").strip().lower()
            if confirm == "y":
                print("Right! Let's continue on!")
                break
            elif confirm == "n":
                print("Let's start again!")
                break
            else:
                print("Invalid input, try again")
            
        if confirm == "y":
            break
    else:
        print("Your code isn't right, please try again")

print(" - ".join([part1, part2, part3]))

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.mcdfoodforthoughts.com/")

time.sleep(waitTime)

# Continue
driver.find_element(By.XPATH, "//input[@id = 'NextButton']").click()
time.sleep(waitTime)

# Fill in code 1
code1 = driver.find_element(By.ID, "CN1")
code1.send_keys(part1)
time.sleep(waitTime)

# Fill in code 2
code2 = driver.find_element(By.ID, "CN2")
code2.send_keys(part2)
time.sleep(waitTime)

# Fill in code 3
code3 = driver.find_element(By.ID, "CN3")
code3.send_keys(part3)
time.sleep(waitTime)

driver.quit()