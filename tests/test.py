import unittest
import xmlrunner

class TestStringMethods(unittest.TestCase):
  def test_lstrip(self): #testing for left stripping
    self.assertEqual('   hello '.lstrip(),'hello ')
  def test_isupper(self): #testing for isupper
    self.assertTrue('HELLO'.isupper())
    self.assertFalse('HELlO'.isupper())
  def test_isTrue(self):
    self.assertTrue(1*1*1)
  def test_isFalse(self):
    self.assertTrue(0)
    
if __name__=='__main__':
  unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    failfast=False, buffer=False, catchbreak=False)
