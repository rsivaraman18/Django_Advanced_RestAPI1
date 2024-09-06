Class Based RestApi using Serializers --> with Validation
1.Here for serialization is Done using Modelserializer Class used.
2.Views wriiten on class Based.
3.It works with 4 main methods(get,post,put,patch,delete).
4.Database used is MySQL.
5.You can create superuser --> To insert fields.
6.Here two tables are created and the linked with Foreignkey Relation.
7.In Ouput Screnshot you can see that Forign key are linked.
8.Here the Detailed Info of Foreign KEy were given see the Output of Project 8 and Project 9.


Modelserializer
1.model: database Name
2.Fields
        fields = '__all__'  Returns all fields
        fields = ['name','description']
        exclude = ['description']

    

