# objective: I want to list all the disks in a server
# include the size of the disks
# and the disk name

import os
import collections
import ctypes
import sys

import locale
locale.setlocale(locale.LC_ALL, '')  # set locale to default to get thousands separators

PULARGE_INTEGER = ctypes.POINTER(ctypes.c_ulonglong)  # Pointer to large unsigned integer
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
kernel32.GetDiskFreeSpaceExW.argtypes = (ctypes.c_wchar_p,) + (PULARGE_INTEGER,) * 3

class UsageTuple(collections.namedtuple('UsageTuple', 'total, used, free')):
    def __str__(self):
        # Add thousands separator to numbers displayed
        return self.__class__.__name__ + '(total={:n}, used={:n}, free={:n})'.format(*self)

for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
       if os.path.exists(f'{drive_letter}:'):
           print(f'{drive_letter}:')
       else:
           pass

def disk_usage(path):
    if sys.version_info < (3,):  # Python 2?
        saved_conversion_mode = ctypes.set_conversion_mode('mbcs', 'strict')
    else:
        try:
            path = os.fsdecode(path)  # allows str or bytes (or os.PathLike in Python 3.6+)
        except AttributeError:  # fsdecode() not added until Python 3.2
            pass

    # Define variables to receive results when passed as "by reference" arguments
    _, total, free = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()

    success = kernel32.GetDiskFreeSpaceExW(
                            path, ctypes.byref(_), ctypes.byref(total), ctypes.byref(free))
    if not success:
        error_code = ctypes.get_last_error()

    if sys.version_info < (3,):  # Python 2?
        ctypes.set_conversion_mode(*saved_conversion_mode)  # restore conversion mode

    if not success:
        windows_error_message = ctypes.FormatError(error_code)
        raise ctypes.WinError(error_code, '{} {!r}'.format(windows_error_message, path))

    used = total.value - free.value

    return UsageTuple(total.value, used, free.value)



if __name__ == '__main__':
    print(disk_usage('C:/'))

