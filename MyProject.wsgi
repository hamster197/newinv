import os
import sys

path = '/var/www/crm'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

sys.path.append("/var/www/crm/myvenv/lib/python3.6/site-packages")
os.environ['DJANGO_SETTINGS_MODULE'] = 'zhem.settings'



from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
