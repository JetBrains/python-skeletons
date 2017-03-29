"""Skeleton for 'pywintypes' module.

Project: pywin32 214 <http://sourceforge.net/projects/pywin32/>
Skeleton by: Simon Zack <simonzack@gmail.com>
"""


def ACL(*args, **kwargs):
    pass


def ACLType(*args, **kwargs):
    pass


def CreateGuid(*args, **kwargs):
    pass


def DEVMODEAType(*args, **kwargs):
    pass


def DEVMODEType(*args, **kwargs):
    pass


def DEVMODEWType(*args, **kwargs):
    pass


def DosDateTimeToTime(*args, **kwargs):
    pass


def FALSE(*args, **kwargs):
    pass


def HANDLE(*args, **kwargs):
    pass


def HANDLEType(*args, **kwargs):
    pass


def HKEY(*args, **kwargs):
    pass


def IID(*args, **kwargs):
    pass


def IIDType(*args, **kwargs):
    pass


def IsTextUnicode(*args, **kwargs):
    pass


def OVERLAPPED(*args, **kwargs):
    pass


def OVERLAPPEDType(*args, **kwargs):
    pass


def SECURITY_ATTRIBUTES(*args, **kwargs):
    pass


def SECURITY_ATTRIBUTESType(*args, **kwargs):
    pass


def SECURITY_DESCRIPTOR(*args, **kwargs):
    pass


def SECURITY_DESCRIPTORType(*args, **kwargs):
    pass


def SID(*args, **kwargs):
    pass


def SIDType(*args, **kwargs):
    pass


def TRUE(*args, **kwargs):
    pass


def Time(*args, **kwargs):
    pass


def TimeType(*args, **kwargs):
    pass


def Unicode(*args, **kwargs):
    pass


def UnicodeFromRaw(*args, **kwargs):
    pass


def UnicodeType(*args, **kwargs):
    pass


def WAVEFORMATEX(*args, **kwargs):
    pass


def WAVEFORMATEXType(*args, **kwargs):
    pass


def WAVE_FORMAT_PCM(*args, **kwargs):
    pass


class error(Exception):
    def __init__(self, *args):
        nargs = len(args)
        if nargs > 0:
            self.winerror = args[0]
        else:
            self.winerror = None
        if nargs > 1:
            self.funcname = args[1]
        else:
            self.funcname = None
        if nargs > 2:
            self.strerror = args[2]
        else:
            self.strerror = None
        Exception.__init__(self, *args)


class com_error(Exception):
    def __init__(self, *args):
        nargs = len(args)
        if nargs > 0:
            self.hresult = args[0]
        else:
            self.hresult = None
        if nargs > 1:
            self.strerror = args[1]
        else:
            self.strerror = None
        if nargs > 2:
            self.excepinfo = args[2]
        else:
            self.excepinfo = None
        if nargs > 3:
            self.argerror = args[3]
        else: self.argerror = None
        Exception.__init__(self, *args)
