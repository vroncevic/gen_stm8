# STM8 project skeleton generator

**gen_stm8** is toolset for generation STM8 project skeleton for
developmet of embedded applications.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_stm8/workflows/Python%20package%20gen_stm8/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_stm8.svg)](https://github.com/vroncevic/gen_stm8/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_stm8.svg)](https://github.com/vroncevic/gen_stm8/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Generation flow](#generation-flow)
- [Tool structure](#library-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_stm8/workflows/Install%20Python2%20Package%20gen_stm8/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_stm8/workflows/Install%20Python3%20Package%20gen_stm8/badge.svg?branch=master)

Navigate to release **[page](https://github.com/vroncevic/gen_stm8/releases/)** download and extract release archive.

To install **gen_stm8** type the following:

```
tar xvzf gen_stm8-x.y.z.tar.gz
cd gen_stm8-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/gen_stm8
copying gen_stm8/__init__.py -> build/lib.linux-x86_64-2.7/gen_stm8
creating build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro
copying gen_stm8/stm8_pro/stm8_setup.py -> build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro
copying gen_stm8/stm8_pro/__init__.py -> build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro
copying gen_stm8/stm8_pro/write_template.py -> build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro
copying gen_stm8/stm8_pro/read_template.py -> build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro
creating /usr/local/lib/python2.7/dist-packages/gen_stm8
copying build/lib.linux-x86_64-2.7/gen_stm8/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_stm8
creating /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro
copying build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro/stm8_setup.py -> /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro
copying build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro
copying build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro/write_template.py -> /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro
copying build/lib.linux-x86_64-2.7/gen_stm8/stm8_pro/read_template.py -> /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_stm8/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro/stm8_setup.py to stm8_setup.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro/write_template.py to write_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_stm8/stm8_pro/read_template.py to read_template.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating gen_stm8.egg-info
writing requirements to gen_stm8.egg-info/requires.txt
writing gen_stm8.egg-info/PKG-INFO
writing top-level names to gen_stm8.egg-info/top_level.txt
writing dependency_links to gen_stm8.egg-info/dependency_links.txt
writing manifest file 'gen_stm8.egg-info/SOURCES.txt'
reading manifest file 'gen_stm8.egg-info/SOURCES.txt'
writing manifest file 'gen_stm8.egg-info/SOURCES.txt'
Copying gen_stm8.egg-info to /usr/local/lib/python2.7/dist-packages/gen_stm8-1.0.0-py2.7.egg-info
```

Install lib data
```
python setup.py install_data
running install_data
copying gen_stm8/run/gen_stm8_run.py -> /usr/local/bin/
copying gen_stm8/run/factory_reset.sh -> /usr/local/bin/
creating /usr/local/lib/python2.7/dist-packages/gen_stm8/conf
copying gen_stm8/conf/gen_stm8.cfg -> /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/
copying gen_stm8/conf/gen_stm8_util.cfg -> /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template
copying gen_stm8/conf/template/Makefile.template -> /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template/
copying gen_stm8/conf/template/stm8s.template -> /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template/
copying gen_stm8/conf/template/module.template -> /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template/
copying gen_stm8/conf/project.yaml -> /usr/local/lib/python2.7/dist-packages/gen_stm8/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_stm8/log
copying gen_stm8/log/gen_stm8.log -> /usr/local/lib/python2.7/dist-packages/gen_stm8/log/
```

Or You can use docker to create image/container.

[![gen_stm8 docker checker](https://github.com/vroncevic/gen_stm8/workflows/gen_stm8%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_stm8/actions?query=workflow%3A%22gen_stm8+docker+checker%22)

### Dependencies

**gen_stm8** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/gen_stm8_flow.png)

### Tool structure

**gen_stm8** is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/gen_stm8.png)

Generator structure:

```
.
├── conf/
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
├── run/
│   ├── factory_reset.sh
│   └── gen_stm8_run.py
└── stm8_pro/
    ├── __init__.py
    ├── read_template.py
    ├── stm8_setup.py
    └── write_template.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_stm8/badge/?version=latest)](https://gen_stm8.readthedocs.io/projects/gen_stm8/en/latest/?badge=latest)

More documentation and info at:
* [gen_stm8.readthedocs.io](https://gen_stm8.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 by [vroncevic.github.io/gen_stm8](https://vroncevic.github.io/gen_stm8/)

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
