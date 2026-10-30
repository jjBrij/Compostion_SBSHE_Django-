from rest_framework import generics
from .models import (
    SiteSettings, AboutSection, TeamMember, Sponsor, Competition, 
    GalleryItem, Champion, Testimonial, AthleteApplication, ContactMessage
)
from .serializers import (
    SiteSettingsSerializer, AboutSectionSerializer, TeamMemberSerializer, 
    SponsorSerializer, CompetitionSerializer, GalleryItemSerializer, 
    ChampionSerializer, TestimonialSerializer, AthleteApplicationSerializer, 
    ContactMessageSerializer
)

class SiteSettingsView(generics.ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

class AboutSectionView(generics.ListAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class SponsorListView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class CompetitionListView(generics.ListAPIView):
    queryset = Competition.objects.all().order_by('date')
    serializer_class = CompetitionSerializer

class GalleryListView(generics.ListAPIView):
    queryset = GalleryItem.objects.all().order_by('-created_at')
    serializer_class = GalleryItemSerializer

class ChampionListView(generics.ListAPIView):
    queryset = Champion.objects.all().order_by('-year')
    serializer_class = ChampionSerializer

class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class AthleteApplicationCreateView(generics.CreateAPIView):
    queryset = AthleteApplication.objects.all()
    serializer_class = AthleteApplicationSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer