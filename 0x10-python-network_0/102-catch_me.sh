#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me and get the response
curl -sLX PUT  -d "user_id=98" -H "Origin:school" "0.0.0.0:5000/catch_me"