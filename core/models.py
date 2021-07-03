from django.db import models
from django.contrib.auth.models import User  # import the superuser
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField



"""ARTICLE MODEL"""
class Article(models.Model): # Create new post model

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, unique=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.title)


"""COMMENT MODEL"""
class Comment(models.Model): # Create new course model

    article = models.ForeignKey(Article, related_name='article_title', on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s - %s' % (self.article, self.commenter)


"""SCHOOL MODEL"""
class School(models.Model):

    school_name = models.CharField(max_length=200, null=True, blank=True)
    is_affiliated = models.BooleanField(null=True, blank=True, default=True)
    overview = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=235, null=True, blank=True)
    culture = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to=None, null=True, blank=True)
    school_ranking =  models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=234, null=True, blank=True)
    number_of_staff = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=234, null=True, blank=True)
    mobile = models.CharField(max_length=234, null=True, blank=True)
    email = models.EmailField(max_length=234, blank=True)
    number_of_students = models.IntegerField(null=True, blank=True)
    has_accomodation = models.BooleanField(default=True)
    min_tuition = models.IntegerField(null=True, blank=True)
    max_tuition = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.school_name


"""COURSE MODEL"""
class Course(models.Model):
    
    PROGRAM_CHOICES = (
        ('phD', 'Doctorate'),
        ('ms', 'Masters'),
        ('bs', 'Bachelors'),
        ('dip', 'Diploma'),
    )

    STUDY_CHOICES = (
        ('fulltime', 'Full Time'),
        ('parttime', 'Part Time'),
        ('both', 'Both'),
    )

    course_name = models.CharField(max_length=200, null=True, blank=True, default='')
    school = models.ForeignKey(School,  related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    tution_fees = models.IntegerField(null=True, blank=True, default=0)
    requirements = models.CharField(max_length=200, null=True, blank=True, default='')
    program_options = models.CharField(max_length=200, choices=PROGRAM_CHOICES, null=True)
    study_option = models.CharField(max_length=233, choices=STUDY_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.course_name


"""SCHOLARSHIP MODEL"""
#options for scholarship class
class Scholarship(models.Model): # Create new scholarship model

    FUNDING_CHOICES = (
        ('CHOOSE', '.....'),
        ('PARTIAL', 'Partial funding'),
        ('FULL', 'Fully funded'),
    )

    DEGREE = (
        ('CHOOSE', '.....'),
        ('UNDERGRADUATE', 'Undergraduates only'),
        ('MASTERS', 'Masters only'),
        ('DOCTORATE', 'PhD only'),
        ('ALL', 'All degrees'),
    )

    name = models.CharField(max_length=150, help_text='Enter Name of Scholarship', blank=False, unique=True)
    donor = models.CharField(max_length=150, help_text='Enter Name of Scholarship Donor', blank=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    institution = models.ForeignKey(School, default=1, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    funding = models.CharField(max_length=15, choices=FUNDING_CHOICES, verbose_name=('Type of funding'), default='.....')
    degree_level = models.CharField(max_length=30, choices=DEGREE, default='.....')
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    deadline = models.DateField(verbose_name=('Application deadline'))
    requirements = models.TextField(verbose_name=('Application requirements')) 
    date_published = models.DateField()
    contact = models.CharField(max_length=250, help_text='Enter full name of Contact person')
    telephone = PhoneNumberField(help_text='Enter phone number of Contact person')
    email = models.EmailField(max_length=200, help_text='Enter email of Contact person', blank=False, unique=True)
    website = models.URLField(max_length=250, help_text='Enter scholarship application website', blank=False, unique=True)  

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return "{}".format(self.name)
