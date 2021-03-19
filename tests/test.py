import unittest
import xmlrunner

class TestStringMethods(unittest.TestCase):
  def test_lstrip(self): #testing for left stripping
    self.assertEqual('   hello '.lstrip(),'hello ')
  def test_isupper(self): #testing for isupper
    self.assertTrue('HELLO'.isupper())
    self.assertFalse('HELlO'.isupper())
    
if __name__=='__main__':
  unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    # these make sure that some options that are not applicable
    # remain hidden from the help menu.
    failfast=False, buffer=False, catchbreak=False)
