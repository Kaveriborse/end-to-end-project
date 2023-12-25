# shell script with the help of which we can run no of commands in one time
echo $(date)]: "START"


echo [$(date)]: "creating env with python 3.8 version" 

conda create --prefix ./env python=3.8 -y


echo [$(date)]: "activating the environment" 

source activate ./env  # activate env mannualy

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 
