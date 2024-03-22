#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os, shutil


# In[14]:


path = r"D:/"


# In[17]:


file_name = os.listdir(path)


# In[34]:


folder_names = ["csv files", "image files", "text files","PDF files","Doc files","Zip files","Exe files"]

for loop in range(0,7):
    if not os.path.exists(path+folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])


# In[36]:


for file in file_name:
    if ".csv"in file and not os.path.exists(path+"csv files/"+file):
        shutil.move(path+file,path+"csv files/"+file)
    elif ".xlsx"in file and not os.path.exists(path+"csv files/"+file):
        shutil.move(path+file,path+"csv files/"+file)
    elif ".png"in file and not os.path.exists(path+"image files/"+file):
        shutil.move(path+file,path+"image files/"+file)
    elif ".jpg"in file and not os.path.exists(path+"image files/"+file):
        shutil.move(path+file,path+"image files/"+file)
    elif ".jpeg"in file and not os.path.exists(path+"image files/"+file):
        shutil.move(path+file,path+"image files/"+file)
    elif ".txt"in file and not os.path.exists(path+"text files/"+file):
        shutil.move(path+file,path+"text files/"+file)
    elif ".pdf"in file and not os.path.exists(path+"PDF files/"+file):
        shutil.move(path+file,path+"PDF files/"+file)
    elif ".docx"in file and not os.path.exists(path+"Doc files/"+file):
        shutil.move(path+file,path+"Doc files/"+file)
    elif ".zip"in file and not os.path.exists(path+"Zip files/"+file):
        shutil.move(path+file,path+"Zip files/"+file)
    elif ".rar"in file and not os.path.exists(path+"Zip files/"+file):
        shutil.move(path+file,path+"Zip files/"+file)
    elif ".exe"in file and not os.path.exists(path+"Exe files/"+file):
        shutil.move(path+file,path+"Exe files/"+file)
    else:
        print("There are files in this path that were not moved")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




