class Person:
  name = "Tahmid"
  id = 67
  dept = "CSE"

  def info(self):
    print(f"Name: {self.name}, ID: {self.id}, Depertment: {self.dept}")


a = Person()
a.name = "Tanmoy"
a.id = 33
# print(a.name, a.id, a.dept)
a.info()

b = Person()
b.name = "Mahmud"
b.id = 61
b.info()

th = Person()
th.info()