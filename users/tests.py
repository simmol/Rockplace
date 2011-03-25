"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from users.models import User

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

class UserTest(TestCase):

  def setUp(self):
    self.user = User
    self.user.username = 'testuser'
    self.user.facebook_id = 'test_facebook_id'

  def testRegistration(self):
    flag = True
    try:
       User.registration()
    except AttributeError:
      flag = False

    self.assertTrue( flag, 'Registration implemented')

  def testLogin(self):
    self.assertTrue(0, 'Login not implemented')

  def testUserModel(self):
    self.assertEqual(self.user.username, 'testuser')
