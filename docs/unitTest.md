## Unit Tests

#### Usage

* test results of a script
* create a test_script.py or a script_test.py file to hold your unit test
* after script.py and test_script.py is implemented, run in cmd: 
```python
python -m unittest test_script
```
* check assert methods

#### Examples

```python
# example 1
# the below exists in test_script.py
# which tests the circle_area method created in script.py
import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    # test areas when radius >= 0
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)
    
    # make sure value errors are raised when necessary
    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        
    # make sure type errors are raised when necessary
    def test_types(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
```

#### Disclaimers

* n/a

Sources: [_Socratica_](https://youtu.be/1Lfv5tUGsn8)