#!/usr/bin/env bash
# scripts makes a cURL request to url passed as argument
# displays the size of the body of the response

curl --head "$1" | grep "Content-Length" | cut -c 17-
