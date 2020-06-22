# python-development-quality
A pdq python test suite


## Simple usage

```python
import pdq

ts = pdq.PrintTestSuite("operations")

assert ts.equals("4", 4), ts.get_last_run()
assert ts.equals("'four'", "four"), ts.get_last_run()
assert ts.equals("{}", {}), ts.get_last_run()
assert ts.equals("[]", []), ts.get_last_run()
assert ts.equals("()", ()), ts.get_last_run()
assert ts.equals("None", None), ts.get_last_run()

assert ts.issame("None", None), ts.get_last_run()
assert ts.issame("type(1)", int), ts.get_last_run()

assert ts.catch("1/0", ZeroDivisionError("division by zero")), ts.get_last_run()

ts.issame("3.1415926535", 3.1415926535)
# <<< 10 ('issame', 'operations') 3.1415926535 3.1415926535 3.1415926535 False None
False

```
