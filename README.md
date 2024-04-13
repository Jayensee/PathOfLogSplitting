# PathOfLogSplitting
A very short script that splits the Path of Exile client chat log file into multiple log files by date.

## How to use

1. Change the paths in the config.json to the path of the original log and the path where you want to save the new logs
2. Run the python file

Windows for some reason uses backslashes by default in paths shown in the file explorer but in python those are used as escape characters, so you gotta change the backslashes in the path to frontslashes if you copy paste from the file explorer.

Warning: This will create a file for every day on which you've played PoE, it can create hundreds or thousands of files in the output folder.

You need to have python installed to run python scripts. If you're on Linux or and older Mac then you almost certainly have it by default, on Windows you can find it in the app store (this is not the recommended installation if you intend to actually use python extensively, but for just running small scripts it should be fine).

As far as I know, on Windows you can't just double-click to run a python file, you gotta: 
1. open a command line
2. navigate over to the correct folder with `cd correct/folder/path` (make sure to use the path where you downloaded the code)
3. run `python PathOfLogSplitting.py`

It should be entirely impossible for this script to in any way change the original log file, but as a general precaution, whenever you're handling important files always make a backup (yes, PoE chat logs are very important :D).

This script skips debug logs so the output folder should always use up less disk space than the original.
Also, I don't have logs before 2021 so I can't guarantee the script will work for log files with older logs, since the format could have changed since then.
