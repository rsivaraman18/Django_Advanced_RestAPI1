from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination 


class WatchlistPagination(PageNumberPagination):
    page_size = 3
    ### REST ATTRIBUTE ARE OPTIONAL
    # page_query_param  = 'p'
    page_size_query_param  = 'newsize' #### http://127.0.0.1:8000/movieapi/watchlist_paginationview/?newsize=7
    max_page_size =5  #### Restricted the maximum size.
    # last_page_strings = 'end'   ### http://127.0.0.1:8000/movieapi/watchlist_paginationview/?page=end


class WatchlistPagination2LOP(LimitOffsetPagination):
    default_limit =3
    max_limit = 4
    limit_query_param = 'start'
    offset_query_param = 'end'


