# pylint: disable=W0401,W0611,no-absolute-import,invalid-name,import-error,bare-except,broad-except,wrong-import-order,ungrouped-imports,wrong-import-position
"""check unexistant names imported are reported"""
from __future__ import print_function
from .no_self_use.bla import lala1  # [no-name-in-module]
from .no_self_use import lala  # [no-name-in-module]
from .no_self_use import Super
import os
from re import findiiter, compiile  # [no-name-in-module,no-name-in-module]
from rie import *
import re
import sys
from xml.etree import ElementTree

import collections.tutu  # [no-name-in-module]
from collections import toto  # [no-name-in-module]
toto.yo()

ElementTree.nonexistant_function()  # [no-member]
ElementTree.another.nonexistant.function()  # [no-member]

print(sys.stdout, 'hello world')
print(sys.stdoout, 'bye bye world')  # [no-member]

re.finditer('*', 'yo')

'SOMEVAR' in os.environ  # [pointless-statement]

try:
    from collections import something
except ImportError:
    something = None

try:
    from collections import anything  # [no-name-in-module]
except ValueError:
    anything = None

try:
    import collections.missing
except ImportError:
    pass

try:
    import collections.indeed_missing  # [no-name-in-module]
except ValueError:
    pass

try:
    import collections.emit  # [no-name-in-module]
except Exception:
    pass

try:
    import collections.emit1
except ImportError:
    pass

try:
    if something:
        import collections.emit2  # [no-name-in-module]
except Exception:
    pass
