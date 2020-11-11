# Django-ForeignKey-Tutorial
Everything there is to learn about Django's Foreign Key will be captured here.

## How this repo was created in the beginning

Step 1: Clone empty git repository.

    git clone https://github.com/digitallyamar/Django-ForeignKey-Tutorial.git
    cd Django-ForeignKey-Tutorial

Step 2: Create Python virtual environment.

    python3 -m venv venv

Stage 3: Install Django

    pip install Django

Step 4: Create the Django project in the current directory

    django-admin startproject ForeignKey .

Step 4: Create a dummy todo app & add it to the project.

    django-admin startapp todo

    Edit INSTALLED_APPS list in the ForeignKey/settings.py file.
    Add "todo" app to the list.

Step 6: Apply migrations and check the server is running fine.

    To migrate the project to include admin DB models, issue the following command:

    python3 manage.py migrate

    Check everything is working fine by running the command:

    python3 manage.py runserver

Now visit http://127.0.0.1:8000/ and you shoule be greeted with Django homepage.

Step 7: Create an admin user by issuing the command:

    python3 manage.py createsuperuser

Step 8: Define models for Todo app

    Now that we have basic setup running, it is time to add models to our todo app.

    Edit the todo/models.py to introduce two new todo app models:

        1. Todo 
        2. Location

Step 7: Once the models and associated save and __self__ methods are described,
        create migration files and migrate to it.

        python3 manage.py makemigrations
        python3 manage.py migrate

Step 8: Now that we have everything in place, it is time to run our server:

        python3 manage.py runserver

Now visit http://127.0.0.1:8000/admin and login


## Stage 1 - How to update field of an object pointed by a Foreign Key.


Step 9: We need to add our models to admin by editing the todo/admin.py file

        Notice how we are plugging in a url to Todo task from Location using:
        
        task_link()

Now visit http://127.0.0.1:8000/admin and login

Step 10: Create location entry first & add a todo task set to that location.

        Notice how we can access todo associated with a location by visiting 
        "Task Link" field in the Location Admin panel

This is how you can update foreign key's field.