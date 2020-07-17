# blinkled
blinkled app for RPI

RPI Setup:
1. The GPIO channel set up as OUTPUT

Steps:
1. After installing django, now you can create a new django app called "blinkled".
   >>> django-admin startproject blinkled
2. Now setup "led" django app
   >>> python manage.py startapp led
3. Run server
   >>> python manage.py runserver 0.0.0.0:8080
4. Send command on client browser
   >>> http://http://192.168.0.124:8000/led/turnOff/

