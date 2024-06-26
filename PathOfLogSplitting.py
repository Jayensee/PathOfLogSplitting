from os.path import exists
from os import mkdir
from time import time
from json import load



with open("config.json", "r") as f:
    config = load(f)

log_file_path = config["Original Log File Path"]
output_folder_path = config["Output Folder Path"]

if "Client.txt" not in log_file_path:
    log_file_path += "/Client.txt"

start_time = time()
with open(log_file_path, "r", encoding="utf-8") as original_file:
    line = original_file.readline()
    last_saved_date = line[:10]
    raw_text = ""
    while len(line)>0:
        if "INFO Client" in line:
            current_date = line[:10]
            raw_text += line
            if last_saved_date != current_date:
                year = current_date[:4]
                new_folder = f"{output_folder_path}/{year}"
                if not exists(new_folder):
                    mkdir(new_folder)
                new_path = f"{new_folder}/{current_date.replace('/','_')}.txt"
                if not exists(new_path):
                    print(f"Saving {current_date.replace('/','_')}.txt", end="\r")
                    with open(new_path, "w", encoding="utf-8") as new_file:
                        new_file.write(raw_text)
                last_saved_date = line[:10]
                raw_text = ""
        line = original_file.readline()
print(f"Took {(time()-start_time):.2f} seconds to run.")