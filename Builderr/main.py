

from Student import Student

if __name__ == "__main__":
   name=input("Enter your name: ")
   age=int(input("Enter your age: "))
   course=input("Enter your course: ")
   email=input("Enter your email: ")
   s=Student.Builder().set_name(name).set_age(age).set_course(course).set_email(email).build()
   print(s)