import os

path="notebooks/research.ipynb"  # it is comb of file and folder

dir,file=os.path.split(path)   # it separates the name of file and folder

os.makedirs(dir,exist_ok=True)   # it will create a dir

'''
with open(file,"w") as f:  # it will craete a file
    pass
    '''

with open(path,"w") as f:
    pass