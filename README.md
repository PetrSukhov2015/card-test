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
## tests
```
  |id    |request_type       |test_pattern                      | comment                         | cvv | expirtaion_month | expirtaion_year  | amount                        | result|
     |1     | selenium          |Equivalence classes partitioning  | positiv                         | 123 | 03               | 2019             | 100500.22                     | ok    |
     |1     | selenium          |Boundary-value analysis           | boundary of month               | 001 | 02               | 2019             | 100500.22                     | ok    |
     |2     | selenium          |Boundary-value analysis           | boundary of month               | 001 | 01               | 2019             | 100500.22                     | ok    |
     |3     | selenium          |Boundary-value analysis           | boundary of month               | 001 | 00               | 2019             | 100500.22                     | error |
     |4     | selenium          |Boundary-value analysis           | boundary of month               | 001 | 11               | 2019             | 100500.22                     | ok    |
     |5     | selenium          |Boundary-value analysis           | boundary of month               | 001 | 12               | 2019             | 100500.22                     | ok    |
     |6     | selenium          |Boundary-value analysis           | boundary of month and so on*    | 001 | 13               | 2019             | 100500.22                     | error |
     |21    | selenium          |Equivalence classes partitioning  | negative                        | err | error            | error            | error                         | error |
     |22    | selenium          |Equivalence classes partitioning  | negative empty fields and so on*|     |                  |                  |                               | error |
     |41    | selenium          |Equivalence classes partitioning  | negative wrong amount           | 001 | 12               | 2019             | -100500.22                    | ok    |
     |42    | selenium          |Equivalence classes partitioning  | negative wrong amount           | 001 | 12               | 2019             | 100500,22                     | ok    |
     |43    | http              |Random data Selection             | generate random data for fields |a c  | &6               |   (123           |  gldfj.k;l                    | error |
     |44    | http              |Fault Injection                   | try to generate fail            |1 3  | 03               | 2019             | 100500.22                     | ok    |
     |45    | selenium          |Secur test                        | Script Injection  and so on*    | 123 | 03               | 2019             | <script>alert(5+6);</script>  | error |
```
