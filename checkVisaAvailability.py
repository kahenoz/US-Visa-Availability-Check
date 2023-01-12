import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By

while True:    
    driver = webdriver.Chrome()
    driver.minimize_window()
    time.sleep(2)
    driver.get('https://ais.usvisa-info.com/en-tr/niv/users/sign_in')
    time.sleep(2)

    email_input = driver.find_element(By.ID,"user_email")
    time.sleep(1)
    # your email for login
    email_input.send_keys('us.visa.application@example.com')
    time.sleep(1)
    password_input = driver.find_element(By.ID,"user_password")
    time.sleep(1)
    # your password for login
    password_input.send_keys('examplepassword123!')
    time.sleep(1)

    policy_confirm_input = driver.find_element(By.CLASS_NAME, "icheckbox")
    time.sleep(1)
    policy_confirm_input.click()

    time.sleep(1)
    login_form = driver.find_element(By.TAG_NAME,"form")
    time.sleep(1)
    login_form.submit()

    time.sleep(1)
    continue_button = driver.find_element(By.XPATH,"//a[@href='/en-tr/niv/schedule/44831590/continue_actions']")
    continue_button.click()

    time.sleep(1)
    schedule_button = driver.find_element(By.CLASS_NAME,"fa-calendar-alt")
    schedule_button.click()

    time.sleep(1)
    continue_button = driver.find_element(By.XPATH,"//a[@href='/en-tr/niv/schedule/44831590/continue']")
    continue_button.click()

    time.sleep(2)
    location_select = driver.find_element(By.ID,"appointments_consulate_appointment_facility_id")
    location_select.click()
    location_option = driver.find_element(By.XPATH,"//option[contains(text(), 'Istanbul')]")
    location_option.click()
    time.sleep(1)
    location_select = driver.find_element(By.ID,"appointments_consulate_appointment_facility_id")
    location_select.click()
    time.sleep(1)

    element_available = driver.find_element(By.ID,"consulate_date_time")
    display_style_istanbul = element_available.value_of_css_property("display")


    # check if the element is present on the page
    if display_style_istanbul == "block":
        # There is availability in Istanbul, so send an email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # an email account to send emails, you should use App Pasword otherwise it won't work
        server.login('sender@mail.com', 'senden.mail.password')
        # sender: example@example.com
        # receiver: the email account which you want to receive emails on
        server.sendmail('sender@mail.com', 'receiver@mail.com', 'There is availability in Istanbul, hurry up!')
        server.quit()
    else:
        location_select = driver.find_element(By.ID,"appointments_consulate_appointment_facility_id")
        location_select.click()
        location_option_ankara = driver.find_element(By.XPATH,"//option[contains(text(), 'Ankara')]")
        time.sleep(1)
        location_option_ankara.click()
        location_select.click()
        time.sleep(2)
        element_available_ankara = driver.find_element(By.ID,"consulate_date_time")
        display_style_ankara = element_available_ankara.value_of_css_property("display")
        if display_style_ankara == "block":
            # There is availability in Istanbul, so send an email
            server = smtplib.SMTP('smtp.gmail.com', 587)
       	    server.starttls()
            # an email account to send emails, you should use App Pasword otherwise it won't work
            server.login('sender@mail.com', 'senden.mail.password')
            # sender: example@example.com
            # receiver: the email account which you want to receive emails on
            server.sendmail('sender@mail.com', 'receiver@mail.com', 'There is availability in Ankara, hurry up!')
            server.quit()
        else:             
            print("There is no availability")
            time.sleep(10)
            driver.quit()
        
    # time.sleep function makes while loop wait for 30 mins
    time.sleep(30 * 60)
