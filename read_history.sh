#!/bin/bash 
updateHistory="~/Desktop/UpdateAutomator/update_history.txt"
prevRunFiles=()

read_history_file() {	
	while read line; 
	   do 
	   prevRunFiles+=($line) 
	done < $updateHistory

	for filename in "${prevRunFiles[@]}"; 
	   do 
	   echo "$filename"
	done
}

test -f $updateHistory || echo > $updateHistory
read_history_file

