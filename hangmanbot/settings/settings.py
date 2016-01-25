DEBUG = False

if DEBUG:
    from .local import *
else:
    from .private import *
