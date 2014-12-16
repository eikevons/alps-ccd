alps-ccd: The ALPS CCD toolbox
==============================

This package contains tools to read and analyze CCD frames. It has been tested
on Python 2.7 and Python 3.4+.

Required Python packages are:
  - numpy
  - scipy
  - matplotlib


Detailed installation on Ubuntu
-------------------------------

This installation instructions describe how to create a new virtualenv and
install the package into this.

1. Install the following Ubuntu packages:

   - python-numpy
   - python-scipy
   - python-matplotlib
   - ipython
   - python-virtualenv
   - git

2. Prepare install directory:

   We will download and install my Python code into a "special" directory (a
   virtual environment) in order to not pollute your hard disk.

   a) Create "virtualenv" named ALPS (or any other name and anywhere you like) with::

          virtualenv --system-site-packages --clear ALPS

      and activate it for the current shell session::

            source ALPS/bin/activate

   b) Prepare download directory::

          mkdir ALPS/src

      and go there::

          cd ALPS/src

3. Download and install my packages from GitHub

   a) Download::

          git clone https://github.com/eikevons/alps-ccd.git
          git clone https://github.com/eikevons/plttools.git


   b) Install the packages in the "ALPS" virtualenv (from inside `.../ALPS/src/`)::

          pip install -e alps-ccd
          pip install -e plttools

      .. note:: With the `-e` switch, the packages are installed
         *editable* which means that changes to the source code are
         automatically available in the installed version.

         Alternatively, one can create links to the package directories
         by hand::

             cd ../lib/python2.7/site-packages
             ln -s ../../../src/alps-ccd/ccd/ .
             ln -s ../../../src/plttools/plttools/ .

4. Test that the install worked.

   a) Start IPython and try to load the modules::

          ipython
          In [1]: import ccd, ccd.io, ccd.analysis, ccd.analysis.hotpixels
          In [2]: import plttools
   
   b) If you start a new shell, be sure that you activate the virtualenv
      with ``source .../ALPS/bin/activate`` before starting python.
