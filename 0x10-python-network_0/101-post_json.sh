#!/bin/bash
# send curl POST request to given url and json file data
curl -s -X POST $1 -H 'Accept: application/json' -H 'Content-Type: application/json' -d @$2
