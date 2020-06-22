

import pdq

ts = pdq.PrintTestSuite("operations")

assert ts.equals("4", 4), ts.get_last_run()
assert ts.equals("'four'", "four"), ts.get_last_run()
assert ts.equals("{}", {}), ts.get_last_run()
assert ts.equals("[]", []), ts.get_last_run()
assert ts.equals("()", ()), ts.get_last_run()
assert ts.equals("None", None), ts.get_last_run()

assert ts.ne("4", 5), ts.get_last_run()
assert ts.ne("5.0", 6), ts.get_last_run()

assert ts.lt("'a'", 'b'), ts.get_last_run()
assert ts.lt("False", True), ts.get_last_run()

assert ts.ge("'a'", '_'), ts.get_last_run()
assert ts.ge("7", 7), ts.get_last_run()

assert ts.gt("'a'", '_'), ts.get_last_run()
assert ts.gt("7", 5), ts.get_last_run()

assert ts.le("'a'", 'a'), ts.get_last_run()
assert ts.le("4", 5), ts.get_last_run()

assert ts.issame("None", None), ts.get_last_run()
assert ts.issame("type(1)", int), ts.get_last_run()

assert ts.notsame("None", False), ts.get_last_run()
assert ts.notsame("type(1.0)", int), ts.get_last_run()

assert ts.catch("1/0", ZeroDivisionError("division by zero")), ts.get_last_run()
