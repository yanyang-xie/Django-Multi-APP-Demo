# Django-Multi-APP-Demo
Django demo project with more apps

1. Project的base url中加入app的url pattern
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app1/', include('app1.urls')),
    url(r'^app2/', include('app2.urls')),
]

2. 添加app 共用的commontemplates与commonstatic文件夹, 然后在setting中配置static及template
HERE = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join( HERE ,'media').replace('\\','/') 
MEDIA_URL = '/media/' 
STATIC_ROOT = os.path.join(HERE,'static').replace('\\','/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
   # add other path no app static 
   os.path.join(HERE,'commonstatic/').replace('\\','/'),
) 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'commontemplates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
               'django.contrib.auth.context_processors.auth',
       'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


