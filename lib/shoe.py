#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        self.is_worn = False

    def wear(self):
        self.is_worn = True

    def clean(self):
        self.is_worn = False
