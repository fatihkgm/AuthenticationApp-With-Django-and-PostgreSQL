# AuthenticationApp-With-Django-and-PostgreSQL


ð  Created database 
	âï¸ CREATE USER <name> WITH PASSWORD 'password' CREATEDB;

	âï¸	CREATE TABLE users  
	    (id BIGSERIAL PRIMARY KEY NOT NULL,  
	    name VARCHAR(200) NOT NULL, 		
	    email VARCHAR(200) NOT NULL,   
	    password VARCHAR(200) NOT NULL,  
	    UNIQUE (email));  
	

ð Basic Installation guide
   Create a folder and go to directory
   âï¸ python -m venv env
   âï¸ "for mac user" source ./env/bin/activate  
   âï¸ "for Windows user" source/env/Scripts/activate
   âï¸ pip install django
   âï¸ pip install --upgrade pip
   âï¸ django-admin startproject <folderName> .
   âï¸ "Run server to see if project works" python manage.py runserver
ð  Creating pages 
âï¸   python manage.py startapp account

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication


ð´ Heroku Deployment 		
	âï¸ export database to json file = > python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 >		 project_dump.json		
	âï¸pip freeze > requirements.txt. 
	âï¸runtime.txt => python-version		
	âï¸make config set in setting.py		
	âï¸heroku create app and git push heroku main		

https://devcenter.heroku.com/articles/deploying-python	

ð YouTube Link:    
   https://youtu.be/6jDCt98MZNA
   
   

![Screen-Recording-2021-03-29-at-7](https://user-images.githubusercontent.com/63836841/112942189-bef84780-90fd-11eb-98ca-de43caedbea0.gif)




   



