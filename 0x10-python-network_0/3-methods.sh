#!/bin/bash
# scripts sends a get request and outputs allowed methods
curl -s --head $1 | grep Allow | cut -d " " -f 2-
