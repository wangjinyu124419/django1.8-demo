# django1.8_demo
demo_mysite

行服务运
python manage.py runserver
或者
django-admin runserver启动服务


django-admin 需要配置环境变量，以及将环境变量制定的模块路径添加到python的模块搜索路径:

在.zshrc文件中中永久设置的

```
export DJANGO_SETTINGS_MODULE=mysite.settings
export PYTHONPATH=$PYTHONPATH:/Users/wangjinyu/PycharmProjects/mysite
```
不设置环境变量报错：

```python
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
```

不添加搜索路径报错：
```
django . ImportError: No module named mysite.settings
```


