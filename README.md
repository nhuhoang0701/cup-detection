# cup-detection

This is a part of the course SY32 (Image Processing and Object Detection). The goal of the project is to localize and detect the plastic cup in images that are taken and labelled by all of students studying the course. The train and test dataset could be found [here](https://gitlab.utc.fr/sy32/sy32-ecocup-p22/dataset/-/tree/main/). There are 2 approaches for this problem:
- Mask-RCNN
- YOLO

## Mask-RCNN
### Install Mask-RCNN library
After activating virtual environment using `pipenv`, clone the Mask-RCNN library created by *matterport*:
```
git clone https://github.com/matterport/Mask_RCNN.git
```

Then, install the library:
```
cd Mask_RCNN
sudo python setup.py install
```
Finally, check if the library is installed:
```
pip show mask-rcnn
```
