# Table of Contents
1. [Introduction](README.md#introduction)
2. [Repo directory structure](README.md#repo-directory-structure)
3. [Code Details](README.md#code-details)
4. [Test Suite](README.md#test-suite)
5. [Environment](README.md#environment)


# Introduction
This code was written in response to the coding challenge organized by Insight DataScience. Additional details about the challenge are available at https://github.com/InsightDataScience/donation-analytics/blob/master/README.md

# Repo Directory Structure
The layout of the code and directory follows the suggested layout at https://github.com/InsightDataScience/donation-analytics/blob/master/README.md#repo-directory-structure

# Code details
The code is split in two files. utils.py contains utility functions and constant variables. main.py contains functions to read and process the input files. The program prints helpful information message to show progress.

The program takes three labelled parameters: --input, --percentile and --output
The default values are as follows:

--input = ./input/itcont.txt
--percentile = ./input/percentile.txt
--output = ./output/repeat_donors.txt

python ./src/main.py --input="./input/itcont14.txt" --percentile="./input/percentile.txt" --output="./output/repeat_donors.txt"

# Test Suite
There are five test cases in the test suite folder.

## Test 1
Input is the sample data provided as part of the challenge. The largest year is the current calendar year (2018).

## Test 2
The data range in the input itcont.txt file is limited to one year (2017-2017). There is no data for prior years.

## Test 3
Invalid ( < 0 ) percentile value

## Test 4
Invalid (> 100) percentile value

## Test 5
Run the test case against valid sample data. The largest year is the NOT the current calendar year (2016).

# Environment
The code is written in python 3 and run time environment was created using conda utility.
Following packages are part of my environment. You may not need to install all of these packages.

name: idp
channels:
- intel
- defaults
dependencies:
- boto=2.48.0=py36hdbc59ac_1
- bz2file=0.98=py36_0
- cairo=1.14.10=h913ea44_6
- ffmpeg=3.4=h766ddd1_0
- fontconfig=2.12.4=hffb9db1_2
- gensim=3.1.0=py36h33de7db_0
- gettext=0.19.8.1=h15daf44_3
- glib=2.53.6=h33f6a65_2
- graphite2=1.3.10=h337f25e_1
- harfbuzz=1.7.4=h08e020e_0
- icu=58.2=h4b95b61_1
- jasper=1.900.1=h1f36771_4
- jpeg=9b=he5867d9_2
- libcxx=4.0.1=h579ed51_0
- libcxxabi=4.0.1=hebd6815_0
- libffi=3.2.1=h475c297_4
- libiconv=1.15=hdd342a3_7
- libopus=1.2.1=h169cedb_0
- libprotobuf=3.4.1=h326466f_0
- libtiff=4.0.9=h0dac147_0
- libvpx=1.6.1=h057a404_0
- libxml2=2.9.4=hf05c021_6
- nltk=3.2.5=py36h1190bce_0
- olefile=0.45.1=py36_0
- opencv=3.3.1=py36h60a5f38_1
- pcre=8.41=hfb6ab37_1
- pillow=4.2.1=py36h0263179_0
- pixman=0.34.0=hca0a616_3
- smart_open=1.5.3=py36_0
- appnope=0.1.0=py36_intel_5
- asn1crypto=0.22.0=py36_0
- backports=1.0=py36_intel_6
- bleach=2.0.0=py36_intel_0
- bzip2=1.0.6=intel_13
- certifi=2017.7.27.1=py36_intel_0
- cffi=1.10.0=py36_intel_0
- chardet=3.0.4=py36_intel_0
- cryptography=2.0.3=py36_intel_0
- cycler=0.10.0=py36_intel_5
- cython=0.27.1=py36_intel_0
- daal=2018.0.1.20171012=1
- decorator=4.1.2=py36_intel_0
- entrypoints=0.2.3=py36_intel_0
- freetype=2.8=intel_0
- get_terminal_size=1.0.0=py36_intel_5
- hdf5=1.10.1=intel_0
- html5lib=0.999999999=py36_intel_0
- icc_rt=2018.0.0=intel_0
- idna=2.6=py36_intel_0
- intelpython=2018.0.0=3
- intelpython3_core=2018.0.1=1
- intelpython3_full=2018.0.1=0
- ipykernel=4.6.1=py36_intel_0
- ipython=6.1.0=py36_intel_0
- ipython_genutils=0.2.0=py36_intel_0
- ipywidgets=7.0.0=py36_intel_0
- jinja2=2.9.6=py36_intel_0
- jsonschema=2.6.0=py36_intel_0
- jupyter=1.0.0=py36_intel_5
- jupyter_client=5.1.0=py36_intel_0
- jupyter_console=5.1.0=py36_intel_0
- jupyter_core=4.3.0=py36_intel_1
- libpng=1.6.32=intel_0
- llvmlite=0.20.0=py36_intel_0
- markupsafe=1.0=py36_intel_0
- matplotlib=2.0.2=np113py36_intel_1
- mistune=0.7.4=py36_intel_1
- mkl=2018.0.1=intel_5
- mkl_fft=1.0.0=np113py36_intel_15
- mkl_random=1.0.0=np113py36_intel_6
- mpmath=0.19=py36_intel_5
- nbconvert=5.2.1=py36_intel_0
- nbformat=4.4.0=py36_intel_0
- nose=1.3.7=py36_intel_16
- notebook=5.0.0=py36_intel_0
- numba=0.35.0=py36_intel_0
- numexpr=2.6.2=np113py36_intel_5
- numpy=1.13.3=py36_intel_6
- openmp=2018.0.0=intel_8
- openssl=1.0.2l=intel_0
- pandas=0.20.3=np113py36_intel_4
- pandocfilters=1.4.1=py36_intel_0
- path.py=10.3.1=py36_intel_0
- pexpect=4.2.1=py36_intel_1
- pickleshare=0.7.4=py36_intel_1
- pip=9.0.1=py36_intel_0
- prompt_toolkit=1.0.15=py36_intel_0
- ptyprocess=0.5.2=py36_intel_0
- pycparser=2.18=py36_intel_0
- pydaal=2018.0.1.20171012=np113py36_intel_0
- pygments=2.2.0=py36_intel_1
- pyopenssl=17.2.0=py36_intel_0
- pyparsing=2.2.0=py36_intel_0
- pysocks=1.6.7=py36_intel_0
- pytables=3.4.2=np113py36_intel_2
- python=3.6.3=intel_3
- python-dateutil=2.6.0=py36_intel_3
- pytz=2017.2=py36_intel_3
- pyyaml=3.12=py36_intel_3
- pyzmq=16.0.2=py36_intel_4
- requests=2.18.4=py36_intel_0
- scikit-learn=0.19.0=np113py36_intel_6
- scipy=0.19.1=np113py36_intel_23
- setuptools=27.2.0=py36_intel_0
- simplegeneric=0.8.1=py36_intel_5
- six=1.10.0=py36_intel_8
- sqlite=3.20.1=intel_0
- sympy=1.1.1=py36_intel_0
- tbb=2018.0.1=py36_intel_3
- tcl=8.6.4=intel_17
- terminado=0.6=py36_intel_6
- testpath=0.3.1=py36_intel_0
- tk=8.6.4=intel_26
- tornado=4.5.2=py36_intel_0
- traitlets=4.3.2=py36_intel_1
- urllib3=1.22=py36_intel_0
- wcwidth=0.1.7=py36_intel_5
- webencodings=0.5.1=py36_0
- wheel=0.29.0=py36_intel_5
- widgetsnbextension=3.0.2=py36_0
- xz=5.2.3=intel_0
- yaml=0.1.7=intel_0
- zlib=1.2.11=intel_3
- pip:
  - backports.shutil-get-terminal-size==1.0.0
  - ipython-genutils==0.2.0
  - jupyter-client==5.1.0
  - jupyter-console==5.1.0
  - jupyter-core==4.3.0
  - mkl-fft==1.0.0
  - mkl-random==1.0.0
  - prompt-toolkit==1.0.15
  - smart-open==1.5.3
  - tables==3.4.2
prefix: /Users/ashishkumar/anaconda3/envs/idp
