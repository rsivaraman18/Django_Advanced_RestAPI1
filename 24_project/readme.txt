Throttling...50-->49-->48
Throttling examples -- 50 request/day or 10 request/user
                       2request/day for unregistered user
Project Continues with Django Token Authentication and not JWT Used.

Throttling Types:
    1.AnonRateThrottle --> Not Registered User
    2.UserRateThrottle --> Registered User


Lets Start
1.To set the Throtling to entire Project or globally
    1A.Setting files -->  Add this Throttling Class
        'DEFAULT_THROTTLE_CLASSES': [
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ],
        'DEFAULT_THROTTLE_RATES': {
            'anon': '1/day',
            'user': '3/day'
        }
    1B.Unknown--> 1 request/day , registered--> 3 request/day    
        Check with any request
        URL : http://127.0.0.1:8000/movieapi/movie/3/review_detail/
        Method : GET
        body : --
        Authentication : -
        Output before allowed request :
                                        {
                                            "id": 1,
                                            "reviewer_name": "siva",
                                            "rating": 4,
                                            "description": "Very good",
                                            "active": true,
                                            "created": "2024-09-05T07:36:20.365124Z",
                                            "update": "2024-09-05T07:36:20.365124Z"
                                        }
        Output after 1 request: {
                "detail": "Request was throttled. Expected available in 86393 seconds."
            }



2.To set Throtling to each view Class/Locally
    2A.Now Comment the Global throtling already applied in Settings.
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.TokenAuthentication',
            ],

            # 'DEFAULT_THROTTLE_CLASSES': [
            #     'rest_framework.throttling.AnonRateThrottle',
            #     'rest_framework.throttling.UserRateThrottle'
            # ],
            'DEFAULT_THROTTLE_RATES': {
                'anon': '1/day',
                'user': '3/day'
            }
        }

    2B.Then add the throttle class where you need.
        Movieapp --> views.py

        from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
        class ReviewbyId(generics.RetrieveUpdateDestroyAPIView):
    
            permission_classes = [IsReviewUserorReadOnlyorStaff] 
            queryset         = MyReview.objects.all()
            serializer_class = ReviewSerializer1
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    2C.Check with Postman
        URL : http://127.0.0.1:8000/movieapi/movie/3/review_detail/
        Method : GET
        HEADERS : Authorization : Token 22323a449af6c69e0efdac51bfc491529d586d7b

        BODY : --- 
        OUTPUT: Upto 4 request it will provide result. 
        OUTPUT : {
                    "detail": "Request was throttled. Expected available in 86395 seconds."
                }

Note: If you set the throttling class for 2 Class Based Views.
      then the request will be counted together.
      For eg: If total 10 allowed.  
             If u made 6 request with url1(class1) and
             then only 4 request left for url2(class2).
