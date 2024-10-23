import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    """
        Returns the number of vowels (a, e, i, o, u) in the input string.

        Input:
        - s: A string to check for vowels.

        Output:
        - An integer representing the number of vowels in the string.
        """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Part 2
def short_lists(lst: list[list[int]]) -> list[list[int]]:
    """
    Filters the input list and returns lists of length 2.
    Input: lst (list[list[int]]) - list of lists of integers
    Output: (list[list[int]]) - list containing only lists of length 2
    """
    return [sublist for sublist in lst if len(sublist) == 2]

# Part 3
def ascending_pairs(lists: list[list[int]]) -> list[list[int]]:
    """
    Returns a list where sublists of length 2 are sorted in ascending order.

    Input:
    - lists: A list of lists of integers.

    Output:
    - A new list where any sublist of length 2 has its elements sorted
      in ascending order. Other sublists remain unchanged.
    """
    return [sorted(lst) if len(lst) == 2 else lst for lst in lists]

# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def __eq__(self, other):
        return self.dollars == other.dollars and self.cents == other.cents

def add_prices(price1: Price, price2: Price) -> Price:
    """
    Adds two prices and returns the sum as a new Price object.
    Input: price1, price2 (Price) - price objects
    Output: (Price) - new price object with normalized cents
    """
    total_cents = price1.dollars * 100 + price1.cents + price2.dollars * 100 + price2.cents
    return Price(total_cents // 100, total_cents % 100)

# Part 5
class Rectangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def rectangle_area(rect: Rectangle) -> int:
    """
    Computes the area of a rectangle based on its coordinates.
    Input: rect (Rectangle) - the rectangle with coordinates (x1, y1), (x2, y2)
    Output: (int) - the area of the rectangle
    """
    width = rect.x2 - rect.x1
    height = rect.y2 - rect.y1
    return abs(width * height)

# Part 6
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

def books_by_author(author: str, books: list[Book]) -> list[Book]:
    """
    Filters the list of books and returns the ones written by the given author.
    Input: author (str) - the author to filter by
           books (list[Book]) - list of Book objects
    Output: (list[Book]) - list of books written by the given author
    """
    return [book for book in books if book.author == author]


# Part 7
import math

class Circle:
    def __init__(self, x: int, y: int, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

def circle_bound(rect: Rectangle) -> Circle:
    """
    Computes the smallest bounding circle for a rectangle.
    Input: rect (Rectangle) - the rectangle with coordinates (x1, y1), (x2, y2)
    Output: (Circle) - the bounding circle
    """
    center_x = (rect.x1 + rect.x2) // 2
    center_y = (rect.y1 + rect.y2) // 2
    radius = math.sqrt(((rect.x2 - rect.x1) / 2) ** 2 + ((rect.y2 - rect.y1) / 2) ** 2)
    return Circle(center_x, center_y, radius)

# Part 8
class Employee:
    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay


def below_pay_average(employees: list[Employee]) -> list[str]:
    """
    Returns a list of employee names who are paid below the average pay.
    Input: employees (list[Employee]) - list of Employee objects
    Output: (list[str]) - list of employee names paid below average
    """
    if not employees:
        return []

    average_pay = sum(employee.pay for employee in employees) / len(employees)
    return [employee.name for employee in employees if employee.pay < average_pay]
