class Vector:
    def __init__(self, *args):
        try:
            iter(args)
            self._args = [i for i in args[0]]
        except:
            self._args = list(args)

    def __str__(self):
        return '<' + str(self._args)[1:-1] + '>'

    def __repr__(self):
        return f'Vector({str(self._args)[1:-1]})'

    def __len__(self):
        return len(self._args)

    def __contains__(self, val):
        return (val in self._args)

    def __getitem__(self, val):
        return self._args[val]

    def __setitem__(self, oldVal, newVal):
        self._args[oldVal] = newVal

    def copy(self):
        return Vector(self._args)

    def __add__(self, other):
        return Vector([self._args[i] + other[i] for i in range(len(other))])

    def __mul__(self, other):
        return Vector([self._args[i]*other for i in range(len(self._args))])

    def __rmul__(self, other):
        return Vector(self._args)*other

    def __eq__(self, other):
        return self._args == other._args

    def __gt__(self, other):
        return self._args > other._args

    def __le__(self, other):
        return self._args <= other._args

    def dot(self, other):
        return sum([self._args[i] * other[i] for i in range(len(self._args))])

    def norm(self):
        return sum([i*i for i in self._args]) ** 0.5

    def __iter__(self):
        return iter(self._args)

    def __next__(self):
        return next(self._args)
