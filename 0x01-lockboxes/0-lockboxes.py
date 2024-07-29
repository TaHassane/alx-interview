#!/usr/bin/python3
"""
Determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    boxes can be unlocked?
    """
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
