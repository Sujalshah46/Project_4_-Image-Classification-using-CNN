# Project_4_ Image Classification using CNN_BY_EdgeAIHub
import os
os.chdir('D:\\MasterClass\\Artificial_Intelligence\\Day12\\Code\\simple_images\\thanosMarvel\\')
i=1
#Project_4_ Image Classification using CNN_BY_EdgeAIHub
for file in os.listdir():
    src=file
    dst="2"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1
#Project_4_ Image Classification using CNN_BY_EdgeAIHub

