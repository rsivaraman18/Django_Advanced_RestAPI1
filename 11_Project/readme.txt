Class Based RestApi using Serializers --> with Validation
1.Here for serialization is Done using Modelserializer Class used.
2.Views wriiten on class Based.
3.It works with 4 main methods(get,post,put,patch,delete).
4.Database used is MySQL.
5.You can create superuser --> To insert fields.
6.Here two tables are created and the linked with Foreignkey Relation.

7.Here Class Based Views are created using the Mixin.

Class Based Views 3 Types
1.APIVIEW
2.MIXIN WITH GENERIC Views
3.Generic Views

IMPORTANT POINTS TO REMEMBER TO CREATE MIXINS:
    1.Urls with Id should use pk as attribute.
        http://127.0.0.1:8000/movieapi/reviews/2/
        path('reviews/<int:pk>/', Reviewbyid.as_view()) ,

    2.Import this 2 lines
        from rest_framework import mixins
        from rest_framework import generics

    3.Complete code
        ## queryset and serializer_class is attribute.Dont think it as Variable.
        class Reviewbyid(mixins.RetrieveModelMixin ,mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,  generics.GenericAPIView):
            
            queryset         = MyReview.objects.all()  
            serializer_class = ReviewSerializer

            def get(self, request, *args, **kwargs):
                return self.retrieve(request, *args, **kwargs)

            def put(self, request, *args, **kwargs):
                return self.update(request, *args, **kwargs)

            def delete(self, request, *args, **kwargs):
                return self.destroy(request, *args, **kwargs)



IMPORTANT POINTS TO REMEMBER TO CREATE GENERIC VIEWS:
