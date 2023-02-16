# Album Club
Requires python3.

## Dev

From the root of the project folder:

Create a virtual environment and activate it (if you want.)

Run `pip install -r REQUIREMENTS.txt` or `poetry install`

Run `mkdir albumclub/static`

Run `python manage.py migrate`

Run `python manage.py createsuperuser`

In the root dir run the backend with `DJANGO_DEBUG=ON python manage.py runserver`.

In another terminal and in `/frontend` run the frontend with `npm run dev` to keep front end code in sync.

Run `python manage.py collectstatic`

Svelte files are located in `/frontend/src`

Now if you try to hit `localhost:8000`, you will be redirected to `http://localhost:8000/accounts/login/?next=/`.

Try to login with the provided credentials and you will see the Svelte app again.

Hit `localhost:8000/accounts/logout` to logout.

Basic API greeting at `/api/greet`

Run production server with `python -m gunicorn albumclub.wsgi`