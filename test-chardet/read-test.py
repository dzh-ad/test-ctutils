# from io
from pathlib import Path

import numpy as np
import zarr

from numcodecs import Blosc
from numpy.typing import NDArray
from skimage.util import img_as_ubyte

# from ctutils
import sys
import os
import io
import struct
import locale

import compoundfiles
import numpy as np
from PIL import Image

from .configparser import ConfigParser


# own function!
def _load_vgi(file_path: Path) -> NDArray:
    """Load a VGI file from disk.

    Parameters
    ----------
    file_path : Path
        Path to the VGI file.

    Returns
    -------
    NDArray[np.uint8]
        The array.
    """


    return array