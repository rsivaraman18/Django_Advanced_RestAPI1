Filtering ---> 52 Video
PROJECT ---> 27 Filtering using Django-filter Packages
NOTE:   1.Django-Filter package will support only for Generic API Views.
            Eg:class Product(generics.ListAPIView):
                pass 
        2.If you need to make Filtering(Ordering ,Searching) for APIView
          that  are written generally you need to go with Project 26.
          There Parameter and get query set method  used with APIView.
            Eg:class Product(APIView):
                pass



1.Install Django-filter
    pip install django-filter

2.Go to setting -->Add 'django_filter'
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Movieapp',
        'rest_framework',
        'rest_framework.authtoken',
        'django_filters'
    ]

3.
