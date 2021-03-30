# AuthenticationApp-With-Django-and-PostgreSQL


📌  Created database 
	✔️ CREATE USER <name> WITH PASSWORD 'password' CREATEDB;

	✔️	CREATE TABLE users  
	    (id BIGSERIAL PRIMARY KEY NOT NULL,  
	    name VARCHAR(200) NOT NULL, 		
	    email VARCHAR(200) NOT NULL,   
	    password VARCHAR(200) NOT NULL,  
	    UNIQUE (email));  
	

📌 Basic Installation guide
   Create a folder and go to directory
   ☑️ python -m venv env
   ☑️ "for mac user" source ./env/bin/activate  
   ☑️ "for Windows user" source/env/Scripts/activate
   ☑️ pip install django
   ☑️ pip install --upgrade pip
   ☑️ django-admin startproject <folderName> .
   ☑️ "Run server to see if project works" python manage.py runserver
📌  Creating pages 
☑️   python manage.py startapp account

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication


🔴 Heroku Deployment 		
	☑️ export database to json file = > python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 >		 project_dump.json		
	☑️pip freeze > requirements.txt. 
	☑️runtime.txt => python-version		
	☑️make config set in setting.py		
	☑️heroku create app and git push heroku main		

https://devcenter.heroku.com/articles/deploying-python	

👉 YouTube Link:    
   https://youtu.be/6jDCt98MZNA
   
   

![Screen-Recording-2021-03-29-at-7](https://user-images.githubusercontent.com/63836841/112942189-bef84780-90fd-11eb-98ca-de43caedbea0.gif)




   



