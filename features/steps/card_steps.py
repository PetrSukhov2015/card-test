from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import selenium
import requests
import os
import re
import sys

@given('{request_type} page with card form with {test_pattern} and {comment} and test {id}')
def step_init(context, request_type, test_pattern,comment,id):
    print ('test id '+id)
    print ('test_pattern is '+test_pattern)
    print ('comment '+comment)
    context.the_url = 'file:///C:/Users/sukhov/Desktop/form/form.html' # like http://

    if ('selenium'== request_type):
        context.selenium = True
        context.http=False
        #for exampel chrome
        #options = webdriver.ChromeOptions()
        #options.add_argument('--use-fake-ui-for-media-stream')
        #options.add_argument('--use-fake-device-for-media-stream')
        a_path = os.path.abspath('drivers/chromedriver.exe')
        context.driver = selenium.webdriver.Chrome(a_path)#, chrome_options=options)
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
        context.driver.get(context.the_url)
    elif('http'==request_type):
        context.selenium = True
        context.http=False
    else:
        print ('Error: request_type page with card form with test_pattern and comment')
        sys.exit(1)

#requests.post(url, data=test_run_json, headers=headers, auth=(str(self.login), str(self.passwd)), verify=False)


#When set <cvv> <expirtaion_month> <expirtaion_year> <amount>
@when('set {cvv} {expirtaion_month} {expirtaion_year} {amount}')
def step_set_params(context, cvv, expirtaion_month, expirtaion_year, amount):
    if (context.driver):
        #Page Object refactoring
        context.driver.find_element_by_xpath('//*[@id="cvv"]').send_keys(cvv)#.find_element_by_id('cvv').send_keys(cvv)
        context.driver.find_element_by_id('expirtaion_month').send_keys(expirtaion_month)
        context.driver.find_element_by_id('expirtaion_year').send_keys(expirtaion_year)
        context.driver.find_element_by_id('amount').send_keys(amount)
        #print ('some submit')
    elif (context.http):
        pass
        #headers = {"content-type": "application/json"}
        #data=json.dumps({"cvv": cvv, "expirtaion_month": expirtaion_month, "expirtaion_year":expirtaion_year, "amount":amount})
        #context.response = requests.post(context.the_url, data=test_run_json, headers=headers) # some http request
    else:
        print ('Error: set cvv expirtaion_month expirtaion_year amount')


@then('check {result}')
def step_check(context, result):
    if (context.driver): #driver
        wait = WebDriverWait(context.driver, 5) #wait 5 sec
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))
            context.actual_result='error'
            print('error on page')
        except:
            actual_result='ok'
            print('no error on page')

        #context.driver.close()


    elif (context.http): # http
        if str(context.response.text).__contains__('error'): #div error... class name
            context.actual_result='error'
    else:
        print ('Error: check result')


    if (context.actual_result == result):
        print ('test passed')
    else:
        print ('test filed')
    #some check
    #assert context.actual_result, result



