from rest_framework import serializers
from .models import (
    SiteSettings, AboutSection, TeamMember, Sponsor, Competition, 
    GalleryItem, Champion, Testimonial, AthleteApplication, ContactMessage
)

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class AthleteApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteApplication
        fields = '__all__'

    def validate_profile_photo(self, value):
        if value and value.size > 4 * 1024 * 1024:
            raise serializers.ValidationError("Image file too large ( > 4MB ).")
        return value

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'