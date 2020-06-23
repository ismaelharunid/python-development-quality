# python-development-quality
A pdq python test suite


## Simple usage

```python
>>> import pdq
>>> 
>>> test_suite = pdq.WriterTestSuite("root")
>>> 
>>> ts = pdq.WriterTestSuite("operations", parent=test_suite, verbosity=4)
>>> 
>>> assert ts.equals("4", 4), ts.get_last_run()
>>> assert ts.equals("'four'", "four"), ts.get_last_run()
>>> assert ts.equals("{}", {}), ts.get_last_run()
>>> assert ts.equals("[]", []), ts.get_last_run()
>>> assert ts.equals("()", ()), ts.get_last_run()
>>> assert ts.equals("None", None), ts.get_last_run()
>>> 
>>> assert ts.ne("4", 5), ts.get_last_run()
>>> assert ts.ne("5.0", 6), ts.get_last_run()
>>> 
>>> assert ts.lt("'a'", 'b'), ts.get_last_run()
>>> assert ts.lt("False", True), ts.get_last_run()
>>> 
>>> assert ts.ge("'a'", '_'), ts.get_last_run()
>>> assert ts.ge("7", 7), ts.get_last_run()
>>> 
>>> assert ts.gt("'a'", '_'), ts.get_last_run()
>>> assert ts.gt("7", 5), ts.get_last_run()
>>> 
>>> assert ts.le("'a'", 'a'), ts.get_last_run()
>>> assert ts.le("4", 5), ts.get_last_run()
>>> 
>>> assert ts.issame("None", None), ts.get_last_run()
>>> assert ts.issame("type(1)", int), ts.get_last_run()
>>> 
>>> assert ts.notsame("None", False), ts.get_last_run()
>>> assert ts.notsame("type(1.0)", int), ts.get_last_run()
>>> 
>>> assert ts.contains("(1,2,3)", 2), ts.get_last_run()
>>> assert ts.has("2", (1,2,3)), ts.get_last_run()
>>> assert ts.notcontains("(1,2,3)", 4), ts.get_last_run()
>>> assert ts.nothas("5", (1,2,3)), ts.get_last_run()
>>> 
>>> assert ts.instance("5", int), ts.get_last_run()
>>> assert ts.notinstance("5", float), ts.get_last_run()
>>> 
>>> assert ts.subclass("int", object), ts.get_last_run()
>>> assert ts.notsubclass("float", type), ts.get_last_run()
>>> 
>>> assert ts.truish("57"), ts.get_last_run()
>>> assert ts.nottruish("None"), ts.get_last_run()
>>> 
>>> assert ts.throws("1/0", ZeroDivisionError("division by zero")), ts.get_last_run()
>>> 
>>> 
>>> ts = pdq.WriterTestSuite("setup-and-run", parent=test_suite)
>>> 
>>> ts.equals("4", 4)
>>> ts.equals("'four'", "four")
>>> ts.equals("{}", {})
>>> ts.equals("[]", [])
>>> ts.equals("()", ())
>>> ts.equals("None", None)
>>> 
>>> ts.add("ne", "4", 5)
>>> ts.add("ne", "5.0", 6)
>>> 
>>> ts.add("lt", "'a'", 'b')
>>> ts.add("lt", "False", True)
>>> 
>>> ts.add("ge", "'a'", '_')
>>> ts.add("ge", "7", 7)
>>> 
>>> ts.add("gt", "'a'", '_')
>>> ts.add("gt", "7", 5)
>>> 
>>> ts.add("le", "'a'", 'a')
>>> ts.add("le", "4", 5)
>>> 
>>> ts.add("issame", "None", None)
>>> ts.add("issame", "type(1)", int)
>>> 
>>> ts.add("notsame", "None", False)
>>> ts.add("notsame", "type(1.0)", int)
>>> 
>>> ts.add("contains", "(1,2,3)", 2)
>>> ts.add("has", "2", (1,2,3))
>>> ts.add("notcontains", "(1,2,3)", 4)
>>> ts.add("nothas", "5", (1,2,3))
>>> 
>>> ts.add("instance", "5", int)
>>> ts.add("notinstance", "5", float)
>>> 
>>> ts.add("subclass", "int", object)
>>> ts.add("notsubclass", "float", type)
>>> 
>>> ts.add("truish", "57", )
>>> ts.add("nottruish", "None", )
>>> 
>>> ts.add("throws", "1/0", ZeroDivisionError("division by zero"))
>>> 
>>> test_suite.run_tests()
>>> test_suite.summary()
Summary for root
  [PASS] 0/0
  [FAIL] 0/0
  [ERR]  0/0
  with 2 children
    Summary for operations
      [PASS] 31/31
      [FAIL] 0/31
      [ERR]  1/31
      no children
    Summary for setup-and-run
      [PASS] 31/31
      [FAIL] 0/31
      [ERR]  1/31
      no children
```
