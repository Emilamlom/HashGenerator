class Hashes:
    def hash(radius):
        '''
        Function to compute the area of a circle.
        :param radius: Radius of the circle
        :return: the circle's area
        '''
        try:
            radius = float(radius)
            if radius <= 0:
                raise ValueError('Values for area cannot be negative')
            else:
                return (radius ** 2) * pi
        except ValueError as e:
            return e