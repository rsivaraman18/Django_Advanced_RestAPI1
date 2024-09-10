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

3.setting -->
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'], 

4.URLS
    ### Django -Filtering
   path('<int:pk>/allreviews/', UserReviewsfilter3.as_view()) ,

5.Views
    from django_filters.rest_framework import DjangoFilterBackend

    class UserReviewsfilter3(generics.ListAPIView):
        serializer_class = ReviewSerializer1
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['reviewer_name__username', 'active']  # 'username' will be mapped here

        def get_queryset(self):
            pk = self.kwargs['pk']
            return MyReview.objects.filter(watchlist=pk)

6.Check URLS
    URLS : http://127.0.0.1:8000/movieapi/2/allreviews/?reviewer_name__username=siva
           http://127.0.0.1:8000/movieapi/2/allreviews/?reviewer_name__username=siva&active=True
    METHOD: GET 
    HEADER:-
    BODY : -
    OUTPUT : [
                {
                    "id": 2,
                    "reviewer_name": "siva",
                    "rating": 4,
                    "description": "Excellent",
                    "active": false,
                    "created": "2024-09-05T08:49:32.431447Z",
                    "update": "2024-09-10T06:49:08.285828Z"
                }
            ]

    
