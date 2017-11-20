Installation
============

::

   pip3 install pelican
   pelican-themes --install ~/pelican-themes/Flex/
   pip3 install ghp-import


Generate Content
================

::

   pelican content -s publishconf.py


Viewing local changes
=====================

::

   pelican content
   cd output
   python -m pelican.server


Committing local changes
========================

::

   git push origin configuration

Publish to GitHub Pages
=======================

::

   pelican content -o output -s pelicanconf.py
   ghp-import output
   git push git@github.com:mariatta/mariatta.github.io.git gh-pages:master --force
   git push origin configuration