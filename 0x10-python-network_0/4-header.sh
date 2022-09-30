#!/bin/bash
# send get request with additional custom header
curl -sH "X-School-User-Id: 98" "$1"
