class Car:

	def __init__(self, speed, wheels):

	    self.speed = speed
            self.wheels = wheels

        print('(Initalised car make: {})'.format(self.speed))

	def tell(self):

	    print('Speed:"{}" Wheels:"{}"'.format(self.speed, self.wheels)


class Mercedes(Car):

        def __init__(self, speed, wheels, cylinders):

           self.cylinders = cylinders

           print('Initalised Mercedes: {})'.format(self.cylinders))


class A180(Mercedes.car):

       def __init__(self, speed, wheels, cylinders, version):

           self.version = version

           print('Initalised A180: {})'.format(self.version))

t = A180(180, 4, 4, 'SE')
m = Mercedes(500, 6, 12, 'Off.road')

