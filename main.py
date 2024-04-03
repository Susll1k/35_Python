class Student:
    def __init__(self, name, age, average_score):
        self.name=name
        self.age=age
        self.__average_score=average_score

    def set_average_score(self):
        name = input('Your average score: ')
        self.__average_score = name

    def get_average_score(self):
        return self.__average_score 


    def information_output(self):
        return f'Name: {self.name}\nAge: {self.age}\nAverage score: {self.get_average_score()}'

class StudentHighestCourse(Student):
    def __init__(self, name, age, average_score, name_graduate_work):
        super().__init__(name, age, average_score)
        self.name_graduate_work=name_graduate_work
    
    def information_output(self):
        return f'Name: {self.name}\nAge: {self.age}\nAverage score: {self.get_average_score()}\nThe name of the graduate work: {self.name_graduate_work}'
    
student1=Student('Mark', 19, 0)
student2=StudentHighestCourse('Franchesco', 21, 0, 'BlaBla')

student1.set_average_score()
student2.set_average_score()



print(student1.information_output())
print(student2.information_output())

