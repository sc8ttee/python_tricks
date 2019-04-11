## Filter

#### Usage

* filter data

#### Examples

```python
# example 1
# remove None (e.g. "", 0, 0.0, [], (), {}, False, None)
countries = ["", "Argentina", "", "Brazil", "Chile"]
list(filter(None, countries))
```

#### Disclaimers

* when filtering None, beware of 0's. 0 is oftern valid data

Sources: [_Socratica_](https://youtu.be/hUes6y2b--0)