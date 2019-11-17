## [Python](.\python.html)
## List Comprehensions

#### Usage

* build a simple list

* list = [_expr_ for _val_ in _collection_]
* list = [_expr_ for _val_ in _collection_ if _test_]
* list = [_expr_ for _val_ in _collection_ if _test_ and _test2_]
* list = [_expr_ for _val_ in _collection_ if _test_ and _val2_ in _collection2_]

#### Examples

```python
# example 1
squares = [i**2 for i in range(1,101)]

# example 2
# from movies, creates a list of movies that start with "G"
num = [1, 2, 3]
gmovies = [str(x) for x in num if x < 2]

# example 3
# from movies, creates a list of movies that are before 2000
movies = [("Citizen Kane", 1941), ("Spirited Away", 2001)]
pre2k = [title for (title, year) in movies if year < 2000]
```

#### Disclaimers

* n/a

Sources: [_Socratica_](https://youtu.be/AhSvKGTh28Q)