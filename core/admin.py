

from django.contrib import admin

from core.savedcourse.models import SavedCourse
from core.savedscholarship.models import SavedScholarship
from core.savedschool.models import SavedSchool
from core.advisor.models import CareerQuestion, CareerQuestionAnswer, CareerQuestionOption
from core.student.models import StudentAccount
from core.testimonials.models import Testimonial
from core.news.models import News
from core.schools.models import School
from core.reviews.models import Review
from core.faculty.models import Faculty
from core.department.models import Department
from core.courses.models import Course
from core.comments.models import Comment
from core.articles.models import Article
from core.scholarships.models import Scholarship
#from core.location.models import Location
from core.requirement.models import Requirements
from core.fees.models import Tuition
from core.programs.models import Program
   


#poshpeck
admin.site.register(CareerQuestion)
admin.site.register(CareerQuestionAnswer)
admin.site.register(SavedSchool)
admin.site.register(SavedScholarship)
admin.site.register(SavedCourse)
admin.site.register(CareerQuestionOption)
admin.site.register(StudentAccount)

#pauline-banye
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Scholarship)
admin.site.register(News)
admin.site.register(Requirements)


#hezekiah
admin.site.register(Course)
admin.site.register(School)
admin.site.register(Program)


#Iconnell
admin.site.register(Review)
admin.site.register(Testimonial)


#Blaise
admin.site.register(Tuition)
#admin.site.register(Location)











