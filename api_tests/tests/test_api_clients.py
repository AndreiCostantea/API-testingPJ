from api_tests.requests.api_clients import *

class TestApiClient:

    nr = randint(1,9999999)
    clientName = 'Costel24'
    clientEmail = f'emailValid{nr}@mailinator.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

    def test_successful_login(self):
        assert self.response.status_code == 201, 'Status code is not correct'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in response keys'

    def test_login_client_registered(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'Status code should be 409'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'

    def test_invalid_email(self):
        self.response = login('Costel', 'afsgfra')
        assert self.response.status_code == 400, 'Staus code should be 400'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Error message is incorrect'
