# card-test
test of 4 input fields of html page
## setup
```
git clone https://github.com/PetrSukhov2015/card-test.git
Python 3.7+
Pip
Win Chrome driver
pip install selenium
pip install requests
pip install behave
```
## task
set tests for form
```html
<form id = "card"
<input id="pan">
<input id="cvv">
<input id="expirtaion_month">
<input id="expirtaion_year">
<input id="amount">
</form>
```
## usage
```
edit features\card.feature
and run test from cmd
behave features\card.feature
```
