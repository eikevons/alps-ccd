"""\
:mod:`ccd.io` CCD Frame I/O
---------------------------

This package contains tools to read e.g. :file:`*.spe` files. Important
helper functions to load single and multiple files are:

* :func:`~ccd.io.tools.get_frame`
* :func:`~ccd.io.tools.frame_iter`

CCD frames are stored as :class:`~ccd.io.frame.Frame` objects. Multi-frame
files are stored as :class:`~ccd.io.frameset.FrameSet`. Meta-information of
such :class:`~ccd.io.frame.Frame`s or :class:`~ccd.io.frameset.FrameSet`s
are stored in :class:`~ccd.io.info.FrameInfo` and
:class:`~ccd.io.info.FrameSetInfo` containers.

.. automodule:: ccd.io.frame
.. automodule:: ccd.io.tools
.. automodule:: ccd.io.frameset
.. automodule:: ccd.io.info
.. automodule:: ccd.io.spe
"""
from .frame import Frame
from .frameset import FrameSet

from .tools import frame_iter, get_frame
