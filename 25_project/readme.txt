Customized Throttling ... 50

1.Create a new throttling File and write the class.
    Movieapp -->throttling.py
    
        from rest_framework.throttling import UserRateThrottle

        class ReviewCreateThrottle(UserRateThrottle):
            scope = 'review-create'

        class ReviewAllThrottle(UserRateThrottle):
            scope = 'review-all'

2.In Setting set the scope.
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],


        'DEFAULT_THROTTLE_RATES': {
            'anon': '1/day',
            'user': '3/day',
            'review-create': '1/day' ,
            'review-all': '5/day' ,
        } 
}

3. Movieapp -->views.py
    from Movieapp.throttling import ReviewCreateThrottle,ReviewAllThrottle
    
    class ReviewAll(generics.ListCreateAPIView): 
        queryset         = MyReview.objects.all()
        serializer_class = ReviewSerializer1
        throttle_classes = [ReviewAllThrottle]

    
    class AddNewReviewtoWatchlist(generics.CreateAPIView):
        serializer_class = ReviewSerializer1
        permission_classes = [IsAuthenticated] 
        throttle_classes = [ReviewCreateThrottle]

4.Lets check with Urls
    4a.Create review checking
        URL : http://127.0.0.1:8000/movieapi/movie/1/review_create/
        Method : POST
        Body: rating:3
        authentication 
        Output before limit : Review Placed
        Output after limit: {
                    "detail": "Request was throttled. Expected available in 86387 seconds."
                    }

    4b.Review all checking
       URL : http://127.0.0.1:8000/movieapi/movie/showall_reviews/
        Method : GET
        Body: --- 
        Output before limit : Show all Reviews
        Output after limit: {
                    "detail": "Request was throttled. Expected available in 86387 seconds."
                    } 


5.Now Lets Learn ScopedRate Throttling.
    --> It reduces the code.
    --> It Doesnot want any new file like throttling as we did earlier.

    5A.Choose any Class you want throttling and write this 3 lines.
        3 lines --> from rest_framework.throttling import ScopedRateThrottle
                    throttle_classes = [ScopedRateThrottle]
                    throttle_scope   = 'review-detail-throttle'
        example:
            from rest_framework.throttling import ScopedRateThrottle
            class ReviewbyId(generics.RetrieveUpdateDestroyAPIView):
        
                permission_classes = [IsReviewUserorReadOnlyorStaff] 
                queryset         = MyReview.objects.all()
                serializer_class = ReviewSerializer1
                throttle_classes = [ScopedRateThrottle]
                throttle_scope   = 'review-detail-throttle'
    
    5B.Write this scope throttle in setting as shown.
        
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.TokenAuthentication',
            ],


            'DEFAULT_THROTTLE_RATES': {
                'review-detail-throttle':'7/day',
            } 
        }
