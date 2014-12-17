from django.test import TestCase

class LoginTests(TestCase):

    def test_access_mytribe_without_being_logged_in_redirects_to_login(self):
        response = self.client.get('/mytribe/')

        self.assertRedirects(response, expected_url='/accounts/login/?next=/mytribe/', status_code=302, target_status_code=200, msg_prefix='')


