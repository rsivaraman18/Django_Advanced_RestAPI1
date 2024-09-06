Learn -> 42 to 37 Django Rest Frame Work
This only 42nd --Manual Token

TOKEN AUTHENTICATION --->
1.Settings.py --> rest_framework.authtoken
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Movieapp',
    'rest_framework',
    'rest_framework.authtoken'  Newly added
]

2.Settings.py -->

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

3.Migrate now.
4.Create Manual Token for user at Admin panel

5.Now run the url at Postman Application.
URLS : http://127.0.0.1:8000/movieapi/watch/show_reviews/
HEADERS : Authorization : Token 1f39922e828728a39363c22a91090be10c705f15


6. Update a review from Postman
Method : Put
Url : 
http://127.0.0.1:8000/movieapi/watch/3/review_create/
Headers : Authorization : Token 1f39922e828728a39363c22a91090be10c705f15(siva)
Body : 
            {
                "rating": 1,
                "description": "Bad",
                "active": true
            }


7.Create a review
Method : POST
Url:     http://127.0.0.1:8000/movieapi/watch/1/review_create/
Headers :   Authorization: Token 1f39922e828728a39363c22a91090be10c705f15
Body:    {
                "rating": 1,
                "description": "Bad",
                "active": true
            }
USER ---> Which User making this review will be analysed based on the Token.








