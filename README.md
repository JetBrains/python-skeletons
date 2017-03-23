Python Skeletons
================


Deprecated: use PEP 484 and Typeshed instead
--------------------------------------------

The python-skeletons repository is deprecated. There is now a standard for type
hints in Python:

* [PEP 484: Type Hints](https://www.python.org/dev/peps/pep-0484/) for syntax
  and semantics of type hints
* [The Typeshed repository](https://github.com/python/typeshed/) for the common
  collection of Python stubs

PyCharm 2017.1 and newer bundles the whole Typeshed repo, but only a few modules
from it are actually enabled in PyCharm (including `builtins`, `typing`, `six`,
and several others).

If you want to add any other module from Typeshed to your project, you can put
it inside your project's root or into the source folders of your project.

Feel free to contribute your changes to the [Typeshed
repo](https://github.com/python/typeshed/). Make sure you've read the
contributing notes. More modules from Typeshed will be enabled in the next
versions of PyCharm.


See Also
--------

* [Old docs about python-skeletons](README-obsolete.md) (Deprecated!)

