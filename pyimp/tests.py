

import pdq

test_suite = pdq.WriterTestSuite("root")

ts = pdq.WriterTestSuite("using-assert", parent=test_suite)

assert ts.isequal("4", 4), ts.get_last_run()
assert ts.isequal("'four'", "four"), ts.get_last_run()
assert ts.isequal("{}", {}), ts.get_last_run()
assert ts.isne("4", 5), ts.get_last_run()
assert ts.islt("False", True), ts.get_last_run()
assert ts.isge("7", 7), ts.get_last_run()
assert ts.isgt("7", 5), ts.get_last_run()
assert ts.isle("4", 5), ts.get_last_run()
assert ts.issame("None", None), ts.get_last_run()
assert ts.issame("type(1)", int), ts.get_last_run()
assert ts.notsame("type(1.0)", int), ts.get_last_run()
assert ts.iscontaining("(1,2,3)", 2), ts.get_last_run()
assert ts.isin("2", (1,2,3)), ts.get_last_run()
assert ts.notcontaining("(1,2,3)", 4), ts.get_last_run()
assert ts.notin("5", (1,2,3)), ts.get_last_run()
assert ts.isinstance("5", int), ts.get_last_run()
assert ts.notinstance("5", float), ts.get_last_run()
assert ts.issubclass("int", object), ts.get_last_run()
assert ts.notsubclass("float", type), ts.get_last_run()
assert ts.istruish("57"), ts.get_last_run()
assert ts.nottruish("None"), ts.get_last_run()
assert ts.isthrowing("1/0", ZeroDivisionError), repr(ts.get_last_run())

ts = pdq.WriterTestSuite("setup-and-run", parent=test_suite, verbosity=4)

ts.add("isequal", "4", 4)
ts.add("isequal", "'four'", "four")
ts.add("isequal", "{}", {})
ts.add("isne", "4", 5)
ts.add("islt", "False", True)
ts.add("isge", "7", 7)
ts.add("isgt", "7", 5)
ts.add("isle", "4", 5)
ts.add("issame", "None", None)
ts.add("issame", "type(1)", int)
ts.add("notsame", "type(1.0)", int)
ts.add("iscontaining", "(1,2,3)", 2)
ts.add("isin", "2", (1,2,3))
ts.add("notcontaining", "(1,2,3)", 4)
ts.add("notin", "5", (1,2,3))
ts.add("isinstance", "5", int)
ts.add("notinstance", "5", float)
ts.add("issubclass", "int", object)
ts.add("notsubclass", "float", type)
ts.add("istruish", "57")
ts.add("nottruish", "None")
ts.add("isthrowing", "1/0", ZeroDivisionError)

test_suite.run_tests()
test_suite.report(True)
test_suite.summary()


