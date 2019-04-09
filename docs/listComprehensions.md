## List Comprehensions

#### Usage

* build a simple list
* [_expr_ for _val_ in _collection_]
* [_expr_ for _val_ in _collection_ if _test_]
* [_expr_ for _val_ in _collection_ if _test_ and _test2_]
* [_expr_ for _val_ in _collection_ if _test_ and _val2_ in _collection2_]

#### Examples

```python
# example 1
squares = [i**2 for i in range(1,101)]

# example 2
# from movies, creates a list of movies that start with "G"
movies = ["Citizen Kane", "Groundhog Day"]
gmovies = [_title_ for _title_ in _movies_ if _title.startswith("G")_]

# example 3
# from movies, creates a list of movies that are before 2000
movies = [("Citizen Kane", 1941), ("Spirited Away", 2001)]
pre2k = [_title_ for (_title_, _year_) in _movies_ if _year_ _<_ _2000_]
```

#### Disclaimers

* n/a

Sources: _Socratica_