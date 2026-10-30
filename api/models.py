from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Custom User Model for Admin & Judge Roles
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('JUDGE', 'Judge'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='JUDGE')
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"

# 2. Global Site Settings (Hero Section ONLY now)
class SiteSettings(models.Model):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Where Champions Are Born")
    hero_subtitle = models.TextField(default="A professional sports competition company organizing cricket tournaments...")
    hero_image = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Stats
    total_events = models.CharField(max_length=50, default="120+")
    total_athletes = models.CharField(max_length=50, default="8,500+")
    total_championships = models.CharField(max_length=50, default="45+")

    class Meta:
        verbose_name = "Hero & Settings"
        verbose_name_plural = "Hero & Settings"

    def __str__(self):
        return "Global Hero Settings"

# 3. About Page Section (Dedicated Model)
class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="Building the Stage for Champions")
    intro = models.TextField(default="Since our founding, Apex Sports has organized...")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    
    history_title = models.CharField(max_length=200, default="A Decade of Competition")
    history_subtitle = models.CharField(max_length=200, default="From a single local tournament...")
    history_content = models.TextField(default="What started as a weekend cricket league...")
    
    mission = models.TextField(default="To organize professional, fair, and unforgettable sporting competitions...")
    vision = models.TextField(default="To become the most trusted multi-sport competition company...")

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page Configuration"

# 4. Team Members (Dynamic)
class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name

# 5. Sponsors (Powered By Section)
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/', blank=True, null=True)
    
    def __str__(self):
        return self.name

# 6. Dynamic Competition Model
class Competition(models.Model):
    title = models.CharField(max_length=200)
    sport = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='competitions/')
    location = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Open', 'Registration Open'),
        ('Coming Soon', 'Coming Soon'),
        ('Closed', 'Registration Closed')
    ])
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

# 7. Dynamic Gallery Model
class GalleryItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 8. Champion Records
class Champion(models.Model):
    name = models.CharField(max_length=150)
    sport = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    position = models.CharField(max_length=50, default='Gold')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='champions/')
    
    def __str__(self):
        return f"{self.name} - {self.year}"

# 9. Dynamic Testimonials (What Athletes Say)
class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    sport = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    
    def __str__(self):
        return self.name

# 10. Athlete Applications (Apply Now Form)
class AthleteApplication(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    competition = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    achievements = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='applications/', blank=True, null=True)
    terms_agreed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.sport}"

# 11. Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"