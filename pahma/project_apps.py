# these are the webapps available for PAHMA

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'rest_framework',
    'django_tables2',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # 'demo' apps -- uncomment for debugging or demo
    'hello',
    'service',
    # 'service' apps: no UI
    'common',
    #'csvimport',
    'suggest',
    'suggestpostgres',
    'suggestsolr',
    #'batchuploadimages',
    # 'standard' apps
    #'asura',
    #'adhocreports',
    'grouper',
    'imagebrowser',
    'imageserver',
    'imaginator',
    'internal',
    'ireports',
    'landing',
    'osteology',
    'permalinks',
    'search',
    #'taxonomyeditor',
    'toolbox',
    #'simplesearch',
    'uploadmedia',
    'uploadtricoder',
)

