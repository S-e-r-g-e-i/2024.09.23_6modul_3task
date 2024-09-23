# Множественное наследование

class Horse:                                    # класс описывающий лошадь
    x_distance = 0                              # пройденный путь.
    sound = 'Frrr'                              # звук, который издаёт лошадь

    def run(self, dx):                          # изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    y_distance = 0                              # высота полёта
    sound = 'I train, eat, sleep, and repeat'   # звук, который издаёт орёл (отсылка)

    def fly(self, dy):                          # изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):                    # класс описывающий пегаса

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        coordinate = (self.x_distance, self.y_distance)
        return coordinate

    def voice(self):
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())  # ??? все правильно же, почему должно быть "I train, eat, sleep, and repeat"??? 

p1.voice()

print(Pegasus.mro())