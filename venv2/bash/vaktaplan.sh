#!bin/bash
cd ../python
source /Users/odinndagur/Code/Github/vaktaplan/venv2/python/camelot-env/bin/activate
echo pt1
python3 vaktaplan-pt-1.py
deactivate

source /Users/odinndagur/Code/Github/vaktaplan/venv2/python/minecart-env/bin/activate
echo pt2
python3 vaktaplan-pt-2.py
deactivate

source /Users/odinndagur/Code/Github/vaktaplan/venv2/python/camelot-env/bin/activate
echo pt3
python3 vaktaplan-pt-3.py