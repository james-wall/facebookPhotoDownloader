# main.py
# script to batch download Facebook photos from an individual account

# start LIBRARIES
import facebook
# end LIBRARIES

# start METHODS

def getTokenFromUser():

    # ask for token from user
    token = str(input("Hey can you give me your Facebook user token?")) # TODO add input error handling

    # it pays to be polite
    print ("Thanks!")

    # return token
    return token

def getLoginInformationFromUser():
    # TODO
    return [1, 2] # TODO fix 

def getInformationFromUser():
    loginInfo = []
    loginInfo.append(getTokenFromUser())
    loginInfo.append(getLoginInformationFromUser()) # TODO list of lists here

    return loginInfo

def establishLoginWithAPI():
    # TODO
	todo = 1

def getPhotoDetailsFromUser():
    # TODO how many photos?
    # when should the photos be from?
    # what date range?
    # who should be in the photos?
	todo2 = 2

def downloadPhotosToLocation():
    # TODO use information from user to download photos
    # optional ask of where to download photos, otherwise download in a default location (like a desktop folder)
	todo3 = 3

# end METHODS

# 
#
#
#
# start MAIN

getInformationFromUser()

establishLoginWithAPI()

getPhotoDetailsFromUser()

downloadPhotosToLocation()

# end MAIN