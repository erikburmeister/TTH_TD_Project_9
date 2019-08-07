# TTH_TD_Project_9
 Improve a Django Project

In project #9 we are tasked with fixing up a project that was not well thought out. 
We need to fix the following:

* Bad template inheritance
* Extra database calls
* Extra views
* Fix the Models
* Make tests to cover 75% or more

-----------------------------------------

Check the site preview image & coverage image 
for quick look at the result.

-----------------------------------------

To Create a User

In the teminal type 'python manage.py createsuperuser'
Follow the steps.
go to '/admin' on the url.
sign in and done. 

-----------------------------------------

Check test coverage

* coverage run --source='.' manage.py test menu
* coverage report

-----------------------------------------

Check requirements.txt Info on package versions on it.

* Django==2.2.3
* django-debug-toolbar==2.0
* pytz==2019.2
* selenium==3.141.0
* sqlparse==0.3.0
* urllib3==1.25.3
