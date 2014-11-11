from django.test import TestCase

class LoginTestCase(TestCase):

    def test_login(self):

        # First check for the default behavior
        response = self.client.get('/admin/')
        self.assertRedirects(response, '/admin/login/?next=/admin/')

