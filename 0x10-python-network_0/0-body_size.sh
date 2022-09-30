#!/bin/bash
# scripts makes a cURL request to url passed as argument; displays size of response body
curl --head "$1" | grep "Content-Length" | cut -c 17-
