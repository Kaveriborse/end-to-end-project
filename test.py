'''import os

path="notebooks/research.ipynb"  # it is comb of file and folder

dir,file=os.path.split(path)   # it separates the name of file and folder

os.makedirs(dir,exist_ok=True)   # it will create a dir


with open(file,"w") as f:  # it will craete a file
    pass
    

with open(path,"w") as f:
    pass'''

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(0.7,61.2,57.0,5.69,5.73,3.5,'Ideal','G','VS1')

data=custdataobj.get_data_as_dataframe()
print(data)
