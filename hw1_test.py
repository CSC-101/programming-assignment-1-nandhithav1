from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, books_by_author, circle_bound, below_pay_average, Price, Rectangle, Book, Circle, Employee

# Write your test cases for each part below.


    # Part 1
    def test_vowel_count_hello():
        assert vowel_count("Hello") == 2

    def test_vowel_count_uppercase():
        assert vowel_count("AEIOU") == 5

    # Part 2
    def test_short_lists_mixed():
        assert short_lists([[1, 2], [3, 4, 5], [6, 7]]) == [[1, 2], [6, 7]]

    def test_short_lists_single_and_empty():
        assert short_lists([[1], [2, 3], []]) == [[2, 3]]

    # Part 3
    def test_ascending_pairs_mixed(self):
        assert ascending_pairs([[3, 2], [1], [5, 4]]) == [[2, 3], [1], [4, 5]]

    def test_ascending_pairs_unsorted(self):
        assert ascending_pairs([[9, 8], [6, 5], [3, 7]]) == [[8, 9], [5, 6], [3, 7]]

    # Part 4
    def test_add_prices_normal(self):
        assert add_prices(Price(2, 50), Price(1, 75)) == Price(4, 25)

    def test_add_prices_edge(self):
        assert add_prices(Price(3, 10), Price(0, 95)) == Price(4, 5)

    # Part 5
    def test_rectangle_area_basic(self):
        assert rectangle_area(Rectangle(0, 0, 3, 4)) == 12

    def test_rectangle_area_negative_coordinates(self):
        assert rectangle_area(Rectangle(-3, -4, 0, 0)) == 12

    # Part 6
    def test_books_by_author_single_match():
        books = [Book("Book 1", "Author A"), Book("Book 2", "Author B")]
        assert books_by_author("Author A", books) == [books[0]]

    def test_books_by_author_no_match():
        books = [Book("Book 1", "Author A"), Book("Book 2", "Author B")]
        assert books_by_author("Author C", books) == []


    # Part 7
    def test_circle_bound_basic():
        rect = Rectangle(0, 0, 4, 3)
        circle = circle_bound(rect)
        assert circle.x == 2 and circle.y == 1 and round(circle.radius, 2) == 2.5

    def test_circle_bound_square():
        rect = Rectangle(0, 0, 2, 2)
        circle = circle_bound(rect)
        assert circle.x == 1 and circle.y == 1 and round(circle.radius, 2) == 1.41

    # Part 8
    def test_below_pay_average_basic():
        employees = [Employee("John", 5000), Employee("Jane", 3000), Employee("Doe", 4000)]
        assert below_pay_average(employees) == ["Jane"]

    def test_below_pay_average_empty():
        employees = []
        assert below_pay_average(employees) == []



