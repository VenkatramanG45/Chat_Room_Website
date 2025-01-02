import os
import sys
from os.path import join, dirname, abspath
from whitenoise import WhiteNoise

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
STATIC_ROOT = join(PROJECT_ROOT, 'collected_static')
sys.path.insert(0, PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings') #Replace myproject with your project name
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# add Whitenoise settings for production
static_file_root = STATIC_ROOT
application = WhiteNoise(application, root=static_file_root)
