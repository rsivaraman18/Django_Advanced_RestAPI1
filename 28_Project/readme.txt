PROJECT 28 ---> PAGINATION

1.To make Clear understanding we plan to make some Changes to Serializers.
    So that you can view the pagination Easily.
    class WatchlistSerializer(serializers.ModelSerializer):
        # reviewinfo = ReviewSerializer1(many=True,read_only=True)
        platform = serializers.CharField(source='platform.name')
        class Meta:
            model = MyWatchlist
            fields = '__all__'  

