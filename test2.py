import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

   def test_first_last_name(self):
       result = formatted_name("pete", "seeger")
       self.assertEqual(result, "Pete Seeger")
