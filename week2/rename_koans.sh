#!/bin/bash

echo "mv $(ls python_koans-*) python_koans-$(md5 python_koans-* | awk -F " = " '{ print $2 }' | cut -c 1-8).zip"
