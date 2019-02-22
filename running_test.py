import sys
import django

assert (int(sys.version.split('.')[0]) == 3 and int(sys.version.split('.')[1]) >= 5)
print('Python version is right!')

assert django.VERSION[0] >= 2
print('Django is up and running!')