from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, SiteSettings, AboutSection, TeamMember, Sponsor, 
    Competition, GalleryItem, Champion, Testimonial, 
    AthleteApplication, ContactMessage
)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = "Apex Sports Admin Panel"
admin.site.site_title = "Apex Sports Admin"
admin.site.index_title = "Welcome to the Apex Sports Dashboard"

# --- Custom Admin Views ---
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'total_events')

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sport', 'date', 'status', 'is_featured')
    list_filter = ('sport', 'status', 'is_featured')
    search_fields = ('title', 'location')

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'year', 'position')
    list_filter = ('sport', 'year')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'rating')

@admin.register(AthleteApplication)
class AthleteApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sport', 'competition', 'submitted_at')
    list_filter = ('sport', 'competition')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')