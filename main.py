# main.py
# script to batch download Facebook photos from an individual account

# start LIBRARIES
import facebook
import requests
# end LIBRARIES

# start METHODS

def get_fb_token(app_id, app_secret):
	url = 'https://graph.facebook.com/oauth/access_token'
	payload = {
		'grant_type': 'client_credentials',
		'client_id': app_id,
		'client_secret': app_secret
	}
	response = requests.post(url, params=payload)
	
	# TODO add error handling for invalid response
	print("json response:")
	print(response.json())
	return response.json()['access_token']

# TODO will have to be one ID for non-admins
def getTokenFromUser():
	
	# ask for token from user  # TODO add input error handling
	app_id = int(input("Hey can you give me your Facebook app ID?"))
	app_secret = str(input("Great! Can you give me your Facebook app secret?"))

	access_token = get_fb_token(app_id, app_secret)

	# it pays to be polite
	print ("Thanks!")

	graph = facebook.GraphAPI(access_token)

	# return token
	return access_token

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