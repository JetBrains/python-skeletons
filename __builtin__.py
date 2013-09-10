"""Skeletons for built-in symbols."""

import sys


def abs(number):
    """Return the absolute value of the argument.

    :type number: T
    :rtype: T | unknown
    """
    pass


def all(iterable):
    """Return True if bool(x) is True for all values x in the iterable.

    :type iterable: collections.Iterable
    :rtype: bool
    """
    pass


def any(iterable):
    """Return True if bool(x) is True for any x in the iterable.

    :type iterable: collections.Iterable
    :rtype: bool
    """
    pass


def bin(number):
    """Return the binary representation of an integer or long integer.

    :type number: numbers.Number
    :rtype: bytes
    """
    pass


def callable(object):
    """Return whether the object is callable (i.e., some kind of function).
    Note that classes are callable, as are instances with a __call__() method.

    :rtype: bool
    """
    pass


def chr(i):
    """Return a string of one character with ordinal i; 0 <= i < 256.

    :type i: int
    :rtype: string
    """
    pass


def cmp(x, y):
    """Return negative if x<y, zero if x==y, positive if x>y.

    :rtype: int
    """
    pass


def dir(object=None):
    """If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.

    :rtype: list[string]
    """
    pass


def divmod(x, y):
    """Return the tuple ((x-x%y)/y, x%y).

    :type x: numbers.Number
    :type y: numbers.Number
    :rtype: (int | long | float | unknown, int | long | float | unknown)
    """
    pass


def filter(function_or_none, sequence):
    """Return those items of sequence for which function(item) is true. If
    function is None, return the items that are true. If sequence is a tuple
    or string, return the same type, else return a list.

    :type function_or_none: collections.Callable | None
    :type sequence: T <= list | collections.Iterable | bytes | unicode
    :rtype: T
    """
    pass


def getattr(object, name, default=None):
    """Get a named attribute from an object; getattr(x, 'y') is equivalent to
    x.y. When a default argument is given, it is returned when the attribute
    doesn't exist; without it, an exception is raised in that case.

    :type name: string
    :rtype: object | unknown
    """
    pass


def globals():
    """Return the dictionary containing the current scope's global variables.

    :rtype: dict[string, unknown]
    """
    pass


def hasattr(object, name):
    """Return whether the object has an attribute with the given name.

    :type name: string
    :rtype: bool
    """
    pass


def hash(object):
    """Return a hash value for the object.

    :rtype: int
    """
    pass


def hex(number):
    """Return the hexadecimal representation of an integer or long integer.

    :type number: numbers.Integral
    :rtype: string
    """
    pass


def id(object):
    """Return the identity of an object.

    :rtype: int
    """
    pass


def isinstance(object, class_or_type_or_tuple):
    """Return whether an object is an instance of a class or of a subclass
    thereof.

    :rtype: bool
    """
    pass


def issubclass(C, B):
    """Return whether class C is a subclass (i.e., a derived class) of class B.

    :rtype: bool
    """
    pass


def iter(source, sentinel=None):
    """Get an iterator from an object. In the first form, the argument must
    supply its own iterator, or be a sequence. In the second form, the callable
    is called until it returns the sentinel.

    :type source: collections.Iterable[T]
    :rtype: collections.Iterator[T]
    """
    pass


def len(object):
    """Return the number of items of a sequence or mapping.

    :type object: collections.Sized
    :rtype: int
    """
    pass


def locals():
    """Update and return a dictionary containing the current scope's local
    variables.

    :rtype: dict[string, unknown]
    """
    pass


def map(function, sequence, *sequence_1):
    """Return a list of the results of applying the function to the items of
    the argument sequence(s).

    :type function: ((T) -> V) | None
    :type sequence: collections.Iterable[T]
    :rtype: list[V] | bytes | unicode
    """
    pass


def next(iterator, default=None):
    """Return the next item from the iterator.

    :type iterator: collections.Iterator[T]
    :rtype: T
    """
    pass


def oct(number):
    """Return the octal representation of an integer or long integer.

    :type number: numbers.Integral
    :rtype: string
    """
    pass


def open(name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=None, opener=None):
    """Open a file, returns a file object.

    :type name: string
    :type mode: string
    :type buffering: int
    :type encoding: string | None
    :type errors: string | None
    :rtype: file
    """
    pass


def ord(c):
    """Return the integer ordinal of a one-character string.

    :type c: string
    :rtype: int
    """
    pass


def pow(x, y, z=None):
    """With two arguments, equivalent to x**y. With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).

    :type x: numbers.Number
    :type y: numbers.Number
    :type z: numbers.Number | None
    :rtype: int | long | float | complex
    """
    pass


if sys.version_info < (3,):
    def range(start, stop=None, step=None):
        """Return a list containing an arithmetic progression of integers.

        :type start: numbers.Integral
        :type stop: numbers.Integral | None
        :type step: numbers.Integral | None
        :rtype: list[int]
        """
        pass


def reduce(function, sequence, initial=None):
    """Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.

    :type function: collections.Callable
    :type sequence: collections.Iterable
    :type initial: T
    :rtype: T | unknown
    """
    pass


def repr(object):
    """
    Return the canonical string representation of the object.

    :rtype: string
    """
    pass


def round(number, ndigits=None):
    """Round a number to a given precision in decimal digits (default 0 digits).

    :type number: numbers.Real
    :type ndigits: numbers.Real | None
    :rtype: float
    """
    pass


class slice(object):
    def __init__(self, start, stop=None, step=None):
        """Create a slice object. This is used for extended slicing (e.g. a[0:10:2]).

        :type start: numbers.Integral
        :type stop: numbers.Integral | None
        :type step: numbers.Integral | None
        """
        return


def vars(object=None):
    """Without arguments, equivalent to locals(). With an argument, equivalent
    to object.__dict__.

    :rtype: dict[string, unknown]
    """
    pass


class object:
    """ The most base type."""

    @staticmethod
    def __new__(cls, *more):
        """Create a new object.

        :type cls: T
        :rtype: T
        """
        pass


class enumerate(object):
    """enumerate object."""

    def __init__(self, iterable, start=0):
        """Create an enumerate object.

        :type iterable: collections.Iterable[T]
        :type start: int | long
        :rtype: enumerate[int, T]
        """
        pass

    def next(self):
        """Return the next value, or raise StopIteration.

        :rtype: (int, T)
        """
        pass

    def __iter__(self):
        """x.__iter__() <==> iter(x).

        :rtype: enumerate[int, T]
        """
        pass


if sys.version_info < (3,):
    class xrange(object):
        """xrange object."""

        def __init__(self, start, stop=None, step=None):
            """Create an xrange object.

            :type start: numbers.Integral
            :type stop: numbers.Integral | None
            :type step: numbers.Integral | None
            :rtype: xrange[int]
            """
            pass


class int(object):
    """Integer numeric type."""

    def __init__(self, x=None, base=10):
        """Convert a number or string x to an integer, or return 0 if no
        arguments are given.

        :type x: object
        :type base: numbers.Integral
        """
        pass

    def __add__(self, y):
        """Sum of x and y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __sub__(self, y):
        """Difference of x and y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __mul__(self, y):
        """Product of x and y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __floordiv__(self, y):
        """Floored quotient of x and y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __mod__(self, y):
        """Remainder of x / y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __pow__(self, y, modulo=None):
        """x to the power y.

        :type y: numbers.Number
        :type modulo: numbers.Integral | None
        :rtype: int
        """
        pass

    def __lshift__(self, n):
        """x shifted left by n bits.

         :type n: numbers.Integral
         :rtype: int
         """
        pass

    def __rshift__(self, n):
        """x shifted right by n bits.

         :type n: numbers.Integral
         :rtype: int
         """
        pass

    def __and__(self, y):
        """Bitwise and of x and y.

        :type y: numbers.Integral
        :rtype: int
        """
        pass

    def __or__(self, y):
        """Bitwise or of x and y.

        :type y: numbers.Integral
        :rtype: int
        """
        pass

    def __xor__(self, y):
        """Bitwise exclusive or of x and y.

        :type y: numbers.Integral
        :rtype: int
        """
        pass

    def __div__(self, y):
        """Quotient of x and y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __truediv__(self, y):
        """Quotient of x and y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __radd__(self, y):
        """Sum of y and x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rsub__(self, y):
        """Difference of y and x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rmul__(self, y):
        """Product of y and x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rfloordiv__(self, y):
        """Floored quotient of y and x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rmod__(self, y):
        """Remainder of y / x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rpow__(self, y):
        """x to the power y.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rlshift__(self, y):
        """y shifted left by x bits.

         :type y: numbers.Integral
         :rtype: int
         """
        pass

    def __rrshift__(self, y):
        """y shifted right by n bits.

         :type y: numbers.Integral
         :rtype: int
         """
        pass

    def __rand__(self, y):
        """Bitwise and of y and x.

        :type y: numbers.Integral
        :rtype: int
        """
        pass

    def __ror__(self, y):
        """Bitwise or of y and x.

        :type y: numbers.Integral
        :rtype: int
        """
        pass

    def __rxor__(self, y):
        """Bitwise exclusive or of y and x.

        :type y: numbers.Integral
        :rtype: int
        """
        pass

    def __rdiv__(self, y):
        """Quotient of y and x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __rtruediv__(self, y):
        """Quotient of y and x.

        :type y: numbers.Number
        :rtype: int
        """
        pass

    def __pos__(self):
        """x unchanged.

        :rtype: int
        """
        pass

    def __neg__(self):
        """x negated.

        :rtype: int
        """
        pass

    def __invert__(self):
        """The bits of x inverted.

        :rtype: int
        """
        pass


if sys.version_info < (3,):
    class long(object):
        """Long integer numeric type."""

        def __init__(self, x=None, base=10):
            """Convert a number or string x to a long integer, or return 0 if
            no arguments are given.

            :type x: object
            :type base: numbers.Integral
            """
            pass

        def __add__(self, y):
            """Sum of x and y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __sub__(self, y):
            """Difference of x and y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __mul__(self, y):
            """Product of x and y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __floordiv__(self, y):
            """Floored quotient of x and y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __mod__(self, y):
            """Remainder of x / y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __pow__(self, y, modulo=None):
            """x to the power y.

            :type y: numbers.Number
            :type modulo: numbers.Integral | None
            :rtype: long
            """
            pass

        def __lshift__(self, n):
            """x shifted left by n bits.

             :type n: numbers.Integral
             :rtype: long
             """
            pass

        def __rshift__(self, n):
            """x shifted right by n bits.

             :type n: numbers.Integral
             :rtype: long
             """
            pass

        def __and__(self, y):
            """Bitwise and of x and y.

            :type y: numbers.Integral
            :rtype: long
            """
            pass

        def __or__(self, y):
            """Bitwise or of x and y.

            :type y: numbers.Integral
            :rtype: long
            """
            pass

        def __xor__(self, y):
            """Bitwise exclusive or of x and y.

            :type y: numbers.Integral
            :rtype: long
            """
            pass

        def __div__(self, y):
            """Quotient of x and y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __truediv__(self, y):
            """Quotient of x and y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __radd__(self, y):
            """Sum of y and x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rsub__(self, y):
            """Difference of y and x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rmul__(self, y):
            """Product of y and x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rfloordiv__(self, y):
            """Floored quotient of y and x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rmod__(self, y):
            """Remainder of y / x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rpow__(self, y):
            """x to the power y.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rlshift__(self, y):
            """y shifted left by x bits.

             :type y: numbers.Integral
             :rtype: long
             """
            pass

        def __rrshift__(self, y):
            """y shifted right by n bits.

             :type y: numbers.Integral
             :rtype: long
             """
            pass

        def __rand__(self, y):
            """Bitwise and of y and x.

            :type y: numbers.Integral
            :rtype: long
            """
            pass

        def __ror__(self, y):
            """Bitwise or of y and x.

            :type y: numbers.Integral
            :rtype: long
            """
            pass

        def __rxor__(self, y):
            """Bitwise exclusive or of y and x.

            :type y: numbers.Integral
            :rtype: long
            """
            pass

        def __rdiv__(self, y):
            """Quotient of y and x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __rtruediv__(self, y):
            """Quotient of y and x.

            :type y: numbers.Number
            :rtype: long
            """
            pass

        def __pos__(self):
            """x unchanged.

            :rtype: long
            """
            pass

        def __neg__(self):
            """x negated.

            :rtype: long
            """
            pass

        def __invert__(self):
            """The bits of x inverted.

            :rtype: long
            """
            pass


class float(object):
    """Floating point numeric type."""

    def __init__(self, x=None):
        """Convert a string or a number to floating point.

        :type x: object
        """
        pass

    def __add__(self, y):
        """Sum of x and y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __sub__(self, y):
        """Difference of x and y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __mul__(self, y):
        """Product of x and y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __floordiv__(self, y):
        """Floored quotient of x and y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __mod__(self, y):
        """Remainder of x / y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __pow__(self, y):
        """x to the power y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __div__(self, y):
        """Quotient of x and y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __truediv__(self, y):
        """Quotient of x and y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __radd__(self, y):
        """Sum of y and x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rsub__(self, y):
        """Difference of y and x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rmul__(self, y):
        """Product of y and x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rfloordiv__(self, y):
        """Floored quotient of y and x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rmod__(self, y):
        """Remainder of y / x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rpow__(self, y):
        """x to the power y.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rdiv__(self, y):
        """Quotient of y and x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __rtruediv__(self, y):
        """Quotient of y and x.

        :type y: numbers.Number
        :rtype: float
        """
        pass

    def __pos__(self):
        """x unchanged.

        :rtype: float
        """
        pass

    def __neg__(self):
        """x negated.

        :rtype: float
        """
        pass


class complex(object):
    """Complex numeric type."""

    def __init__(self, real=None, imag=None):
        """Create a complex number with the value real + imag*j or convert a
        string or number to a complex number.

        :type real: object
        :type imag: object
        """
        pass

    def __add__(self, y):
        """Sum of x and y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __sub__(self, y):
        """Difference of x and y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __mul__(self, y):
        """Product of x and y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __floordiv__(self, y):
        """Floored quotient of x and y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __mod__(self, y):
        """Remainder of x / y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __pow__(self, y):
        """x to the power y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __div__(self, y):
        """Quotient of x and y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __truediv__(self, y):
        """Quotient of x and y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __radd__(self, y):
        """Sum of y and x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rsub__(self, y):
        """Difference of y and x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rmul__(self, y):
        """Product of y and x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rfloordiv__(self, y):
        """Floored quotient of y and x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rmod__(self, y):
        """Remainder of y / x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rpow__(self, y):
        """x to the power y.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rdiv__(self, y):
        """Quotient of y and x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __rtruediv__(self, y):
        """Quotient of y and x.

        :type y: numbers.Number
        :rtype: complex
        """
        pass

    def __pos__(self):
        """x unchanged.

        :rtype: complex
        """
        pass

    def __neg__(self):
        """x negated.

        :rtype: complex
        """
        pass


if sys.version_info >= (3,):
    class bytes(object):
        """Bytes object."""

        def __init__(self, object=''):
            """Construct an immutable array of bytes.

            :type object: object
            """
            pass

        def __add__(self, y):
            """The concatenation of x and y.

            :type y: bytes
            :rtype: bytes
            """
            pass

        def __mul__(self, n):
            """n shallow copies of x concatenated.

            :type n: numbers.Integral
            :rtype: bytes
            """
            pass

        def __rmul__(self, n):
            """n shallow copies of x concatenated.

            :type n: numbers.Integral
            :rtype: bytes
            """
            pass

        def __getitem__(self, y):
            """y-th item of x, origin 0.

            :type y: numbers.Integral
            :rtype: int
            """
            pass

        def __iter__(self):
            """Iterator over bytes.

            :rtype: collections.Iterator[int]
            """
            pass

        def capitalize(self):
            """Return a copy of the string with its first character capitalized
            and the rest lowercased.

            :rtype: bytes
            """
            pass

        def center(self, width, fillchar=' '):
            """Return centered in a string of length width.

            :type width: numbers.Integral
            :type fillchar: bytes
            :rtype: bytes
            """
            pass

        def count(self, sub, start=None, end=None):
            """Return the number of non-overlapping occurrences of substring
            sub in the range [start, end].

            :type sub: bytes
            :type start: numbers.Integral | None
            :type end: numbers.Integral | None
            :rtype: int
            """
            pass

        def decode(self, encoding='utf-8', errors='strict'):
            """Return a string decoded from the given bytes.

            :type encoding: string
            :type errors: string
            :rtype: unicode
            """
            pass

        def endswith(self, suffix, start=None, end=None):
            """Return True if the string ends with the specified suffix,
            otherwise return False.

            :type suffix: bytes | tuple
            :type start: numbers.Integral | None
            :type end: numbers.Integral | None
            :rtype: bool
            """
            pass

        def find(self, sub, start=None, end=None):
            """Return the lowest index in the string where substring sub is
            found, such that sub is contained in the slice s[start:end].

            :type sub: bytes
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def index(self, sub, start=None, end=None):
            """Like find(), but raise ValueError when the substring is not
            found.

            :type sub: bytes
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def isalnum(self):
            """Return true if all characters in the string are alphanumeric and
            there is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def isalpha(self):
            """Return true if all characters in the string are alphabetic and there
            is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def isdigit(self):
            """Return true if all characters in the string are digits and there
            is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def islower(self):
            """Return true if all cased characters in the string are lowercase
            and there is at least one cased character, false otherwise.

            :rtype: bool
            """
            pass

        def isspace(self):
            """Return true if there are only whitespace characters in the
            string and there is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def istitle(self):
            """Return true if the string is a titlecased string and there is at
            least one character, for example uppercase characters may only
            follow uncased characters and lowercase characters only cased ones.

            :rtype: bool
            """
            pass

        def isupper(self):
            """Return true if all cased characters in the string are uppercase
            and there is at least one cased character, false otherwise.

            :rtype: bool
            """
            pass

        def join(self, iterable):
            """Return a string which is the concatenation of the strings in the
            iterable.

            :type iterable: collections.Iterable[bytes]
            :rtype: bytes
            """
            pass

        def ljust(self, width, fillchar=' '):
            """Return the string left justified in a string of length width.
            Padding is done using the specified fillchar (default is a space).

            :type width: numbers.Integral
            :type fillchar: bytes
            :rtype: bytes
            """
            pass

        def lower(self):
            """Return a copy of the string with all the cased characters
            converted to lowercase.

            :rtype: bytes
            """
            pass

        def lstrip(self, chars=None):
            """Return a copy of the string with leading characters removed.

            :type chars: bytes | None
            :rtype: bytes
            """
            pass

        def partition(self, sep):
            """Split the string at the first occurrence of sep, and return a
            3-tuple containing the part before the separator, the separator
            itself, and the part after the separator.

            :type sep: bytes
            :rtype: (bytes, bytes, bytes)
            """
            pass

        def replace(self, old, new, count=-1):
            """Return a copy of the string with all occurrences of substring
            old replaced by new.

            :type old: bytes
            :type new: bytes
            :type count: numbers.Integral
            :rtype: bytes
            """
            pass

        def rfind(self, sub, start=None, end=None):
            """Return the highest index in the string where substring sub is
            found, such that sub is contained within s[start:end].

            :type sub: bytes
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def rindex(self, sub, start=None, end=None):
            """Like rfind(), but raise ValueError when the substring is not
            found.

            :type sub: bytes
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def rjust(self, width, fillchar=' '):
            """Return the string right justified in a string of length width.
            Padding is done using the specified fillchar (default is a space).

            :type width: numbers.Integral
            :type fillchar: bytes
            :rtype: bytes
            """
            pass

        def rpartition(self, sep):
            """Split the string at the last occurrence of sep, and return a
            3-tuple containing the part before the separator, the separator
            itself, and the part after the separator.

            :type sep: bytes
            :rtype: (bytes, bytes, bytes)
            """
            pass

        def rsplit(self, sep=None, maxsplit=-1):
            """Return a list of the words in the string, using sep as the
            delimiter string.

            :type sep: bytes | None
            :type maxsplit: numbers.Integral
            :rtype: list[bytes]
            """
            pass

        def rstrip(self, chars=None):
            """Return a copy of the string with trailing characters removed.

            :type chars: bytes | None
            :rtype: bytes
            """
            pass

        def split(self, sep=None, maxsplit=-1):
            """Return a list of the words in the string, using sep as the
            delimiter string.

            :type sep: bytes | None
            :type maxsplit: numbers.Integral
            :rtype: list[bytes]
            """
            pass

        def splitlines(self, keepends):
            """Return a list of the lines in the string, breaking at line
            boundaries.

            :type keepends: bool
            :rtype: list[bytes]
            """
            pass

        def startswith(self, prefix, start=None, end=None):
            """Return True if string starts with the prefix, otherwise return
            False.

            :type prefix: bytes | tuple
            :type start: numbers.Integral | None
            :type end: numbers.Integral | None
            :rtype: bool
            """
            pass

        def strip(self, chars=None):
            """Return a copy of the string with the leading and trailing
            characters removed.

            :type chars: bytes | None
            :rtype: bytes
            """
            pass

        def swapcase(self):
            """Return a copy of the string with uppercase characters converted
            to lowercase and vice versa.

            :rtype: bytes
            """
            pass

        def title(self):
            """Return a titlecased version of the string where words start with
            an uppercase character and the remaining characters are lowercase.

            :rtype: bytes
            """
            pass

        def upper(self):
            """Return a copy of the string with all the cased characters
            converted to uppercase.

            :rtype: bytes
            """
            pass

        def zfill(self, width):
            """Return the numeric string left filled with zeros in a string of
            length width.

            :type width: numbers.Integral
            :rtype: bytes
            """
            pass


class str(object):
    """String object."""

    def __init__(self, object=''):
        """Construct an immutable string.

        :type object: object
        """
        pass

    def __add__(self, y):
        """The concatenation of x and y.

        :type y: string
        :rtype: string
        """
        pass

    def __mul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: string
        """
        pass

    def __mod__(self, y):
        """x % y.

        :rtype: string
        """
        pass

    def __rmul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: string
        """
        pass

    def __getitem__(self, y):
        """y-th item of x, origin 0.

        :type y: numbers.Integral
        :rtype: str
        """
        pass

    def __iter__(self):
        """Iterator over bytes.

        :rtype: collections.Iterator[str]
        """
        pass

    def capitalize(self):
        """Return a copy of the string with its first character capitalized
        and the rest lowercased.

        :rtype: str
        """
        pass

    def center(self, width, fillchar=' '):
        """Return centered in a string of length width.

        :type width: numbers.Integral
        :type fillchar: str
        :rtype: str
        """
        pass

    def count(self, sub, start=None, end=None):
        """Return the number of non-overlapping occurrences of substring
        sub in the range [start, end].

        :type sub: string
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: int
        """
        pass

    if sys.version_info < (3,):
        def decode(self, encoding='utf-8', errors='strict'):
            """Return a string decoded from the given bytes.

            :type encoding: string
            :type errors: string
            :rtype: unicode
            """
            pass

    def encode(self, encoding='utf-8', errors='strict'):
        """Return an encoded version of the string as a bytes object.

        :type encoding: string
        :type errors: string
        :rtype: bytes
        """
        pass

    def endswith(self, suffix, start=None, end=None):
        """Return True if the string ends with the specified suffix,
        otherwise return False.

        :type suffix: string | tuple
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: bool
        """
        pass

    def find(self, sub, start=None, end=None):
        """Return the lowest index in the string where substring sub is
        found, such that sub is contained in the slice s[start:end].

        :type sub: string
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        pass

    def index(self, sub, start=None, end=None):
        """Like find(), but raise ValueError when the substring is not
        found.

        :type sub: string
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        pass

    def isalnum(self):
        """Return true if all characters in the string are alphanumeric and
        there is at least one character, false otherwise.

        :rtype: bool
        """
        pass

    def isalpha(self):
        """Return true if all characters in the string are alphabetic and there
        is at least one character, false otherwise.

        :rtype: bool
        """
        pass

    def isdigit(self):
        """Return true if all characters in the string are digits and there
        is at least one character, false otherwise.

        :rtype: bool
        """
        pass

    def islower(self):
        """Return true if all cased characters in the string are lowercase
        and there is at least one cased character, false otherwise.

        :rtype: bool
        """
        pass

    def isspace(self):
        """Return true if there are only whitespace characters in the
        string and there is at least one character, false otherwise.

        :rtype: bool
        """
        pass

    def istitle(self):
        """Return true if the string is a titlecased string and there is at
        least one character, for example uppercase characters may only
        follow uncased characters and lowercase characters only cased ones.

        :rtype: bool
        """
        pass

    def isupper(self):
        """Return true if all cased characters in the string are uppercase
        and there is at least one cased character, false otherwise.

        :rtype: bool
        """
        pass

    def join(self, iterable):
        """Return a string which is the concatenation of the strings in the
        iterable.

        :type iterable: collections.Iterable[string]
        :rtype: string
        """
        pass

    def ljust(self, width, fillchar=' '):
        """Return the string left justified in a string of length width.
        Padding is done using the specified fillchar (default is a space).

        :type width: numbers.Integral
        :type fillchar: string
        :rtype: string
        """
        pass

    def lower(self):
        """Return a copy of the string with all the cased characters
        converted to lowercase.

        :rtype: str
        """
        pass

    def lstrip(self, chars=None):
        """Return a copy of the string with leading characters removed.

        :type chars: string | None
        :rtype: string
        """
        pass

    def partition(self, sep):
        """Split the string at the first occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself, and the part after the separator.

        :type sep: string
        :rtype: (str, str, str)
        """
        pass

    def replace(self, old, new, count=-1):
        """Return a copy of the string with all occurrences of substring
        old replaced by new.

        :type old: string
        :type new: string
        :type count: numbers.Integral
        :rtype: string
        """
        pass

    def rfind(self, sub, start=None, end=None):
        """Return the highest index in the string where substring sub is
        found, such that sub is contained within s[start:end].

        :type sub: string
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        pass

    def rindex(self, sub, start=None, end=None):
        """Like rfind(), but raise ValueError when the substring is not
        found.

        :type sub: string
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        pass

    def rjust(self, width, fillchar=' '):
        """Return the string right justified in a string of length width.
        Padding is done using the specified fillchar (default is a space).

        :type width: numbers.Integral
        :type fillchar: string
        :rtype: string
        """
        pass

    def rpartition(self, sep):
        """Split the string at the last occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself, and the part after the separator.

        :type sep: string
        :rtype: (str, str, str)
        """
        pass

    def rsplit(self, sep=None, maxsplit=-1):
        """Return a list of the words in the string, using sep as the
        delimiter string.

        :type sep: string | None
        :type maxsplit: numbers.Integral
        :rtype: list[str]
        """
        pass

    def rstrip(self, chars=None):
        """Return a copy of the string with trailing characters removed.

        :type chars: string | None
        :rtype: str
        """
        pass

    def split(self, sep=None, maxsplit=-1):
        """Return a list of the words in the string, using sep as the
        delimiter string.

        :type sep: string | None
        :type maxsplit: numbers.Integral
        :rtype: list[str]
        """
        pass

    def splitlines(self, keepends):
        """Return a list of the lines in the string, breaking at line
        boundaries.

        :type keepends: bool
        :rtype: list[str]
        """
        pass

    def startswith(self, prefix, start=None, end=None):
        """Return True if string starts with the prefix, otherwise return
        False.

        :type prefix: string | tuple
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: bool
        """
        pass

    def strip(self, chars=None):
        """Return a copy of the string with the leading and trailing
        characters removed.

        :type chars: string | None
        :rtype: str
        """
        pass

    def swapcase(self):
        """Return a copy of the string with uppercase characters converted
        to lowercase and vice versa.

        :rtype: str
        """
        pass

    def title(self):
        """Return a titlecased version of the string where words start with
        an uppercase character and the remaining characters are lowercase.

        :rtype: str
        """
        pass

    def upper(self):
        """Return a copy of the string with all the cased characters
        converted to uppercase.

        :rtype: str
        """
        pass

    def zfill(self, width):
        """Return the numeric string left filled with zeros in a string of
        length width.

        :type width: numbers.Integral
        :rtype: str
        """
        pass


if sys.version_info < (3,):
    class unicode(object):
        """Unicode string object."""

        def __init__(self, object=''):
            """Construct an immutable Unicode string.

            :type object: object
            """
            pass

        def __add__(self, y):
            """The concatenation of x and y.

            :type y: string
            :rtype: unicode
            """
            pass

        def __mul__(self, n):
            """n shallow copies of x concatenated.

            :type n: numbers.Integral
            :rtype: unicode
            """
            pass

        def __mod__(self, y):
            """x % y.

            :rtype: unicode
            """
            pass

        def __rmul__(self, n):
            """n shallow copies of x concatenated.

            :type n: numbers.Integral
            :rtype: unicode
            """
            pass

        def __getitem__(self, y):
            """y-th item of x, origin 0.

            :type y: numbers.Integral
            :rtype: unicode
            """
            pass

        def __iter__(self):
            """Iterator over bytes.

            :rtype: collections.Iterator[unicode]
            """
            pass

        def capitalize(self):
            """Return a copy of the string with its first character capitalized
            and the rest lowercased.

            :rtype: unicode
            """
            pass

        def center(self, width, fillchar=' '):
            """Return centered in a string of length width.

            :type width: numbers.Integral
            :type fillchar: string
            :rtype: unicode
            """
            pass

        def count(self, sub, start=None, end=None):
            """Return the number of non-overlapping occurrences of substring
            sub in the range [start, end].

            :type sub: string
            :type start: numbers.Integral | None
            :type end: numbers.Integral | None
            :rtype: int
            """
            pass

        def decode(self, encoding='utf-8', errors='strict'):
            """Return a string decoded from the given bytes.

            :type encoding: string
            :type errors: string
            :rtype: unicode
            """
            pass

        def encode(self, encoding='utf-8', errors='strict'):
            """Return an encoded version of the string as a bytes object.

            :type encoding: string
            :type errors: string
            :rtype: bytes
            """
            pass

        def endswith(self, suffix, start=None, end=None):
            """Return True if the string ends with the specified suffix,
            otherwise return False.

            :type suffix: string | tuple
            :type start: numbers.Integral | None
            :type end: numbers.Integral | None
            :rtype: bool
            """
            pass

        def find(self, sub, start=None, end=None):
            """Return the lowest index in the string where substring sub is
            found, such that sub is contained in the slice s[start:end].

            :type sub: string
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def index(self, sub, start=None, end=None):
            """Like find(), but raise ValueError when the substring is not
            found.

            :type sub: string
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def isalnum(self):
            """Return true if all characters in the string are alphanumeric and
            there is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def isalpha(self):
            """Return true if all characters in the string are alphabetic and there
            is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def isdigit(self):
            """Return true if all characters in the string are digits and there
            is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def islower(self):
            """Return true if all cased characters in the string are lowercase
            and there is at least one cased character, false otherwise.

            :rtype: bool
            """
            pass

        def isspace(self):
            """Return true if there are only whitespace characters in the
            string and there is at least one character, false otherwise.

            :rtype: bool
            """
            pass

        def istitle(self):
            """Return true if the string is a titlecased string and there is at
            least one character, for example uppercase characters may only
            follow uncased characters and lowercase characters only cased ones.

            :rtype: bool
            """
            pass

        def isupper(self):
            """Return true if all cased characters in the string are uppercase
            and there is at least one cased character, false otherwise.

            :rtype: bool
            """
            pass

        def join(self, iterable):
            """Return a string which is the concatenation of the strings in the
            iterable.

            :type iterable: collections.Iterable[string]
            :rtype: unicode
            """
            pass

        def ljust(self, width, fillchar=' '):
            """Return the string left justified in a string of length width.
            Padding is done using the specified fillchar (default is a space).

            :type width: numbers.Integral
            :type fillchar: string
            :rtype: unicode
            """
            pass

        def lower(self):
            """Return a copy of the string with all the cased characters
            converted to lowercase.

            :rtype: unicode
            """
            pass

        def lstrip(self, chars=None):
            """Return a copy of the string with leading characters removed.

            :type chars: string | None
            :rtype: unicode
            """
            pass

        def partition(self, sep):
            """Split the string at the first occurrence of sep, and return a
            3-tuple containing the part before the separator, the separator
            itself, and the part after the separator.

            :type sep: string
            :rtype: (unicode, unicode, unicode)
            """
            pass

        def replace(self, old, new, count=-1):
            """Return a copy of the string with all occurrences of substring
            old replaced by new.

            :type old: string
            :type new: string
            :type count: numbers.Integral
            :rtype: unicode
            """
            pass

        def rfind(self, sub, start=None, end=None):
            """Return the highest index in the string where substring sub is
            found, such that sub is contained within s[start:end].

            :type sub: string
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def rindex(self, sub, start=None, end=None):
            """Like rfind(), but raise ValueError when the substring is not
            found.

            :type sub: string
            :type start: numbers.Integral | None
            :type end: numbers.Integral | none
            :rtype: int
            """
            pass

        def rjust(self, width, fillchar=' '):
            """Return the string right justified in a string of length width.
            Padding is done using the specified fillchar (default is a space).

            :type width: numbers.Integral
            :type fillchar: string
            :rtype: unicode
            """
            pass

        def rpartition(self, sep):
            """Split the string at the last occurrence of sep, and return a
            3-tuple containing the part before the separator, the separator
            itself, and the part after the separator.

            :type sep: string
            :rtype: (unicode, unicode, unicode)
            """
            pass

        def rsplit(self, sep=None, maxsplit=-1):
            """Return a list of the words in the string, using sep as the
            delimiter string.

            :type sep: string | None
            :type maxsplit: numbers.Integral
            :rtype: list[unicode]
            """
            pass

        def rstrip(self, chars=None):
            """Return a copy of the string with trailing characters removed.

            :type chars: string | None
            :rtype: unicode
            """
            pass

        def split(self, sep=None, maxsplit=-1):
            """Return a list of the words in the string, using sep as the
            delimiter string.

            :type sep: string | None
            :type maxsplit: numbers.Integral
            :rtype: list[unicode]
            """
            pass

        def splitlines(self, keepends):
            """Return a list of the lines in the string, breaking at line
            boundaries.

            :type keepends: bool
            :rtype: list[unicode]
            """
            pass

        def startswith(self, prefix, start=None, end=None):
            """Return True if string starts with the prefix, otherwise return
            False.

            :type prefix: string | tuple
            :type start: numbers.Integral | None
            :type end: numbers.Integral | None
            :rtype: bool
            """
            pass

        def strip(self, chars=None):
            """Return a copy of the string with the leading and trailing
            characters removed.

            :type chars: string | None
            :rtype: unicode
            """
            pass

        def swapcase(self):
            """Return a copy of the string with uppercase characters converted
            to lowercase and vice versa.

            :rtype: unicode
            """
            pass

        def title(self):
            """Return a titlecased version of the string where words start with
            an uppercase character and the remaining characters are lowercase.

            :rtype: unicode
            """
            pass

        def upper(self):
            """Return a copy of the string with all the cased characters
            converted to uppercase.

            :rtype: unicode
            """
            pass

        def zfill(self, width):
            """Return the numeric string left filled with zeros in a string of
            length width.

            :type width: numbers.Integral
            :rtype: unicode
            """
            pass
