from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Auth Endpoints
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Data Endpoints
    path('settings/', views.SiteSettingsView.as_view(), name='site-settings'),
    path('about/', views.AboutSectionView.as_view(), name='about-section'),
    path('team/', views.TeamMemberListView.as_view(), name='team'),
    path('sponsors/', views.SponsorListView.as_view(), name='sponsors'),
    path('competitions/', views.CompetitionListView.as_view(), name='competitions'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('champions/', views.ChampionListView.as_view(), name='champions'),
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonials'),
    
    # Form Submissions
    path('apply/', views.AthleteApplicationCreateView.as_view(), name='apply'),
    path('contact/', views.ContactMessageCreateView.as_view(), name='contact'),
]