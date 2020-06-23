

import pdq

test_suite = pdq.WriterTestSuite("root")

ts = pdq.WriterTestSuite("operations", parent=test_suite)

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

assert ts.contains("(1,2,3)", 2), ts.get_last_run()
assert ts.has("2", (1,2,3)), ts.get_last_run()
assert ts.notcontains("(1,2,3)", 4), ts.get_last_run()
assert ts.nothas("5", (1,2,3)), ts.get_last_run()

assert ts.instance("5", int), ts.get_last_run()
assert ts.notinstance("5", float), ts.get_last_run()

assert ts.subclass("int", object), ts.get_last_run()
assert ts.notsubclass("float", type), ts.get_last_run()

assert ts.truish("57"), ts.get_last_run()
assert ts.nottruish("None"), ts.get_last_run()

assert ts.catch("1/0", ZeroDivisionError("division by zero")), ts.get_last_run()


ts = pdq.WriterTestSuite("setup-and-run", parent=test_suite)

ts.equals("4", 4)
ts.equals("'four'", "four")
ts.equals("{}", {})
ts.equals("[]", [])
ts.equals("()", ())
ts.equals("None", None)

ts.ne("4", 5)
ts.ne("5.0", 6)

ts.lt("'a'", 'b')
ts.lt("False", True)

ts.ge("'a'", '_')
ts.ge("7", 7)

ts.gt("'a'", '_')
ts.gt("7", 5)

ts.le("'a'", 'a')
ts.le("4", 5)

ts.issame("None", None)
ts.issame("type(1)", int)

ts.notsame("None", False)
ts.notsame("type(1.0)", int)

ts.contains("(1,2,3)", 2)
ts.has("2", (1,2,3))
ts.notcontains("(1,2,3)", 4)
ts.nothas("5", (1,2,3))

ts.instance("5", int)
ts.notinstance("5", float)

ts.subclass("int", object)
ts.notsubclass("float", type)

ts.truish("57")
ts.nottruish("None")

ts.catch("1/0", ZeroDivisionError("division by zero"))

#print(ts.name, 'after setup', ts.tests)
test_suite.run_tests()
test_suite.summary()

