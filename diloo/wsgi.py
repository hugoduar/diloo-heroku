"""
WSGI config for diloo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diloo.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

<<<<<<< HEAD
application = Cling(get_wsgi_application())
=======
application = Cling(get_wsgi_application())


# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diloo.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
