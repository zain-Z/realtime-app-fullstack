# realtime-app-fullstack

# Backend

- Python
- Pipenv
- Django / Django-REST-Framework
- Django-cors-headers
- Channels
- Channels-redis

## Getting started

To start project without getting any errors:

- Install pipenv by command: python install pipenv
- run "pipenv shell"
- You have to install redis on your PC

# link for steps: https://divyanshushekhar.com/how-to-install-redis-on-windows-10/

# for installing channels and channels-redis

1- run "pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl"
2- run "pipenv install channels" then after that run "pipenv install channels channels-redis"

# to use redis and make docker make an image

- run "docker run -p 6379:6379 -d redis:3.0"
