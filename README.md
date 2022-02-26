source environment_3_8_2/bin/activate
cd projectName_Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/admin

userName: admin
Email: admin@gmail.com
password: 786638


In another terminal --> cd projectName_Client --> yarn run serve
