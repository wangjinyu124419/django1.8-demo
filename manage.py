# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print sys.argv

    #debug模式下,代码会print "*"*100调用两次,python manage.py run --noreload可以解决
    #原因
    #https://stackoverflow.com/questions/28489863/why-is-run-called-twice-in-the-django-dev-server
    print "*"*100
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
