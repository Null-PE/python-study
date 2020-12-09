class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self.age <= 16:
            print('plage game')
        else:
            print('work')


def main():
    person = Person('Alcie', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = 'Bob'


if __name__ == '__main__':
    main()
