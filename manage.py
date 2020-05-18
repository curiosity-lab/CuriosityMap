#!/usr/bin/env python
import os
import sys

# cmd = ['manage.py', 'shell']
# cmd = ['manage.py', 'createsuperuser'] # admin/goren@gorengordon.com/goren22GG
cmd = ['manage.py', 'runserver', '8080']

# cmd = ['manage.py', 'startapp', 'child']
# cmd = ['manage.py', 'makemigrations', 'teacher']
# cmd = ['manage.py', 'sqlmigrate', 'teacher',  '0004']

# cmd = ['manage.py', 'makemigrations', 'child']
# cmd = ['manage.py', 'sqlmigrate', 'child',  '0003']

# cmd = ['manage.py', 'makemigrations', 'questionnaire']
# cmd = ['manage.py', 'sqlmigrate', 'questionnaire',  '0007']

# cmd = ['manage.py', 'migrate']

if len(sys.argv) > 1:
    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CuriosityMap.settings.base")
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
            ) # from exc
        execute_from_command_line(sys.argv)
else:
    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CuriosityMap.settings.base")
        try:
            from django.core.management import execute_from_command_line
        except ImportError:
            # The above import may fail for some other reason. Ensure that the
            # issue is really that Django is missing to avoid masking other
            # exceptions on Python 2.
            try:
                import django
            except ImportError:
                raise ImportError(
                    "Couldn't import Django. Are you sure it's installed and "
                    "available on your PYTHONPATH environment variable? Did you "
                    "forget to activate a virtual environment?"
                )
            raise


        if len(sys.argv) == 1:
            execute_from_command_line(cmd)
        else:
            execute_from_command_line(sys.argv)
