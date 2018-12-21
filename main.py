import autenthicate
import util
import requests

api_version = "v43.0"

if autenthicate.access_token:
  header_limit_request = {
    "Authorization": autenthicate.token_type + " " + autenthicate.access_token,
    "Content-Type": "application/json"
  }

  limit_request = requests.get(autenthicate.instance_url + "/services/data/" + api_version +"/limits/", headers=header_limit_request) 

  if limit_request.ok:
    util.iterate_json(limit_request.json())
else:
  print(autenthicate.error + ". http status code:" + str(autenthicate.status_code))
