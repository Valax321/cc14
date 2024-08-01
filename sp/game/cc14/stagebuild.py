import os, zipfile, shutil, errno, subprocess
from os.path import join

# Main settings
game_name = "Network"
version = "1.0"
stage_paths = [ "bin", "cfg", "content", "maps", "materials", "models", "particles", "resource", "scenes", "scripts", "shaders", "sound", "gameinfo.txt", "modelsounds.cache", "readme.txt" ]

# vpk settings
target_folders = [ "materials", "models", "particles", "scenes", "resource", "scripts", "sound" ]
file_types = [ "vmt", "vtf", "mdl", "phy", "vtx", "vvd", "ani", "pcf", "vcd", "txt", "res", "wav", "mp3", "cache", "lst", "nut", "ttf" ]
vpk_path = "D:/Steam/steamapps/common/Source SDK Base 2013 Singleplayer/bin/vpk.exe"

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Copy error: %s' % e)


# ------ BEGIN MAIN SCRIPT -------

# Make staging directory
if not os.path.exists(".staging"):
    os.mkdir(".staging")

# Iterate staged files/folders and copy them across
for sp in stage_paths:
    rel_path = join(".staging", sp)
    print('Staging %s' % sp)
    if os.path.exists(rel_path):
        os.remove(rel_path)
    copy(sp, rel_path)

# Perform vpk packing
old_cwd = os.getcwd()
os.chdir(".staging")
response_path = join(os.getcwd(),"vpk_list.txt")
out = open(response_path,'w')
len_cd = len(os.getcwd()) + 1
for user_folder in target_folders:
    for root, dirs, files in os.walk(join(os.getcwd(),user_folder)):
        for file in files:
            if len(file_types) and file.rsplit(".")[-1] in file_types:
                out.write(os.path.join(root[len_cd:].replace("/","\\"),file) + "\n")
out.close()
print("Building game vpks...")
subprocess.call([vpk_path, "-M", "a", "network_pak", "@" + response_path])

# Clean up vpk'd folders
for folder in target_folders:
    print('Cleaning up %s' % folder)
    shutil.rmtree(folder)

os.remove("vpk_list.txt")

os.chdir(old_cwd)

# Create build zip file
print("Zipping build...")
shutil.make_archive('%s-%s-Release' %(game_name, version), "zip", ".staging")

print("Build completed!")