Filtering ---> 54 Video
1.FILTERING AGAINST username
2.FILTERING USING QUERY PARAMETER

1.Create a New Class in views.py and Urls to make Filter based on the username.
    1A.Class --> Views.py
        class UserReviewsfilter1(generics.ListAPIView):
        serializer_class = ReviewSerializer1

        def get_queryset(self):
            username = self.kwargs['username']
            return MyReview.objects.filter(reviewer_name__username=username)
    
    1B.Class --> Urls.py
        ### URLS ---> http://127.0.0.1:8000/movieapi/reviews/siva/
        path('reviews/<str:username>/', UserReviewsfilter1.as_view()) ,

2.Check Urls
    URL : http://127.0.0.1:8000/movieapi/reviews/siva/ or 
          http://127.0.0.1:8000/movieapi/reviews/demo1/
    Method : GET
    HEADER:
    Body
    Output:
        [
            {
                "id": 9,
                "reviewer_name": "demo1",
                "rating": 3,
                "description": "great Super!",
                "active": true,
                "created": "2024-09-06T10:57:25.085129Z",
                "update": "2024-09-06T10:57:25.085129Z"
            },
            {
                "id": 10,
                "reviewer_name": "demo1",
                "rating": 4,
                "description": "Super!",
                "active": true,
                "created": "2024-09-06T10:57:43.323916Z",
                "update": "2024-09-06T10:57:43.323916Z"
            },
        ]


2.FILTERING USING QUERY PARAMETER
    2A.Class --> Views.py
        
        class UserReviewsfilter2(generics.ListAPIView):
            serializer_class = ReviewSerializer1

            def get_queryset(self):
                username = self.request.query_params.get('username',None)
                return MyReview.objects.filter(reviewer_name__username=username)

    
    2B.Class --> Urls.py
        ### URLS ---> http://127.0.0.1:8000/movieapi/reviews/?username=siva
        path('reviews/<str:username>/', UserReviewsfilter2.as_view()) ,
    
2.Check Urls
    URL : http://127.0.0.1:8000/movieapi/reviews/?username=siva or 
          http://127.0.0.1:8000/movieapi/reviews/?username=demo1
    Method : GET
    HEADER:
    Body
    Output:
        [
            {
                "id": 9,
                "reviewer_name": "demo1",
                "rating": 3,
                "description": "great Super!",
                "active": true,
                "created": "2024-09-06T10:57:25.085129Z",
                "update": "2024-09-06T10:57:25.085129Z"
            },
            {
                "id": 10,
                "reviewer_name": "demo1",
                "rating": 4,
                "description": "Super!",
                "active": true,
                "created": "2024-09-06T10:57:43.323916Z",
                "update": "2024-09-06T10:57:43.323916Z"
            },
        ]


