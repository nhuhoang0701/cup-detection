#!/usr/bin/env python3

# draw an image with detected objects
import matplotlib.pyplot as plt


def draw_box_around_object(filename, boxes_list):
    """Draw image with boxes around the detected object

    Args:
        filename (str): path of image
        boxes_list (tuple): coordinations of the box
    """
    # load the image
    data = plt.imread(filename)
    # plot the image
    plt.imshow(data)
    # get the context for drawing boxes
    ax = plt.gca()
    # plot each box
    for box in boxes_list:
        # get coordinates
        y1, x1, y2, x2 = box
        # calculate width and height of the box
        width, height = x2 - x1, y2 - y1
        # create the shape
        rect = plt.Rectangle((x1, y1), width, height, fill=False, color="red")
        # draw the box
        ax.add_patch(rect)
    # show the plot
    plt.show()
