# - Create a User
# POST https://reqres.in/api/users
# 	request body:  {"name": "morpheus", "job": "leader"}
#	Response: {"id": "2", "createdAt": "<<date>>"}


# Test1:
#      Use the user id that was generated in the setup and get the user id using below GET request and validate it returns the same user id.
#	GET https://reqres.in/api/users/2


# Test2:
# 	Update the user using below request.
#	PUT https://reqres.in/api/users/2
#	request body: {"name": "morpheus", "job": "zion resident"}


# Cleanup:
#	Remove the user using below request.
#	DELETE https://reqres.in/api/users/2

