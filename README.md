# Convin-Rahul
The test platform for file and text fields

## Notes
- Update and create are notified as Logs in log.txt file (Could've created a new Notifiaction model or sent mails for the same) 
- File to char field is achieved using a 20 sec sleep followed by sha256 for the file
- Speed is achieved using Threading in Python (Should use Celery for larger environments, also Node.js is a very good alternative for the same)
- Because signals are being used on the post_save, you can use any method for updating the model. Directly updating from the admin_panel can be used to test. For the sake of API and update API has been provided at `/main/create`

## How to run
Automatic Method
- Create and Activate your virtual environment. (preferred)
- Run the ```SETUP.sh``` file.
- Run the server using `python manage.py runserver`

Manual Method
- Create and Activate your virtual environment. (preferred)
- Install the requirements using ```pip install -r requirements.txt```
- Make migrations and update the tables using 
`
python manage.py makemigrations
python manage.py migrate
`
- Run the server using `python manage.py runserver`