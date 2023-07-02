#!/bin/bash
# Sends JSON Post request to URL passed as first argument
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
