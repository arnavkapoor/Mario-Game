#!/bin/bash

for f in *.py; 
    do echo "$f";
    pylint3 --extension-pkg-whitelist=numpy "$f" | tail -2
    done