<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/gen_stm8_logo.png" width="25%">

# STM8 project skeleton generator

**gen_stm8** is toolset for generation STM8 project skeleton for
developmet of embedded applications.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_stm8 python checker](https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python_checker.yml) [![gen_stm8 package checker](https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_stm8.svg)](https://github.com/vroncevic/gen_stm8/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_stm8.svg)](https://github.com/vroncevic/gen_stm8/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/debtux.png)

[![gen_stm8 python3 build](https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_stm8/)**.

You can install by using pip

```bash
#python3
pip3 install gen_stm8
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_stm8/releases/)** download and extract release archive.

To install **gen_stm8** type the following

```bash
tar xvzf gen_stm8-x.y.z.tar.gz
cd gen_stm8-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_stm8-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_stm8_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_stm8_run.py /usr/local/bin/gen_stm8_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_stm8/releases)** download and extract release archive.

To install **gen_stm8** locate and run setup.py with arguments

```bash
tar xvzf gen_stm8-x.y.z.tar.gz
cd gen_stm8-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_stm8** requires next modules and libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Tool structure

**gen_stm8** is based on OOP.

Generator structure

```bash
gen_stm8/
    ├── conf/
    │   ├── gen_stm8.logo
    │   ├── gen_stm8.cfg
    │   ├── gen_stm8_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── Makefile.template
    │       ├── module.template
    │       └── stm8s.template
    ├── __init__.py
    ├── log/
    │   └── gen_stm8.log
    ├── pro/
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        ├── factory_reset.sh
        └── gen_stm8_run.py

    6 directories, 14 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen-stm8/badge/?version=latest)](https://gen-stm8.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

- [gen_stm8.readthedocs.io](https://gen-stm8.readthedocs.io/)
- [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 - 2024 by [vroncevic.github.io/gen_stm8](https://vroncevic.github.io/gen_stm8/)

**gen_stm8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)