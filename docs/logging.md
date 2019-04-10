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
```

#### Disclaimers

* n/a

Sources: [_Socratica_](https://youtu.be/g8nQ90Hk328)