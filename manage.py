#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print "*"*100
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # sys.path.append(BASE_DIR)
    # sys.path.append('/Users/wangjinyu/PycharmProjects/mysite')
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
