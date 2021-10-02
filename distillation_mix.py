######################################################################
# This module contains the class used to merge 2 distillation profiles
# into one based on a mixture and volume provided. Uses an average of the
# to come up with one distillation profile
#######################################################################

import pandas as pd
import boto3
import os

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

    def getProfile(self,path,name):

        #validate inputs
        assert isinstance(path,str) == True, "path must be a string"
        assert len(path) > 0, "path length must be greater then 0"
        assert isinstance(name, str) == True, "path must be a string"
        assert len(name) > 0, "path length must be greater then 0"

        #check if running on AWS or not
        if os.environ.get("AWS_EXECUTION_ENV") is not None:
            ## for running on lamda
            try:
                s3 = boto3.client('s3')
                resp = s3.get_object(Bucket=path,Key=name)
                data = pd.read_csv(resp['Body'],sep=',',index_col=False)
                return(data)
            except Exception as err:
                return(err)

        else:
            # import csv based on file name
            if name[-3:] == 'csv':
                data = pd.read_csv(path + '/' + name,index_col=False)
                return(data)
            else:
                raise ValueError ('the name must be a csv')


    def getDisMix(self,profile1,vol1,profile2,vol2):

        if os.environ.get("AWS_EXECUTION_ENV") is not None:
            pass
        else:
            pass

