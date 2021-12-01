# books-ecommerce

Tech task: https://www.notion.so/invite/3e2c666b1fe836fa2560b646ffda30b4e9efa853

## Backend

For backend, we are using Django, DRF (see detailed in `requirements.txt`).

Also, I am using `black` python code formatter: https://github.com/psf/black.

## How to run

#### Backend:
- `python3 -m venv venv`
- `venv\Scripts\activate`
- `cd backend`
- `pip install -r requirements.txt`
- `python manage.py runserver`

## Database

We are using ElephantSQL free instance - so DB is same for everyone.

## Git

I propose using different branches for each feature/bug/fix using checkout from develop branch.
Also, I propose using next naming for branches:
- `feat/task-description` for new features
- `bug/task-description` for bug fixes.
