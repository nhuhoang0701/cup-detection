#!/usr/bin/env python3

#%%
import os
import sys
import helper
from mrcnn import utils, config, model

#%%
ROOT_DIR = os.path.abspath("./")
MASK_RCNN_DIR = os.path.join(ROOT_DIR, "Mask_RCNN")
sys.path.append(MASK_RCNN_DIR)


# %%
# define the test configuration
class TestConfig(config.Config):
    NAME = "test"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 80


# %%
# define the model
rcnn = model.MaskRCNN(mode="inference", model_dir="./", config=TestConfig())
rcnn.load_weights("mask_rcnn_coco.h5", by_name=True)

# %%
from matplotlib.image import imread
img = imread("elephant.jpg")

# %%
# make prediction
results = rcnn.detect([img], verbose=0)

# %%
helper.draw_box_around_object("elephant.jpg", results[0]["rois"])
