class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Subject(Person):
    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        return 220 - self.__age



class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Experiment:
    def __init__(self, title, date, supervisor, subject):
        self.title = title
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def __str__(self):
        return (
            f"Experiment: {self.title} ({self.date})\n"
            f"  Supervisor: {self.supervisor.full_name()}\n"
            f"  Subject: {self.subject.full_name()}, Alter: {self.subject.get_age()}, "
            f"geschätzt max. HF: {self.subject.estimate_max_hr()} bpm"
        )
