# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class StationNotFound(Exception):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return self.value

class NetworkException(Exception):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value