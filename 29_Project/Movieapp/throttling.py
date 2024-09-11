## NEW FILE CREATED FOR CUSTOMIZE THROTTLING

from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'

class ReviewAllThrottle(UserRateThrottle):
    scope = 'review-all'