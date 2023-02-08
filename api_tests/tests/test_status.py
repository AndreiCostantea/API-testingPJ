from api_tests.requests.status import *

class TestStatus:

    def test_get_status_code(self):
        status_code = get_status().status_code
        assert status_code == 200, 'Status code should be 200'

    def test_get_status_body(self):
        status = get_status().json()
        assert 'status' in status.keys(), 'Cheia status nu exista'
        assert status['status'] == 'OK', 'Status message should be "OK"'
