"""Tests are defined here"""
from django.test import TestCase, Client


class TwitterApiTestCase(TestCase):
    """Unit tests for Twitter API requests"""
    def setUp(self):
        self.client = Client()

    def test_tweets_user(self):
        """Status code should be 200 and results should include the username"""
        response = self.client.get('/users/twitter/?limit=1', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['username'].lower(), 'twitter')

    def test_tweets_hashtag(self):
        """Status code should be 200 and results should include the hashtag"""
        response = self.client.get('/hashtags/python/?limit=1', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('python' in response.json()[0]['content'].lower())

    def test_limit_default(self):
        """Default limit should return 30 results"""
        response = self.client.get('/users/twitter/', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 30)

    def test_limit_invalid(self):
        """Invalid limit input should be ignored and defaulted to 30"""
        response = self.client.get('/users/twitter/?limit=0', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 30)
        response = self.client.get('/users/twitter/?limit=foobar', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 30)
