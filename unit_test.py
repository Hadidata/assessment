######################################################################
# this module contains the unit test for the dist_mix class
#######################################################################

import unittest
from distillation_mix import dist_mix
# this class is used to test the dist_mix class
class dist_test(unittest.TestCase):

    # This test case checks if an Assertion error is
    # being raised by the function for sending non-string values
    def test_1(self):
        path = 1212
        name = 1212
        dist = dist_mix()
        with self.assertRaises(AssertionError):
            dist.getProfile(path, name)

    #This test case checks if an Assertion error is
    #being raised by the function for sending an empty strings
    def test_2(self):
        path = ''
        name = ''
        dist = dist_mix()
        with self.assertRaises(AssertionError):
            dist.getProfile(path, name)

    #This test case checks if a value error is raised
    #when sending a name with no csv end at the end of the string
    def test_3(self):
        path = 'xxx'
        name = 'xxx'
        dist = dist_mix()
        with self.assertRaises(ValueError):
            dist.getProfile(path,name)



if __name__ == '__main__':
    unittest.main()

