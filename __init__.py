#!/usr/bin/env python
# This file is Python 2 compliant.#compliant:适用

import sys

if sys.version_info[0] == 3:
    #from .extractor import Extractor, VideoExtractor
    #from .util import log

    from .__main__ import *

    #from .common import *
    #from .version import *
    #from .cli_wrapper import *  #cli:命令语言解译器 (command language interpreter)  wrapper:封装器
    #from .extractor import * #extractor:抽取器
else:
    # Don't import anything.
    pass
