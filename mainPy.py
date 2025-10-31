from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
from tkinter import*

def submit():
    code1 = codeInput1.get()
    print(code1)


window = Tk()
window.geometry("600x600")
window.title("McMan")

icon = PhotoImage(file="images/mrDonald.png")
window.iconphoto(True, icon)
window.config(background = "#ffd700")

header1 = Label(window, 
                text = "Welcome to McMan, the survey completor!", 
                font = ("Arial", 20),
                fg = "#db1020",
                bg = "#ffd700")

message1 = Label(window, 
                      text = "Code 1", 
                      font = ("Arial", 10),
                      fg = "#db1020",
                      bg = "#ffd700",
                      padx = 10,
                      pady = 10)
message1.place(relx=0.17, rely=0.1, anchor = "center")

message2 = Label(window, 
                      text = "Code 2", 
                      font = ("Arial", 10),
                      fg = "#db1020",
                      bg = "#ffd700",
                      padx = 10,
                      pady = 10)
message2.place(relx=0.5, rely=0.1, anchor = "center")

message3 = Label(window, 
                      text = "Code 3", 
                      font = ("Arial", 10),
                      fg = "#db1020",
                      bg = "#ffd700",
                      padx = 10,
                      pady = 10)
message3.place(relx=0.83, rely=0.1, anchor = "center")

codeInput1 = Entry(window,
                   width = 4,
                   bg = "white",
                   fg = "black")
codeInput1.place(relx=0.17, rely=0.17, anchor = "center")

codeInput2 = Entry(window,
                   width = 4,
                   bg = "white",
                   fg = "black")
codeInput2.place(relx=0.5, rely=0.17, anchor = "center")

codeInput3 = Entry(window,
                   width = 4,
                   bg = "white",
                   fg = "black")
codeInput3.place(relx=0.83, rely=0.17, anchor = "center")

submit = Button(window, 
                text = "submit", 
                command = submit)

poundsInput = Entry(window,
                    width = 4,
                    bg = "white",
                    fg = "black")
poundsInput.place(x=450, y=500)

penceInput = Entry(window,
                   width = 4,
                   bg = "white",
                   fg = "black")

header1.pack()
submit.pack(side="bottom")
window.mainloop()

# 
# with open("stuff.txt", "r") as f:
#     data = json.load(f)

# print("Welcome to McMan!\nUse this program to autocomplete your survey, and get your offer!")
# print("Don't worry about capital letters, we have that covered! :)")

# while True:
#     pounds = input("Enter the pounds of the meal: ").strip()
#     data["fill_in_boxes"]["pounds"]["default_message"] = pounds

#     pence = input("Enter the pence of your meal: ").strip()
#     data["fill_in_boxes"]["pence"]["default_message"] = pence

#     part1 = input("Enter your first code: ").strip().upper()
#     data["fill_in_boxes"]["code1"]["default_message"] = part1

#     part2 = input("Enter your second code: ").strip().upper()
#     data["fill_in_boxes"]["code2"]["default_message"] = part2

#     part3 = input("Enter your third code: ").strip().upper()
#     data["fill_in_boxes"]["code3"]["default_message"] = part3


#     if len(pounds) < 4 and len(pence) < 3 and len(part1) == len(part2) == len(part3) == 4:
#         print("Your code is " + " - ".join([part1, part2, part3]) + " and you have spent " + "£" + pounds + "." + pence)
#         while True:
#             confirm = input("Is this code correct? (y/n): ").strip().lower()
#             if confirm == "y":
#                 print("Right! Let's continue on!")
#                 break
#             elif confirm == "n":
#                 print("Let's start again!")
#                 break
#             else:
#                 print("Invalid input, try again")
            
#         if confirm == "y":
#             break
#     else:
#         print("Your code or price isn't right, please try again")

# print(" - ".join([part1, part2, part3]))

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--incognito')
# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service = service, options = chrome_option)
# driver.get("https://www.mcdfoodforthoughts.com/")

# while True:
#     time.sleep(10)
#     for box in data["fill_in_boxes"].values():
#         try:
#             element = driver.find_element(By.XPATH, box["XPath"])
#             if "default_message" in box:
#                 element.send_keys(box["default_message"])
#         except:
#             print(f"{box["XPath"]} not found")


#     for option in data["options"].values():
#         try:
#             element = driver.find_element(By.XPATH, option["XPath"])
#             element.click()
#         except:
#             print(f"{option["XPath"]} not found")

#     next_button_XPath = data["buttons"]["next_button"]["XPath"]
#     try:
#         next_button = driver.find_element(By.XPATH, next_button_XPath)
#         next_button.click()
#     except:
#         print("I'm done")
#         break

# driver.quit()