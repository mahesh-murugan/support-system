# creating virtual environment

python3 -m venv support_system_venv

# activate virtual environment
source support_system_venv/bin/activate

# change directory to project directory
cd support_system_project

# install all the packages in activated virtual environment reading requirements.txt 
pip install -r requirements.txt

# run development server
python manage.py runserver
