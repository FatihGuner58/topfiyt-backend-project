from django.db import models

class LandingPageContent(models.Model):
    header_title = models.CharField(max_length=200, default="Topfiyt")
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    hero_title = models.CharField(max_length=300, default="Dizi ve film dünyasının buluşma noktası")
    hero_description = models.TextField(default="Oyuncular, yapımcılar ve ekipler için profesyonel platform.")
    footer_text = models.TextField(default="© 2025 Topfiyt. Tüm hakları saklıdır.")
    footer_contact = models.CharField(max_length=200, default="info@topfiyt.com | +90 555 123 45 67")

    def __str__(self):
        return "Landing Page İçeriği"

class Feature(models.Model):
    landing_page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class SliderItem(models.Model):
    landing_page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE, related_name='sliders')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='slider_images/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class WhatIsTopfiytItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Sıralama için")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
        
class TopfiytForWhoItem(models.Model):
    CATEGORY_CHOICES = [
        ('bireysel', 'Bireysel'),
        ('kurumsal', 'Kurumsal'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Sıralama için")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='bireysel')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Footer(models.Model):
    logo = models.ImageField(upload_to='footer_logos/', null=True, blank=True)
    contact_address = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    copyright_text = models.CharField(max_length=255)
    topfiyt_for_who_title = models.CharField(max_length=255, default="TopFiyt Kimler İçin")
    topfiyt_features_title = models.CharField(max_length=255, default="TopFiyt’te Neler Var?")

    def __str__(self):
        return "Footer Ayarları"

class FooterForWhoItem(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="for_who_items")
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

class FooterFeatureItem(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="feature_items")
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content
