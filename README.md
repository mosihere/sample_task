# Installation

1. Clone the repo<br>
`$ git clone https://github.com/mosihere/sample_task.git`<br><br>
2. Create a Virtualenv<br>
`$ python3 -m venv .env`<br><br>
3. Activate the virtualenv<br>
`$ source .env/bin/activate`<br><br>
4. Install dependecies<br>
`$ python -m pip install -r requirements.txt`<br><br>
5. run the migration files and migrate the db<br>
`$ python manage.py makemigrations`<br>
`$ python manage.py migrate`<br><br>

# Features
1. Customized Pagination
2. Customized Filter
3. Search (Query Parameter)
4. RESTful API
5. ModelViewSet
6. HyperLinkRelation used for serializing relations.

# Endpoint usage samples
1. Getting all books that contains 'star' in their titles and author_id is 1<br>
`http://127.0.0.1:8000/api/books/?title__icontains=star&published_date__lt=&published_date__gt=&author=1`<br><br>
2. Search Authors by name Jimmy for example<br>
`http://127.0.0.1:8000/api/authors/?search=Jimmy`<br><br>
