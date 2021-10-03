######################################################################
# this module contains an example usage of the function in both the local
# machine using the class or using the lamda function via the AWS
# API gateway
#######################################################################

from distillation_mix import dist_mix
import os

#the file path where all the example distillation distributions are
#located
def filePath():
    return(str(os. getcwd()) + "\\" + "distillation profiles")


# This is an example of loading in a profile based on the local
# machine file path
def getProfile(name):
    path = filePath()
    pmix = dist_mix()
    profile = pmix.getProfile(path,name + '.csv')
    return(profile)

# This is an example of the 2 methods working togeather to output
# a weighted average
def calDistillation(proName1,vol1,proName2,vol2):

    path = filePath()
    pmix = dist_mix()
    profile1 = pmix.getProfile(path,proName1 + '.csv')
    profile2 = pmix.getProfile(path, proName2 + '.csv')
    Dismix = pmix.getDisMix(profile1,vol1,profile2,vol2)
    return(Dismix)

def localRun():
    # The following are profile that are currently avaliable
    # bc light,mixed sweet blend,pembina, syncrude sweet premium
    proName1 = 'bc light'
    proName2 = 'mixed sweet blend'
    print ("")
    print("####### Example of a csv profile read: " + proName1 + " #######")
    print(getProfile(proName1))

    print("####### Example of a csv profile read: " + proName2 + " #######")
    print(getProfile(proName2))

    print("####### Example of a mixture of Profile Distribution based on weighted average #######")
    vol1 = 15
    vol2 = 20

    print(calDistillation(proName1, vol1, proName2, vol2))


if __name__ == '__main__':
    localRun()







