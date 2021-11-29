import json
import os
file = open('cred.json')
info = json.load(file)

command = 'curl https://'+info["Domain"]+'.zendesk.com/api/v2/imports/tickets/create_many.json -v -u '+info["username"]+'/token:'+info["AccessToken"]+' -X POST -d @tickets.json -H "Content-Type: application/json"'

os.system(command)