#!/bin/bash
#Bash script that takes in a URL, sends a POST
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
