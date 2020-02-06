# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time

number = 'YOUR NUMBER'
username = 'YOUR EMAIL ID'
password = 'YOUR PASSWORD'

def login():
    
    driver = webdriver.Chrome()
    
    driver.get("https://tinder.com/?lang=en")
    time.sleep(2)    
   
#    method = input("Choose the method of login.    1. Facebook    2. Phone Number ")
    
    login_by_fb(driver)    
#    print(driver.window_handles)
#    print(driver.current_window_handle)

#    if method == '1':
#        login_by_fb(driver)
#    elif method == '2':
#        login_by_phone(driver)
#    else:
#        print("Choose one of the following ways!")
    
    time.sleep(2)
    
    location_access = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    location_access.click()

    enable = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    enable.click()        
    
    swipe(driver)
   
def login_by_fb(driver):
    
    login_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
    login_btn.click()
    
    base = driver.window_handles[0]

    driver.switch_to.window(driver.window_handles[1])
#    print("in new window")
    
    email = driver.find_element_by_xpath('//*[@id="email"]')
    email.send_keys(username)
    
    pass_ = driver.find_element_by_xpath('//*[@id="pass"]')
    pass_.send_keys(password)
    
    new_login_btn = driver.find_element_by_xpath('//*[@id="u_0_0"]')
    new_login_btn.click()

    try:
        confirm_btn = driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button')
        confirm_btn.click()
    except:
        pass 
    
    driver.switch_to.window(base)
    
def login_by_phone(driver):
    
    login_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
    login_btn.click()
    
    phone = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input[@value="'+str(number)+'"]')
    phone.send_keys(number)
    
    cont_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
    cont_btn.click()

    vef_code = input('Enter your verification code: ')    

    for i in range(6):
        verify = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[3]/input['+str(i+1)+']')
        verify.send_keys(vef_code[i])
     
    cont_btn.click()
    
def right_swipe(driver):
    like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
    like_btn.click()
    
def left_swipe(driver):
    dislike_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
    dislike_btn.click()
    
def close_popup(driver):
        popup = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()
    
def close_match(driver):
        match_popup = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

def swipe(temp):
    
    for i in range(6):
        time.sleep(1)
        try:
            right_swipe(temp)
        except Exception:
            try:
                close_popup(temp)
            except Exception:
                close_match(temp)
    
if __name__ == "__main__":
    login()
    
