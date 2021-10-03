######################################################################
# This module contains the class used to merge 2 distillation profiles
# into one based on a mixture and volume provided. Uses an average of the
# to come up with one distillation profile
#######################################################################
#### define all static variables here ####
# name of the AWS lamda enviroment
def getAwsEnvir():
    return ("AWS_EXECUTION_ENV")


#### Packages to import ####
import os
import decimal
import numpy
# import different lib based on if it running it is running on AWS Lamda
# or not
if os.environ.get(getAwsEnvir()) is not None:
    import boto3
    import json
else:
    import pandas as pd

#this function checks if a value can be converted into a float or not
# returns true or false
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


# this class is used to calculate the distillation profile of a mixture
# of 2 distillation profile.
#   This class has 2 Methods
#       getProfile outputs the distillation profile based on the name in the filepath
#           The inputs should be treated as object and key if serveless as lamda has
#           has S3 files avaliable
#           Inputs: path, name
#           Output: dataframe of profile
#       getDistMix outputs the distillation profile of 2 distillation profiles
#           based on volumne and distillation profiles
#           Inputs: profile1, vol1 profile2, vol2
#           Output: a dataframe if class is on local machine and a json table if serverless

class dist_mix():
    # the class should behave differently when it is on Lamda
    # compared to when it is not check to see if it is running in
    # lamda

    def getProfile(self, path, name):

        # validate inputs
        assert isinstance(path, str) == True, "path must be a string"
        assert len(path) > 0, "path length must be greater then 0"
        assert isinstance(name, str) == True, "path must be a string"
        assert len(name) > 0, "path length must be greater then 0"

        # check if running on AWS or not
        if os.environ.get(getAwsEnvir()) is not None:
            ## for running on lamda
            try:
                s3 = boto3.client('s3')
                resp = s3.get_object(Bucket=path, Key=name)
                csvStr = resp['Body'].read().decode('utf-8-sig')
                # return csvStr
                rows = csvStr.split("\r\n")
                data = []
                for row in rows:
                    data.append(row.split(','))
                return data

            except Exception as err:
                return err

        else:
            # import csv based on file name
            if name[-3:] == 'csv':
                data = pd.read_csv(path + '/' + name, index_col=False)
                return data
            else:
                raise ValueError('the name must be a csv')

    # this method returns the DistMix based on the values from 2 Profiles
    # and there respective volumes. inputs are profile1, vol1, profile2
    # and vol2. when the function runs on Lambda inputs are 2D arrays and output
    # is a 2D arrays
    # running on a local machine it is dataframes and the output is a dataframe
    def getDisMix(self, profile1, vol1, profile2, vol2):

        assert isinstance(vol1, float) or isinstance(vol1, int) == True, "vol1 must be a numeric value"
        assert isinstance(vol2, float) or isinstance(vol2, int) == True, "vol2 must be a numeric value"

        # convert dataframe or array into a numpy array
        if os.environ.get(getAwsEnvir()) is not None:
            assert isinstance(profile1, list), "profile1 must be a list"
            assert isinstance(profile2, list), "profile2 must be a list"
            profile1 = numpy.array(profile1)
            profile2 = numpy.array(profile2)
        else:
            assert isinstance(profile1, pd.DataFrame), "profile1 must be a dataframe"
            assert isinstance(profile2, pd.DataFrame), "profile2 must be a dataframe"
            profile1 = numpy.asarray([profile1.columns.values.tolist()] + profile1.values.tolist())
            profile2 = numpy.asarray([profile2.columns.values.tolist()] + profile2.values.tolist())

        #make sure the 2 arrays are the same length
        assert len(profile1) == len(profile2), "Profile 1 len is " \
                + str(len(profile1[1])) + " profile 2 length is " + str(len(profile2[1]))

        #join the 2 arrays into one
        profileJ = numpy.concatenate((profile1, profile2), axis=1)

        #loop to calc a waited average for any numeic row in the Temperature (C) column
        #which is always the second column
        data = []
        vol1per = float(vol1 / (vol1+vol2))
        vol2per = float(vol2 / (vol1+vol2))
        i = 0
        for vol in profileJ:
            if isfloat(vol[1]) == True and isfloat(vol[3]) == True:
                wavg = round((vol1per * float(vol[1])) + (vol2per * float(vol[3])),2)
                data.append([vol[0], wavg])
            elif i == 0:
                data.append([vol[0],vol[1]])
            else:
                data.append([vol[0],"-"])
            i = i + 1

        if os.environ.get(getAwsEnvir()) is not None:
            return data
        else:
            output = pd.DataFrame(data[1:], columns=data[0])
            return output


if __name__ == '__main__':
    dist = dist_mix()
    path = 'C:\\Users\\Hadi-PC\\Desktop\\distillation profiles'
    name1 = 'syncrude sweet premium.csv'
    name2 = 'pembina.csv'
    profile1 = dist.getProfile(path,name1)
    profile2 = dist.getProfile(path, name2)
    distMix = dist.getDisMix(profile1,10,profile2,20)
    print(distMix)
