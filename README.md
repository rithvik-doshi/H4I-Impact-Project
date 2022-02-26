# RUN the following to start the app

virtualenv -p python3 venv
source venv/bin/activate
export FLASK_ENV='Development'
python app.py

## Then you can open http://127.0.0.1:5000/ in the web browser

- Note that you may have to install python libraries via pip/pip3 to get the project working
