######################################################################
# this module contains the unit test for the dist_mix class
#######################################################################

import unittest
from distillation_mix import dist_mix
import pandas as pd
# this class is used to test the dist_mix class
class dist_test(unittest.TestCase):

    ########### Unit test Method getProfile #####################
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

    # This test case checks if a file path is invalid or not
    # if it is invalid a FileNotFoundError should be raised
    def test_4(self):
        path = 'C:/hadi'
        name = 'doesnt_exist.csv'
        dist = dist_mix()
        with self.assertRaises(FileNotFoundError):
            dist.getProfile(path,name)

    #Test if a dataframe is returned when a valid profile name is given
    def test_5(self):
        path = 'C:\\Users\\Hadi-PC\\Desktop\\distillation profiles'
        name = 'bc light.csv'
        dist = dist_mix()
        profile = dist.getProfile(path, name)
        dfCheck = isinstance(profile, pd.DataFrame)
        self.assertEqual(dfCheck,True,"Output must be a data frame")

    ########### Unit test Method getDistMix #####################

    # This test is to determine if an AssertionError is raised when
    # volumes are not numeric values
    def test_6(self):
        vol1 = 'x'
        vol2 = 'x'
        profile1 = 'xxxxx'
        profile2 = 'xxxxx'
        dist = dist_mix()
        with self.assertRaises(AssertionError):
            dist.getDisMix(profile1,vol1,profile2,vol2)

    # This test is to make sure that assertion for dataframe is based
    # when entering profiles into the method
    def test_7(self):
        vol1 = 12
        vol2 = 12
        profile1 = 'xxxxx'
        profile2 = 'xxxxx'
        dist = dist_mix()
        with self.assertRaises(AssertionError):
            dist.getDisMix(profile1,vol1,profile2,vol2)

    # This test is used to determine if the 2 arrays used in the calcaulation are the same
    # length
    def test_8(self):
        profile1 = {'Per':[1, 1, 3] ,
                    'Temp': [1, 72, 23] }
        profile2 = {'Per':[1, 1, 3, 24] ,
                    'Temp': [1, 72, 23, 34] }
        vol1 = 12
        vol2 = 12
        dist = dist_mix()
        with self.assertRaises(AssertionError):
            dist.getDisMix(pd.DataFrame(profile1), vol1,
                           pd.DataFrame(profile2), vol2)

    # This test is to validate the weighted average calculation for distillation
    # profile using test dataframes.
    def test_9(self):

        profile1 = {'Per': [5],
                    'Temp': [12]}
        profile2 = {'Per': [5],
                    'Temp': [1]}

        profile1 = pd.DataFrame(profile1)
        profile2 = pd.DataFrame(profile2)
        vol1 = 12
        vol2 = 18

        vol1per = vol1 / (vol1 + vol2)
        vol2per = vol2 / (vol1 + vol2)

        answer = (vol1per * profile1['Temp'][0]) + (vol2per * profile2['Temp'][0])

        dist = dist_mix()
        mOutput = dist.getDisMix(profile1, vol1,
                       profile2, vol2)

        self.assertEqual(answer,mOutput['Temp'][0],"The method is yielding the incorrect weighted average")
        #print()


if __name__ == '__main__':
    unittest.main()

