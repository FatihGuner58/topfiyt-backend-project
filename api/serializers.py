from rest_framework import serializers
from .models import (
    LandingPageContent, SliderItem, Feature,
    WhatIsTopfiytItem, TopfiytForWhoItem,
    Footer, FooterFeatureItem, FooterForWhoItem
)


class SliderItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = SliderItem
        fields = ['id', 'title', 'description', 'image_url', 'order']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'title', 'description']


class LandingPageContentSerializer(serializers.ModelSerializer):
    sliders = SliderItemSerializer(many=True, read_only=True)
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = LandingPageContent
        fields = '__all__'


class WhatIsTopfiytItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatIsTopfiytItem
        fields = ['id', 'title', 'description', 'order']


class TopfiytForWhoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopfiytForWhoItem
        fields = ['id', 'title', 'description', 'order', 'category']

class FooterFeatureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterFeatureItem
        fields = ['id', 'content']

class FooterForWhoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterForWhoItem
        fields = ['id', 'content']

class FooterSerializer(serializers.ModelSerializer):
    feature_items = FooterFeatureItemSerializer(many=True, read_only=True)
    for_who_items = FooterForWhoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Footer
        fields = [
            'id', 'logo', 'contact_address', 'contact_phone', 'contact_email',
            'facebook_url', 'linkedin_url', 'instagram_url',
            'copyright_text', 'topfiyt_for_who_title', 'topfiyt_features_title',
            'feature_items', 'for_who_items'
        ]