# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #debug模式下,代码会print "*"*100调用两次,python manage.py run --noreload可以解决
    #原因
    #https://stackoverflow.com/questions/28489863/why-is-run-called-twice-in-the-django-dev-server
    print "*"*100
    print('123')
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # sys.path.append(BASE_DIR)
    # sys.path.append('/Users/wangjinyu/PycharmProjects/mysite')
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
