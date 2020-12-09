class Person(object):

    __slots__ = ('_name', '_age', '_gender')

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
        if self._age <= 16:
            print('play game')
        else:
            print('work')


def main():
    person = Person('Alice', 20)
    person.play()
    person._gender = 'male'
    # AttributeError
    # person._family = True


if __name__ == '__main__':
    main()
