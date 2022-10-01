#!/bin/bash
# scripts gets status code of http get response
curl -s -w %{response_code} $1 -o tmpnull
