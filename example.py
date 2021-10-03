######################################################################
# this module contains an example usage of the function in both the local
# machine using the class or using the lamda function via the AWS
# API gateway
#######################################################################

from distillation_mix import dist_mix

#the file path where all the example distillation distributions are
#located
def filePath():
    return('C:\\Users\\Hadi-PC\\Desktop\\distillation profiles')


# This is an example of loading in a profile based on the local
# machine file path
def getProfile(name):
    path = filePath()
    pmix = dist_mix()
    profile = pmix.getProfile(path,name)
    return(profile)

# This is an example of the 2 methods working togeather to output
# a weighted average
def calDistillation(proName1,vol1,proName2,vol2):

    path = filePath()
    pmix = dist_mix()
    profile1 = pmix.getProfile(path,proName1)
    profile2 = pmix.getProfile(path, proName2)
    Dismix = pmix.getDisMix(profile1,vol1,profile2,vol2)
    return(Dismix)

if __name__ == '__main__':
    proName1 = 'bc light.csv'
    proName2 = 'mixed sweet blend.csv'

    print("####### Example of a csv profile read: " + proName1 +" #######")
    print(getProfile(proName1))

    print("####### Example of a csv profile read: " + proName2 + " #######")
    print(getProfile(proName2))

    print("####### Example of a mixture of Profile Distribution #######")
    vol1 = 10
    vol2 = 20

    print(calDistillation(proName1,vol1,proName2,vol2))








