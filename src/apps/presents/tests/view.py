from django.test import TestCase, Client
from django.core.urlresolvers import reverse
class PresentViewTestCase(TestCase):
    """ Test cases for presents app views """

    def setUp(self):
        return

    def test_createView(self):
        """ Test create view. """
        client = Client(enforce_csrf_checks=True)
        response = client.get(reverse('present-add'))
        self.assertEqual(response.status_code, 302)
