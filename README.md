# Merging

Your task in this exercise is to implement a merge of two sorted lists. We will assume that they are integers, but they could be lists of any type that we can put an order on. If we have lists `x` and `y` we want another list, `z`, such that `z = sorted(x + y)`. Don't use that code for it, though. For reasons that we get to next week, concatenating two lists and then sorting them is generally slower than merging them. (Generally, it depends on other things as well, and you might find that your merge implementation is slower than the code above; there are other reasons for that, however, that we can talk about at the exercises).

## Functions

In this exercise we will use a “function” for our code. Why functions are useful, and the fascinating details of how they work, is something we cover in detail later. For now, all you need to know is that a function looks something like this

```python
def merge(x, y):
    """A comment describing the function."""
    # the code that will be run when you call the function
	return z  # what the function returns
```

The documentation comment at the top can be left out, but it is considered good practise to document all functions that you expect others to be able to use.

In the code I provide, you will see functions that look a tiny bit more complicated than above (and in the book). The function `merge` in `src/merge.py` that I want you to implement, looks like this:

```python
def merge(x: list[int], y: list[int]) -> list[int]:
    """A comment describing the function."""
    # the code that will be run when you call the function
	return z  # what the function returns
```

The `list[int]` bits are *type annotations*. You can ignore them; Python does. It is a form of documentation that some tools use to check that you are using functions on the right kind of objects. We won't talk much about types in this class, since these type annotations aren't necessary in Python and can get a little complicated, but I have included them because it is good practise. If you want to use them yourself, you can pick up the basics from the examples, but the full details would take about as long as the full class as it is now. (Type theory can get a bit complicated).

The annotation here just says that `merge` should take two lists of integers (`list[int]`) and it will return a list of integers in return `-> list[int]`. Your editor might give you a warning if you try to use `merge` on other types of objects, but Python itself won't (but might crash if you use an object in a way you shouldn't).


To use a function to merge two lists, you use syntax you have already seen

```python
z = merge(x, y)
```

We will use functions in exercises from now on, even though we don't fully understand them yet, because they give us a convinient way to document and test our code. We will generally use two different ways of testing our code: [doctest](https://docs.python.org/3/library/doctest.html) and [pytest](https://docs.pytest.org/en/7.1.x/). You don't have to worry about how this works yet, because I have already set up the tests for your exercises. If you want to know if your code runs to specification, you can use the command


```sh
> python3 -m doctest src/*.py && python3 -m pytest src
```

in your terminal and it will let you know if there are any errors. (If you run it now, before you have done the exercise, you should get an error. There is nothing wrong with having tests that fail, [some consider it a good approach to programming,](https://en.wikipedia.org/wiki/Test-driven_development), that will just guide you to what needs to be done, and when the tests pass, you know that you are done--for now at least).

In all your projects, I will use this command (and a few others) to check if you have solved the problem at hand. When you commit a solution to GitHub it is automatically run, and you can see the result in the `Actions` tab. So, now you know how those tests are run. Running the tests on the command line are easier than committing, pushing, and checking at GitHub, of course.


To implement a function, you write code after the documentation string. You need to indent your code to the same level as the string (the same way that you have to indent code in `if`-blocks or `for`-loops), but otherwise there is nothing special about code in a function and code outside.

## Implementing `merge(x,y)`

Open `src/merge.py`. You will find a function that looks like this:

```python
def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []  # a new list to copy elements into
    # FIXME: fill out the loop so you merge the lists
    # until one of them is empty
    while i < len(x) and j < len(y):
        break # FIXME: you shouldn't just break here
    # FIXME: At least one of the lists is empty now. Copy the
    # remainder of the other into z.
    return z
```

You need to fill out the `while` loop and the bit after it. If you have done so correctly, the test command I showed you above should tell you that everything is fine.

