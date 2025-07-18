from django.contrib import admin
from django.utils.html import format_html
from .models import LandingPageContent, Feature, SliderItem, WhatIsTopfiytItem, TopfiytForWhoItem, Footer, FooterForWhoItem, FooterFeatureItem

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1 

@admin.register(LandingPageContent)
class LandingPageContentAdmin(admin.ModelAdmin):
    list_display = ('header_title', 'logo_preview')
    readonly_fields = ('logo_preview',)
    inlines = [FeatureInline]

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.logo.url)
        return "Logo yok"
    logo_preview.short_description = "Logo Önizleme"

@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']

@admin.register(WhatIsTopfiytItem)
class WhatIsTopfiytItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']
    list_editable = ['order']

@admin.register(TopfiytForWhoItem)
class TopfiytForWhoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']
    list_editable = ['order']

class FooterForWhoItemInline(admin.TabularInline):
    model = FooterForWhoItem
    extra = 1

class FooterFeatureItemInline(admin.TabularInline):
    model = FooterFeatureItem
    extra = 1

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = (
        'logo_preview', 
        'contact_address', 
        'contact_phone', 
        'contact_email',
        'facebook_url',
        'linkedin_url',
        'instagram_url'
    )
    inlines = [FooterForWhoItemInline, FooterFeatureItemInline]

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80" height="auto" />', obj.logo.url)
        return "-"
    logo_preview.short_description = "Logo"