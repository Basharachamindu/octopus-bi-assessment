from django.contrib import admin
from interview_app.models import School,Summary,Class,AssessmentArea,Student,Answers,Awards,Subject


@admin.register(School)
class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
                    
@admin.register(Summary)
class SummaryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school','syndey_participant', 'syndey_percentile','assessment_area','award','class_name','correct_answer_percentage_per_class','correct_answer','student','student_score','subject','category_id','year_level_name']


@admin.register(Class)
class ClassModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name']


@admin.register(AssessmentArea)
class AssessmentAreaModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
                    
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname']

@admin.register(Answers)
class AnswersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer']    

@admin.register(Awards)
class AwardsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  


@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_name','subject_score']  