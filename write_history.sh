#!/bin/bash

filename=$1
path=$2

echo $filename >> "$path"/update_history.txt
