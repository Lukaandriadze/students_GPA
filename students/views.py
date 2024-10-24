import random
from django.shortcuts import render
def get_random_students():
    names = ['კობა', 'გიორგი', 'ნუგზარიკო', 'ნუკრი', 'ჯამბული', 'გრიშა', 'ბადრი', 'მიხეილ']
    surnames = ['ბარათელი', 'აღმაშენებელი', 'უსუფაშვილი', 'მაისურაძე', 'ონიანი', 'შუბლაძე']
    students = []
    for i in range(100):
        student = {
            'name': random.choice(names),
            'surname': random.choice(surnames),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4),
        }
        students.append(student)
    return students
students_cache = get_random_students()
def main_page_view(request):
    student = random.choice(students_cache)
    return render(request, 'students/main_page.html', {'student': student})
def students_page_view(request):
    return render(request, 'students/students_page.html', {'students': students_cache})
