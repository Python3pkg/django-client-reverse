from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from uuid import uuid4
from .test_urls import PASS_TEXT


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

    def test_invalid_kwargs(self):
        kwargs = {'not_uuid': str(uuid4())}
        response = self.client.post(reverse('reverser'), data={
            'ident': 'tests:uuid',
            'kwargs': kwargs
        }, format="json")
        self.assertEqual(response.status_code, 404)

    def test_multi_kwargs(self):
        kwargs = {
            'uuid': str(uuid4()),
            'pk': str(uuid4())
        }
        response = self.client.post(reverse('reverser'), data={
            'ident': 'tests:multi',
            'kwargs': kwargs
        }, format="json")
        self.assertEqual(response.data, reverse('tests:multi', kwargs=kwargs))

    def test_multi_args(self):
        args = (str(uuid4()), str(uuid4()))
        response = self.client.post(reverse('reverser'), data={
            'ident': 'tests:multi',
            'args': args
        }, format="json")
        self.assertEqual(response.data, reverse('tests:multi', args=args))

    def test_url_valid(self):
        lookup_response = self.client.post(reverse('reverser'), data={'ident': 'tests:root'})
        response = self.client.get(lookup_response.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, PASS_TEXT)
