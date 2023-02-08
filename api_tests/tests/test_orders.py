from api_tests.requests.orders import *
from api_tests.requests.api_clients import *

class TestOrders:

    def setup_method(self):
        self.token = get_token()

    def test_add_valid_order(self):
        response = add_order(self.token, 1, 'Costel')
        assert response.status_code == 201
        assert response.json()['created'] is True
        # clean up
        delete_order(self.token, response.json()['orderId'])

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'Costel')
        assert response.status_code == 404, 'Status code should be 404'
        assert response.json()['error'] == 'This book is not in stock. Try again later.'

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'user1')
        add2 = add_order(self.token, 1, 'user2')
        response = get_orders(self.token)
        assert response.status_code == 200
        assert len(response.json()) == 2

        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token, 1, 'Costel')
        response = delete_order(self.token, add.json()['orderId'])
        assert response.status_code == 204, 'Status code should be 204'

        get_all = get_orders(self.token)
        assert len(get_all.json()) == 0, 'Orders should be 0'

    def test_delete_invalid_order_id(self):
        response = delete_order(self.token, 'dasdadaw')
        assert response.status_code == 404, 'Status code should be 404'
        assert response.json()['error'] == 'No order with id dasdadaw.'

    def test_get_one_order(self):
        order_id = add_order(self.token, 1, 'user1').json()['orderId']
        response = get_order(self.token, order_id)
        assert response.status_code == 200, 'Status code should be 200'
        assert response.json()['id'] == order_id
        assert response.json()['bookId'] == 1
        assert response.json()['customerName'] == 'user1'
        assert response.json()['quantity'] == 1

        delete_order(self.token, order_id)

    def test_get_invalid_order_id(self):
        response = get_order(self.token, '112312123')
        assert response.status_code == 404, 'Status code should be 404'
        assert response.json()['error'] == 'No order with id 112312123.'

    def test_update_invalid_order_id(self):
        response = edit_order(self.token, '1231412', 'Costel')
        assert response.status_code == 404, 'Status code should ne 404'
        assert response.json()['error'] == 'No order with id 1231412.'

    def test_update_valid_order_id(self):
        order_id = add_order(self.token, 1, 'Costi').json()['orderId']
        response = edit_order(self.token, order_id, 'Costel12')
        assert response.status_code == 204, 'Status code should be 204'
        get = get_order(self.token, order_id)
        assert get.json()['customerName'] == 'Costel12'

        delete_order(self.token, order_id)