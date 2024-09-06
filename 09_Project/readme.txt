Class Based RestApi using Serializers --> with Validation
1.Here for serialization is Done using Modelserializer Class used.
2.Views wriiten on class Based.
3.It works with 4 main methods(get,post,put,patch,delete).
4.Database used is MySQL.
5.You can create superuser --> To insert fields.
6.Here two tables are created and the linked with Foreignkey Relation.
7.In Ouput Screnshot you can see that Forign key are linked.
8.Detailed Information will be provided about Foreign Key.


Modelserializer
1.model: database Name
2.Fields
        fields = '__all__'  Returns all fields
        fields = ['name','description']
        exclude = ['description']



NESTED Serializers 

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWatchlist
        fields = '__all__'  


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchdetails = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = MyStreamPlatform
        fields = '__all__'  


**** DETAILS

Serializers: This is the base class for creating serializers. You define the fields explicitly, and it's the most flexible but requires more manual work.

ModelSerializer: This is a subclass of Serializer that automatically generates fields based on the model you provide. It simplifies the process of creating serializers for your models.

HyperlinkedModelSerializer: This is similar to ModelSerializer but includes hyperlinks in the serialized representation. Instead of just representing relationships with primary keys, it uses hyperlinks, which can be more RESTful and informative.

IF WE need only some Fields of Foreignkey we can use this methods
But it is not important.
 1.StringRelatedField
 2.PrimaryKeyRelatedField
 3.HyperLinkedRelatedKey



