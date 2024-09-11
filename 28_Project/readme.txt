PROJECT 28 ---> PAGINATION -->51,57,56,55

1.To make Clear understanding we plan to make some Changes to Serializers.
    So that you can view the pagination Easily.
    class WatchlistSerializer(serializers.ModelSerializer):
        # reviewinfo = ReviewSerializer1(many=True,read_only=True)
        platform = serializers.CharField(source='platform.name')
        class Meta:
            model = MyWatchlist
            fields = '__all__'  


2.Pagination Types
    1.Page Number --57
    2.Limit Offset -- 56
    3.Cursor Pagination --55


3.Create a new file -->pagination.py
    3A.Pagination.py
        from rest_framework.pagination import PageNumberPagination

        class WatchlistPagination(PageNumberPagination):
            page_size = 3

    3B. Urls
        path('watchlist_paginationview/',         watchlist_paginationview1.as_view()) ,

    3C.Views
        from Movieapp.pagination import WatchlistPagination
        from rest_framework import filters
        class watchlist_paginationview1(generics.ListAPIView):
            queryset = MyWatchlist.objects.all()
            serializer_class = WatchlistSerializer
            pagination_class = WatchlistPagination
            filter_backends = [filters.OrderingFilter]
            search_fields = ['avg_rating']

    3D.Check Urls
        Url: http://127.0.0.1:8000/movieapi/watchlist_paginationview/
        Method : GET
        Output: {
                    "count": 9,
                    "next": "http://127.0.0.1:8000/movieapi/watchlist_paginationview/?page=2",
                    "previous": null,
                    "results": [
                        {
                            "id": 1,
                            "platform": "Youtube",
                            "title": "Jailor",
                            "storyline": "Crime,Thriller",
                            "active": true,
                            "created": "2024-09-05",
                            "avg_rating": 2.0,
                            "number_rating": 2
                        },
                    ]
                 }
    



4.Like this Change any attribute at Pagination.py and check the Changes.
    class WatchlistPagination(PageNumberPagination):
    page_size = 3
    ### REST ATTRIBUTE ARE OPTIONAL
    # page_query_param  = 'p'
    page_size_query_param  = 'newsize' #### http://127.0.0.1:8000/movieapi/watchlist_paginationview/?newsize=7
    max_page_size =5  #### Restricted the maximum size.
    # last_page_strings = 'end'   ### http://127.0.0.1:8000/movieapi/watchlist_paginationview/?page=end

5.Pagination-LimitOffset

    5A.Urls.py
        path('watchlist_limitpaginationview/',    watchlist_limitpaginationview.as_view()) ,
    5B.Views.py
        from Movieapp.pagination import WatchlistPagination
        from rest_framework import filters
        class watchlist_limitpaginationview(generics.ListAPIView):
            queryset = MyWatchlist.objects.all()
            serializer_class = WatchlistSerializer
            pagination_class = WatchlistPagination2LOP
            filter_backends = [filters.OrderingFilter]
            search_fields = ['avg_rating']

    5C.Pagination.py
        class WatchlistPagination2LOP(LimitOffsetPagination):
        default_limit =5

    5D.Check LOP
        Url: http://127.0.0.1:8000/movieapi/watchlist_limitpaginationview/
        Method: GET


6.Lets Do for Cursor Pagination
    6A.Urls.py
        

    6B.Views.py

    6c.Pagination.py

    6D.Check with Postman

