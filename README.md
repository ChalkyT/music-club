# Album Club
Requires python3.

## Dev
In one terminal and in the root dir run the backend with `DJANGO_DEBUG=ON python manage.py runserver`.

In another terminal and in `/frontend` run the frontend with `npm run dev` to keep front end code in sync.

Svelte files are located in `/frontend/src`

Create a super user running in a terminal
`python manage.py createsuperuser`

Now if you try to hit `localhost:8000`, you will be redirected to `http://localhost:8000/accounts/login/?next=/`.

Try to login with the provided credentials and you will see the Svelte app again.

Hit `localhost:8000/accounts/logout` to logout.

Basic API greeting at `/api/greet`

Run production server with `python -m gunicorn albumclub.wsgi`