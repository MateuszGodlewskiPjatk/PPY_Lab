import Element
import MyLinkedList
from lab6.Stos import Stos
from lab6.Student import Student

element = Element.Element()

stos = Stos(10)

stos.put(1)
stos.put(2)
stos.put(3)
stos.put(4)
###print(stos.stack)
###print(stos.__str__())


student1 = Student("JanB@gmail.com", "Jan", "Bielecki")
print(student1)

