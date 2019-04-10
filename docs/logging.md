## Logging

#### Usage

* record progress and problems
* 5 levels - Debug < Info < Warning < Error < Critical
* set level depending on what level of messages needed

| Level        | Numeric Value |
|:-------------|:--------------|
| NOTSET       | 0             |
| DEBUG        | 10            |
| INFO         | 20            |
| WARNING      | 30            |
| ERROR        | 40            |
| CRITICAL     | 50            |

#### Examples

```python
# example 1
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\python\\lumberjack.log",
					level = logging.DEBUG,
					format = LOG_FORMAT,
					filemode = 'w')
logger = logging.getLogger()

logger.debug("this is a debug message")
logger.info("this is a info message")
logger.warning("this is a warning message")
logger.error("this is a error message")
logger.critical("this is a critical message")

def quadraticFormula(a, b, c):
	""" Return the solution ax^2 + bx + c = 0 """
	loggger.info("quadratic formula({0}, {1}, {2})".format(a, b, c)
	
	# Compute the discriminant
	logger.debug("# Compute the discriminant")
	disc = b**2 - 4*a*c
	
	# Compute the two roots
	logger.debug("# Compute the two roots")
	root1 = (-b + math.sqrt(disc)) / (2*a)
	root2 = (-b - math.sqrt(disc)) / (2*a)
	
	# Return the roots
	logger.debug("# Return the roots")
	return (root1, root2)
```

#### Disclaimers

* n/a

Sources: [_Socratica_](https://youtu.be/g8nQ90Hk328)