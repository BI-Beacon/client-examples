#!/bin/sh

# Set a BI-Beacon to blue
curl -X POST -F "color=#0000FF" "https://api.bi-beacon.com/v1/simple-awesome-monitor"

# Pulse purple slowly
curl -X POST -F "color=#4400FF" -F "period=3000" "https://api.bi-beacon.com/v1/simple-awesome-monitor"

