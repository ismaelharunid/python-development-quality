
import pdq
from pdq.events import Event, EventListener, StopPropagation

ts = pdq.WriterTestSuite("events", verbosity=4)
ts.add_setup("""
from pdq.events import Event, EventListener, StopPropagation
evts = EventListener("eventtype")
""")

ts.add('israising', 'Event()', Exception)
ts.add('israising', 'Event(86, lambda *args,**largs: None)', Exception)
ts.add('israising', 'Event("eventtype")', Exception)
ts.add('notraising', 'Event("eventtype", lambda *args,**largs: None)', Exception)
ts.add('isinstance', 'Event("eventtype", lambda *args,**largs: None)', Event)

ts.add('notraising', 'evts.on("eventtype", lambda *args,**largs: None)', Exception)

ts.run_tests()
ts.report()
ts.summary()
