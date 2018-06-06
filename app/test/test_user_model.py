import unittest
from app.models import  User

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User(password='123')
		self.assertTrue(u.password_hash is not None)
	def test_no_passowrd_getter(self):
		u = User(password='123')
		with self.assertRaises(AttributeError):
			u.password
	def test_password_verification(self):
		u = User(password='123')
		self.assertTrue(u.verify_password('123'))
		self.assertFalse(u.verify_password('111'))
	def test_password_salts_are_random(self):
		u = User(password='123')
		u1 = User(password='123')
		self.assertTrue(u.password_hash != u1.password_hash)
