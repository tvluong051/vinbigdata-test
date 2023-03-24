## VinBigdata test
Here is an API server for call. There are 2 APIs
- PUT <BASE_PATH>/mobile/<username>/call
- GET <BASE_PATH>/mobile/<username>/billing

## How to start it?
### Start server with Docker
The server is developped with Flask and Postgres and containerized with Docker. Prerequisite to start it is Docker (and Docker compose) installed.

Follow these instruction to start it
1. Pull the project to local workspace
2. Configure server using .env file provided. You are free to choose database credentials as well as server port.
3. Start docker 
```
docker compose up -d 
```
You could also not detach container
```
docker compose up
```
Server will be start at `http://localhost:<port>` (BASE_PATH) where port is provided in `.env` file
3. Using `curl` or more advanced tools as Postman to test the API

### Start server manually
Another way to start the server is setup server locally. In this case, you will need python3 and Postgres server set up in your system
1. Setup Python virtual env
```
python3 -m venv venv
source venv/bin/activate
``` 
2. Install requirements using `pip`
```
python3 -m pip install -r requirements.txt
```
3. Start server
```
export DB_URL=postgresql://<db_username>:<db_pwd>@<db_host>:<db_port>/postgres && python3 wsgi.py
```
rver will be start at `http://localhost:5151`. Though you could also change the port by provide env var `PORT`
4. Using `curl` or more advanced tools as Postman to test the API

5. For running tests
```
export DB_URL=sqlite:///test.db && python3 -m pytest -v
```

## What else could we do to improve
1. More tests
2. API Documentation is setup with Swagger but it's still light, could improve on it. We could also using Swagger to test API
3. Secure API, for example with Basic Auth, OAuth2, etc. Limit user to access to its own billing only
4. CI/CD setup
