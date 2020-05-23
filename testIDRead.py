# -*- coding: UTF-8 -*-

import cv2
import numpy as np


def get_WH(w, h):
    return int(w * 0.63), int(h * 0.8)


def get_image(image):
    h, w = image.shape
    w2, h2 = get_WH(w, h)
    for x in range(w2, w):
        for y in range(1, h2):
            image[y - 1, x - 1] = 0
    return image


def get_ranges(array, min_s=0, color_size=255, min_col=None):
    rs = []
    ranges = []
    start = None
    end = None
    for i, s in enumerate(array):
        s = s / color_size
        if (s > min_s):
            if (start is None):
                start = i
            elif (start is not None):
                end = i
        if (s <= min_s and end is not None and start is not None):
            if (end is not None and start is not None
                    and min_col is not None and (end - start) < min_col):
                continue
            rs.append((start, end - 1))
            ranges.append(end - start)
            start = None
            end = None
        if (i == len(array) - 1 and start is not None and end is not None):
            rs.append((start, len(array) - 1))

    return rs, ranges


def get_show_image(img_range, image):
    color = (255, 0, 0)
    for i, r in enumerate(img_range):
        x, y, w, h = r
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(image, pt1, pt2, color)
    return image


def get_cols(image, l, cols, col_ranges):
    (min_y, max_y) = l
    cols2 = []
    if (col_ranges is None or len(col_ranges) < 1):
        return cols2
    a = sum(col_ranges) / len(col_ranges)
    deviation = int(a * 0.5)
    for i, r in enumerate(col_ranges):
        (min_x, max_x) = cols[i]
        if ((r - a) > deviation):
            line_img = image[min_y:max_y, min_x:max_x]
            line_img_sum = np.sum(line_img, axis=0)
            cols_new, col_ranges_new = get_ranges(line_img_sum, min_s=2, min_col=a - deviation)
            for j, c in enumerate(cols_new):
                cols2.append((min_x + cols_new[j][0], min_x + cols_new[j][1]))
        else:
            cols2.append(cols[i])
    return cols2


def get_img_range(image, percent=None):
    line_sum = np.sum(image, axis=1)
    # print(line_sum)
    lines, ranges = get_ranges(line_sum)
    img_range = []
    for i, l in enumerate(lines):
        (min_y, max_y) = l
        line_img = image[min_y:max_y, :]
        line_img_sum = np.sum(line_img, axis=0)
        cols, col_ranges = get_ranges(line_img_sum)
        cols = get_cols(image, l, cols, col_ranges)
        cols = get_cols_by_min(cols, col_ranges, percent)
        for j, c in enumerate(cols):
            (min_x, max_x) = c
            img_range.append((min_x, min_y, (max_x - min_x), (max_y - min_y)))
    return img_range


def get_ranges_by_col(img_range, interval_s=0):
    if (interval_s == 0):
        return range
    old_x = None
    old_y = None
    range2 = []
    for (i, r) in enumerate(img_range):
        x, y, w, h = r
        if (i == len(img_range) - 1):
            if (old_x is not None and old_y is not None):
                range2.append((old_x, old_y, x - old_x + w, h))
                old_x = None
                old_y = None
            else:
                range2.append((x, y, w, h))
        else:
            if (old_x is not None and old_y is not None):
                range2.append((old_x, old_y, x - old_x + w, h))
                old_x = None
                old_y = None
                continue
            x2, y2, w2, h2 = img_range[i + 1]
            interval = x2 - x
            if (interval > 0 and interval < interval_s):
                old_x = x
                old_y = y
            else:
                range2.append((x, y, w, h))
                old_x = None
                old_y = None
    return range2


def get_cols_by_min(cols, col_ranges, percent=None):
    if (percent is None):
        return cols
    cols2 = []
    if (col_ranges is None or len(col_ranges) < 1):
        return cols2
    a = sum(col_ranges) / len(col_ranges)
    deviation = int(a * percent)
    for i, r in enumerate(col_ranges):
        (min_x, max_x) = cols[i]
        if ((a - r) > deviation):
            if (i < len(col_ranges) - 1):
                cols2.append((min_x, cols[i + 1][1]))
                i += 1
        else:
            cols2.append(cols[i])
    return cols2


path = "id_card.jpg"
image_color = cv2.imread(path)
new_shape = (image_color.shape[1] * 2, image_color.shape[0] * 2)
image_color = cv2.resize(image_color, new_shape)
lower = np.array((0, 0, 0), dtype="uint8")
upper = np.array((100, 100, 100), dtype="uint8")
image = cv2.inRange(image_color, lower, upper)
cv2.imshow('image2',image)
image = get_image(image)

img_range = get_img_range(image)
img_range = get_ranges_by_col(img_range, interval_s=15)
image = get_show_image(img_range, image_color)

cv2.imshow('image', image)
cv2.waitKey(0)
