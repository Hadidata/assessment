##############################################
# This Module is used to invoke the Lamda
# functions for python
##############################################

from distillation_mix import dist_mix
import json

def bucketName():
    return 'validere-assessment'

# this is the lambda function to get a distilaltion profile from the API
# requires the product name
def getProfile(event, context):
    name = event['name'] + '.csv'

    dist = dist_mix()
    profile = dist.getProfile(bucketName(),name)
    return(json.dumps(profile))

# this is the lambda function to get the distillation profile
# for 2 distillation via a weighted average requires the input
# name1, vol1, name2, vol2
def getDisMix(event,context):
    name1 = event['name1'] + '.csv'
    name2 = event['name2'] + '.csv'
    vol1 = event['vol1']
    vol2 = event['vol2']

    dist = dist_mix()
    profile1 = dist.getProfile(bucketName(), name1)
    profile2 = dist.getProfile(bucketName(), name2)

    disMix = dist.getDisMix(profile1,vol1,profile2,vol2)

    return(json.dumps(disMix))




