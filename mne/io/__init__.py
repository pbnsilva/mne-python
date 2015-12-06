"""FIF module for IO with .fif files"""

# Authors: Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#          Matti Hamalainen <msh@nmr.mgh.harvard.edu>
#
# License: BSD (3-clause)

from .open import fiff_open, show_fiff, _fiff_get_fid
from .meas_info import (read_fiducials, write_fiducials, read_info, write_info,
                        _empty_info, _merge_info, Info)

from .proj import make_eeg_average_ref_proj, Projection
from .tag import _loc_to_coil_trans, _coil_trans_to_loc, _loc_to_eeg_loc
from .base import _BaseRaw

from . import array
from . import base
from . import brainvision
from . import bti
from . import ctf
from . import constants
from . import edf
from . import egi
from . import fiff
from . import kit
from . import nicolet
from . import eeglab
from . import pick

from .array import RawArray
from .brainvision import read_raw_brainvision
from .bti import read_raw_bti
from .ctf import read_raw_ctf
from .edf import read_raw_edf
from .egi import read_raw_egi
from .kit import read_raw_kit, read_epochs_kit
from .fiff import read_raw_fif
from .nicolet import read_raw_nicolet
from .eeglab import read_raw_set

# for backward compatibility
from .fiff import RawFIF
from .fiff import RawFIF as Raw
from .base import concatenate_raws
from .reference import (set_eeg_reference, set_bipolar_reference,
                        add_reference_channels)
