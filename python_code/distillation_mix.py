######################################################################
# This module contains the class used to merge 2 distillation profiles
# into one based on a mixture and volume provided. Uses an average of the
# to come up with one distillation profile
#######################################################################

from pandas import dataframes as df
import boto3


# this class is used to calculate the distillation profile of a mixture
# of 2 distillation profile.
#   This class has 2 Methods
#       getProfile outputs the distillation profile based on the name in the filepath
#           The inputs should be treated as object and key if serveless as lamda has
#           has S3 files avaliable
#           Inputs: path, name
#           Output: dataframe of profile
#       getDistMix outputs the distillation profile of 2 distillation profiles
#       based on volumne and distillation profiles
#           Inputs: profile1, vol1 profile2, vol2
#           Output: a dataframe if class is on local machine and a json table if serverless

class dist_mix():
    # the class should behave differently when it is on Lamda
    # compared to when it is on a local machine
    def __init__(self,serverless=True):
        pass

    def getProfiles(self,path,name):
        pass

    def getDisMix(self,profile1,vol1,profile2,vol2):
        pass


