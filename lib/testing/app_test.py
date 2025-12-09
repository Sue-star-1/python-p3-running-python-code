#!/usr/bin/env python3

from os import path
import runpy
import io
import sys
import subprocess

class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists("lib/app.py"))

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        result = subprocess.run([sys.executable, "lib/app.py"], capture_output=True, text=True)
        assert(result.stdout == "Hello World! Pass this test, please.\n")
