# realtime-app-fullstack

# Backend

- python
- pipenv
- django / djangorestframework
- django-cors-headers
- channels
- channels-redis
- asgiref

# Frontend

- javascript
- nodejs
- npm
- create-react-app
- yarn
- react-scripts
- react-websocket

## Getting started

To start project without getting any errors:

- Install pipenv by command: python install pipenv
- run "pipenv shell"
- You have to install redis on your PC

# link for steps: https://divyanshushekhar.com/how-to-install-redis-on-windows-10/

# for installing channels and channels-redis

- run "pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl"
- run "pipenv install channels" then after that run "pipenv install channels channels-redis"

# to use redis and make docker make an image

- run "docker run -p 6379:6379 -d redis:2.8"
