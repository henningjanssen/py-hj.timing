# hj.timing
Minimalistic timing class that passes the results to a callback.

```py
from hj.timing import Timer, json_format

# With a context
with Timer('mytimer', logger=print, format=json_format):
  do_expensive_task()

# without a context, with an outside data-container
from hj.timing import TimingData
tdata = TimingData()
timer = TimingData(timing_container=tdata)
timer.start()
do_expensive_task()
timer.stop()
do_stuff_with_the_timing_data(tdata)
```
