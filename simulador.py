from faker import Faker
import random

fake = Faker()

departamentos = []


def get_departmento(number):
    global departamentos
    global fake
    from university.models import Departament

    if len(departamentos) != number:
        departamentos=[]
        for x in range(number):
            departamentos.append(Departament.objects.create(
                name = fake.company(),
                budget = fake.random_int(min=4, max=20, step=1)
            ))
    random.shuffle(departamentos)
    return departamentos[0]

def get_user():
    global fake
    from django.contrib.auth.models import User
    profile =  fake.profile()
    user = User.objects.create_user(profile['username'], profile['mail'], 'admin12345')
    user.first_name = fake.first_name()
    user.last_name = fake.last_name()
    user.is_staff=True
    user.is_active=True
    user.save()
    return user, profile

def generate_student():
    from university.models import Student
    from django.core.files import File

    user, profile = get_user()
    student=Student(user=user)
    foto = 'university/static/img/woman.png' if profile['sex'] == 'M' else 'university/static/img/man.png'
    with open(foto, 'rb') as arch:
        student.photo = File(arch, name=profile['name']+'.png')
        student.save()
    return student

def get_instructor(cantidad_depa):
    global fake
    from university.models import  Instructor, Office

    user, prof = get_user()
    instructor = Instructor.objects.create(
        user=user,
        office = Office.objects.create(location=fake.slug()),
        departament = get_departmento(cantidad_depa)
    )

    return instructor

def get_numero_no_repedito(lista, maximo):
    dev = -1
    while dev == -1 or dev in lista:
        dev = random.randint(0, maximo)
    return dev

def crear_cursos(num_cursos, estudiantes, instructores):
    from university.models import Course
    global fake

    for x in range(num_cursos):
        prof = instructores[random.randint(0, len(instructores)-1)]
        curso = Course.objects.create(
            title = fake.license_plate(),
            credits = random.randint(2, 12),
            instructor=prof
        )
        estudiantes_add = []
        for y in range(random.randint(10, 30)):
            num = get_numero_no_repedito(estudiantes_add, len(estudiantes)-1)
            curso.students.add(estudiantes[num])
            estudiantes_add.append(num)
        curso.save()

def create_simulation():
    estudiantes = []
    instructores = []
    for x in range(40):
        estudiantes.append(generate_student())

    for x in range(10):
        instructores.append(get_instructor(3))
    crear_cursos(15, estudiantes, instructores)

if __name__ == '__main__':
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fsd.settings")
    django.setup()
    create_simulation()

