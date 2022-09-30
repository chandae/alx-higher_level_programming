#!/bin/bash
# sends post request to url passed as argument
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
