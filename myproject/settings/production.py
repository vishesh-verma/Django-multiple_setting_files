from .base import *
import os



DEBUG= True

DATABASES = {
     'default': {

        'NAME': 'root',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'jaishriram',
        'HOST' : 'localhost',
        'PORT' :'3306',
    }
}
