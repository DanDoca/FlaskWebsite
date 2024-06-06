from . import db
from .models import Course, Module

# Add courses
new_course1 = Course(title='Computer Science', description='Course 1: Computer Science')
new_course2 = Course(title='Software Engineering', description='Course 2: Software Engineering')
new_course3 = Course(title='Cyber Security', description='Course 3: Cyber Security')

db.session.add(new_course1)
db.session.add(new_course2)
db.session.add(new_course3)
db.session.commit()

# Fetch the added courses from the database to get their IDs
course1 = Course.query.filter_by(title='Computer Science').first()
course2 = Course.query.filter_by(title='Software Engineering').first()
course3 = Course.query.filter_by(title='Cyber Security').first()

# Add modules and associate them with courses
modules_data = [
    # Modules for Computer Science course
    ('COS1903', 'Scala Programming', 'Description of Scala Programming', 'Contents of Scala Programming', 'Staff 1', course1.id),
    ('COS1920', 'Database Management', 'Description of Database Management', 'Contents of Database Management', 'Staff 1', course1.id),
    ('COS2905', 'Object Oriented Programming (Java)', 'Description of OOP in Java', 'Contents of OOP in Java', 'Staff 1', course1.id),

    # Modules for Software Engineering course
    ('SE3906', 'Interaction Design', 'Description of Interaction Design', 'Contents of Interaction Design', 'Staff 2', course2.id),
    ('SE3410', 'Web Application Penetration Testing', 'Description of Pen Testing', 'Contents of Pen Testing', 'Staff 2', course2.id),
    ('SE3406', 'Fuzzy Logic & Knowledge Based Systems', 'Description of Fuzzy Logic', 'Contents of Fuzzy Logic', 'Staff 2', course2.id),

    # Modules for Cyber Security course
    ('SE3901', 'C Programming', 'Description of C Programming', 'Contents of C Programming', 'Staff 3', course3.id),
    ('SE3902', 'Computer Law and Cyber Security Management', 'Description of Cyber Security Law', 'Contents of Cyber Security Law', 'Staff 3', course3.id),
    ('SE3903', 'Linux Security', 'Description of Linux Security', 'Contents of Linux Security', 'Staff 3', course3.id),
    ('SE3904', 'Cyber Threat Intelligence and Incident Response', 'Description of Cyber Threat Intelligence', 'Contents of Cyber Threat Intelligence', 'Staff 3', course3.id)
]

for module_data in modules_data:
    new_module = Module(
        module_code=module_data[0],
        title=module_data[1],
        description=module_data[2],
        contents=module_data[3],
        staff=module_data[4],
        course_id=module_data[5]
    )
    db.session.add(new_module)

db.session.commit()

print("Courses and modules added successfully!")
