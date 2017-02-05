#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 5 de fev de 2017

@author: Clayton Bonelli
'''

import os
import importlib.util

__mapping = {}

def register(selector):
    def real_register(cls):
        __mapping[selector] = cls
        return cls
    return real_register
    
def new(selector, *args, **kwargs):
    
    def get_class(selector):
        return __mapping.get(selector)
    
    def new_instance(klass):
        return klass(*args, **kwargs)
    
    def is_in_the_list(filename, names_list):
        for name in names_list:
            if filename.startswith(name):
                return True
        return False    
    
    def can_load(filename, exclude_names=None, include_names=None):
        if __file__ == filename:
            return False
        
        if not os.path.splitext(filename)[1] in ('.py'):
            return False
        
        basename = os.path.basename(filename)
        if exclude_names:
            if is_in_the_list(basename, exclude_names):
                return False
            
        if include_names:
            if not is_in_the_list(basename, include_names):
                return False    
                
        with open(filename) as f:
            lines = f.readlines()
            result = any("@dinjector.register" in line for line in lines) or any("@register" in line for line in lines)
            return result
                    
        return False
    
    def get_modules(path):
        exclude_names = ["tests", "__init__"]
        modules = []
        for root, _, files in os.walk(path):
            names = [os.path.join(root, filename) for filename in files if can_load(os.path.join(root, filename), exclude_names)]
            modules += names
        return modules
    
    def get_base_dir():
        return os.path.split(os.path.split(__file__)[0])[0]

    def load_modules():
        path = get_base_dir() 
        modules = get_modules(path)
    
        for module in modules:
            name = os.path.splitext(os.path.basename(module))[0]
            spec = importlib.util.spec_from_file_location(name, module)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        return None    
    
    return new_instance(get_class(selector) or get_class(load_modules() or selector))
