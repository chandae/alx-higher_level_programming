#!/bin/bash
# script makes request to 0.0.0.0:5000/catch_me
curl -s -w 'You find me!' 0.0.0.0:5000/catch_me -o saved
