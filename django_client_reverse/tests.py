from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from uuid import uuid4


class ReverserTestCase(APITestCase):
    def setUp(self):
        super().setUp()

    def test_reverser(self):
        response = self.client.post(reverse('reverser'), data={'ident': 'tests:root'})
        self.assertEqual(response.data, reverse('tests:root'))

    def test_invalid(self):
        response = self.client.post(reverse('reverser'), data={'ident': 'tests:not_a_thing'})
        self.assertEqual(response.status_code, 404)

    def test_kwrgs_pass(self):
        kwargs = {'uuid': str(uuid4())}
        response = self.client.post(reverse('reverser'), data={
            'ident': 'tests:uuid',
            'kwargs': kwargs
        }, format="json")
        self.assertEqual(response.data, reverse('tests:uuid', kwargs=kwargs))

    def test_args_pass(self):
        args = (str(uuid4()),)
        response = self.client.post(reverse('reverser'), data={
            'ident': 'tests:uuid',
            'args': args
        }, format="json")
        self.assertEqual(response.data, reverse('tests:uuid', args=args))
