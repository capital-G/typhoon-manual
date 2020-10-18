#!/bin/sh

pip3 install -r requirements.txt

python3 image_generator.py

pandoc -i README.md --variable documentclass=scrreprt -f markdown-implicit_figures  -o README.pdf
