######################################################################
# this module contains an example usage of the function in both the local
# machine using the class or using the lamda function via the AWS
# API gateway
#######################################################################

from distillation_mix import dist_mix

# This is an example of loading in a profile based on the local
# machine file path
def getProfile():
    path = 'C:\\Users\\Hadi-PC\\Desktop\\distillation profiles'
    name = 'syncrude sweet premium.csv'
    pmix = dist_mix()
    profile = pmix.getProfile(path,name)


if __name__ == '__main__':
    print(getProfile())






