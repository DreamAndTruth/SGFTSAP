#coding: utf-8
'''
Describe: 
        This file is used to modify the TIMIT wav files name as "S{ }W{ }.wav" .
        Before modify the files name, you need translate the file type SPHERE to WAV.
'''

import os

path = r"E:\Code\BuildDream\用于参考的网络上的说话人识别实现\kaldi-timit-sre-ivector-master\TIMIT_SPREC"

mm = 1


####### modify dir name ####
for d in os.listdir(os.path.join(path, "TRAIN")): # train dir
    if len(str(mm)) == 1:
        n_d = "SP000" + str(mm)
        os.rename(os.path.join(path, "TRAIN", d), os.path.join(path, "TRAIN", n_d))
        mm += 1
    elif len(str(mm)) == 2:
        n_d = "SP00" + str(mm)
        os.rename(os.path.join(path, "TRAIN", d), os.path.join(path, "TRAIN", n_d))
        mm += 1
    else:
        n_d = "SP0" + str(mm)
        os.rename(os.path.join(path, "TRAIN", d), os.path.join(path, "TRAIN", n_d))
        mm += 1
print("Train dirs has modified!")

# The test speaker IDs start from {463-630}
for d in os.listdir(os.path.join(path,  "TEST")):
    n_d = "SP0" + str(mm)
    os.rename(os.path.join(path,"TEST", d), os.path.join(path,"TEST", n_d))
    mm += 1
print("Test dirs has modified!")

####### modify wav name ######
for root, dirs, files in os.walk(os.path.join(path)):
    print("*"*10)
    print("root: {0}, dir:{1}".format(root,dirs))
    print("SpeakerID " + root[-6:])
    n=0
    for name in files:
        if(name.endswith(".PHN")):
            os.remove(os.path.join(root, name))
        elif(name.endswith(".TXT")):
            os.remove(os.path.join(root, name))
        elif(name.endswith(".WRD")):
            os.remove(os.path.join(root, name))
        else:
            new_name = root[-6:] + "W0" + str(n) + ".wav"
            os.rename(os.path.join(root, name), os.path.join(root, new_name))
            n += 1
    print(os.listdir(root))