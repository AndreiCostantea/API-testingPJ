from api_tests.requests.books import *

class TestBooks:

    def test_status_code(self):
        response = get_books()
        assert response.status_code == 200, 'status code should be 200'

    def test_get_all_books(self):
        response = get_books()
        assert len(response.json()) == 6, 'Total number of books should be 6'
        for book in response.json():
            assert 'id' in book.keys()
            assert 'available' in book.keys()
            assert 'name' in book.keys()
            assert 'type' in book.keys()

    def test_get_books_invalid_type(self):
        response = get_books(book_type='horror')
        assert response.status_code == 400, 'Status code should be 400'
        assert response.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_get_books_invalid_limit(self):
        response = get_books(limit=24)
        assert response.status_code == 400, 'Status code should be 400'
        assert response.json()['error'] == "Invalid value for query parameter 'limit'. Cannot be greater than 20."

    def test_get_books_limit(self):
        response = get_books(limit=4)
        assert len(response.json()) == 4, 'Total numbers of books shouls be 4'

    def test_get_all_fiction_books(self):
        response = get_books(book_type='fiction')
        for book in response.json():
            assert book['type'] == 'fiction', 'Book type should be fiction'

    def test_get_all_books_type_limit(self):
        response = get_books(limit=2, book_type='fiction')
        assert len(response.json()) == 2, 'Number of books should be 2'
        for book in response.json():
            assert book['type'] == 'fiction', 'Book type should be fiction'

    def test_get_book(self):
        response = get_book(4)
        assert response.status_code == 200, 'Status should be 200'
        assert response.json()['id'] == 4, 'Book ID should be 4'

    def test_get_book_wrong_id(self):
        response = get_book(24)
        assert response.status_code == 404, 'Status code should be 404'
        assert response.json()['error'] == "No book with id 24", 'Error message wrong'