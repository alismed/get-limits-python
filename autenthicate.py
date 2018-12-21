import requests
import os

environment = {
	"base_url": "",
	"grant_type": "password", 
	"client_id": "",
	"client_secret": "",
	"username": "",
	"password": "",
	"security_token": ""
}
	
response = requests.post(environment["base_url"] + "/services/oauth2/token", params=environment)

status_code = response.status_code
error = response.json().get("error_description")
access_token = response.json().get("access_token") 
instance_url = response.json().get("instance_url") 
token_type = response.json().get("token_type") 
