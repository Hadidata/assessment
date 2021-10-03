##############################################
# This Module is used to invoke the Lamda
# functions for python
##############################################

from distillation_mix import dist_mix

def getProfile(event, context):
    bucket = 'validere-assessment'
    key = 'bc light.csv'

    dist = dist_mix()
    profile = dist.getProfile(bucket,key)
    return(profile)


