#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import os

base="https://oapi.dingtalk.com/robot/send?access_token="
headers={"Content-Type": "application/json"}

access_token=os.environ['INPUT_ACCESS_TOKEN']
title=os.environ['INPUT_TITLE']
content=os.environ['INPUT_CONTENT']

def dingRequest():
  payload={"msgtype":"markdown","at":{"isAtAll":"true"},"markdown":{"title":title,"text":content}}
  url=base+access_token
  r=requests.post(url,headers=headers,data=json.dumps(payload))
  if r.status_code==200:
    # print(r.text)
    try:
      obj=r.json()
      if obj["errcode"] == 0:
        print("Send Success")
      else:
        print("Response:", obj["errmsg"])
    except Exception as error:
      print("Exception:", error)
  else:
    print("Request error", r)

dingRequest()