#!/usr/bin/venv python3

#%%
import os
import sys

#%%
ROOT_DIR = os.path.abspath("./")
MASK_RCNN_DIR = os.path.join(ROOT_DIR, "Mask_RCNN")
sys.path.append(MASK_RCNN_DIR)


#%%

# define the test configuration
from mrcnn import utils

# %%
