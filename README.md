### Description
Yatub API is a social network project that includes the following features: posting messages, commenting on posts, subscribing and unsubscribing from authors.
### Technologies
Python 3.9, Django 2.2.16, DRF, JWT + Djoser
### Running the project in dev mode
- Clone the repository and navigate to it in the command line.
- Install and activate the virtual environment considering Python 3.9:
```bash
py -3.9 -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
```
- Then install all the dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```
- Perform migrations:
```bash
python manage.py migrate
```
Create a superuser:
```bash
python manage.py createsuperuser
```
Start the project:
```bash
python manage.py runserver
```
### Examples of working with the API for all users
For unauthorized users, API access is only in read mode, and it's impossible to make any changes or create any new objects.
```bash
GET api/v1/posts/ - get a list of all publications.
When specifying the parameters limit and offset, the issuance should work with pagination.
GET api/v1/posts/{id}/ - get a publication by id
GET api/v1/groups/ - get a list of available communities
GET api/v1/groups/{id}/ - get information about a community by id
GET api/v1/{post_id}/comments/ - get all comments to a publication
GET api/v1/{post_id}/comments/{id}/ - get a comment to a publication by id
```
### Examples of working with the API for authorized users
To create a publication, use:
```bash
POST /api/v1/posts/
```
with body
{
"text": "string",
"image": "string",
"group": 0
}

To update a publication:
```bash
PUT /api/v1/posts/{id}/
```
with body
{
"text": "string",
"image": "string",
"group": 0
}

To partially update a publication:
```bash
PATCH /api/v1/posts/{id}/
```
with body
{
"text": "string",
"image": "string",
"group": 0
}

To delete a publication:
```bash
DEL /api/v1/posts/{id}/
```
Access to the /api/v1/follow/ endpoint (subscriptions) is only available to authorized users.
```bash
GET /api/v1/follow/ - subscribe a user on behalf of whom the request was made
to the user specified in the request body. Anonymous requests are prohibited.
```
- Authorized users can create posts, comment on them, and subscribe to other users.
- Users can modify (delete) content they created.

### To add a group to the project, you need to use Django admin panel:
```bash
admin/ - after authorization, go to the Groups section and create groups
```
Authorized user access is available through a JWT token (Joser), which can be obtained by making a POST request to the address:
```bash
POST /api/v1/jwt/create/
```
Sending user data in the request body (for example, in Postman):
```bash
{
"username": "string",
"password": "string"
}
```
Add the received token to the headers (Postman), after which all project functions will be available:
```bash
Authorization: Bearer {your_token}
```
To refresh a JWT token:
```bash
POST /api/v1/jwt/refresh/ - update JWT token
```
Check JWT token:
```bash
POST /api/v1/jwt/verify/ - verify JWT token
```
Also, the API project implements pagination (LimitOffsetPagination):
```bash
GET /api/v1/posts/?limit=5&offset=0 - pagination for 5 posts starting from the first
```