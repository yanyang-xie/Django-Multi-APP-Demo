### #### **Django demo project with more apps**
[========]

1. Project的base url中加入app的url pattern
```yaml
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app1/', include('app1.urls')),
    url(r'^app2/', include('app2.urls')),
]
```

------------
2. 添加app 共用的commontemplates与commonstatic文件夹, 且在setting中配置static及template

```yaml
HERE = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(HERE,'static').replace('\\','/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
   os.path.join(HERE,'commonstatic/').replace('\\','/'),
)
```

```yaml
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #这里是定义除了app内部的templates文件夹, 如何找到公共的templates
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
```


