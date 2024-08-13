#!/usr/bin/python3
"""
Module solves the lockboxes problem

You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes: list[list]):
    """
    Returns true if all lockboxes can be opened

    Args:
    boxes (list): list of other boxes
    """
    set_of_keys = {0}
    boxes_status = [0] * len(boxes)
    current_keys = {0}

    while current_keys:
        new_keys = set()
        for key in current_keys:
            new_keys.update(unpack_box(boxes, key))
        current_keys = new_keys - set_of_keys
        set_of_keys.update(new_keys)

    for key in set_of_keys:
        boxes_status[key] = 1

    return all(boxes_status)


def unpack_box(boxes: list[list], idx: int):
    """
    Pushes elements from box array into set_of_keys

    Args:
    boxes (list[list]): box of boxes
    idx (int): index in boxes
    """
    return {key for key in boxes[idx] if key < len(boxes)}
