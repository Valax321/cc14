# User settings (don't use the \ character)
target_folders = [ "materials", "models", "particles", "scenes", "resource", "scripts", "sound" ]
file_types = [ "vmt", "vtf", "mdl", "phy", "vtx", "vvd", "pcf", "vcd", "txt", "res", "wav", "mp3", "cache", "lst", "nut" ]
vpk_path = "D:/Steam/steamapps/common/Source SDK Base 2013 Singleplayer/bin/vpk.exe"

# Script begins
import os,subprocess
from os.path import join
response_path = join(os.getcwd(),"vpk_list.txt")

out = open(response_path,'w')
len_cd = len(os.getcwd()) + 1

for user_folder in target_folders:
	for root, dirs, files in os.walk(join(os.getcwd(),user_folder)):
		for file in files:
			if len(file_types) and file.rsplit(".")[-1] in file_types:
				out.write(os.path.join(root[len_cd:].replace("/","\\"),file) + "\n")

out.close()

subprocess.call([vpk_path, "-M", "a", "network_pak", "@" + response_path])