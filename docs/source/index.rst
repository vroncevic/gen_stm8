STM8 project skeleton generator
--------------------------------

**gen_stm8** is toolset for generation STM8 project skeleton for
developmet of embedded applications.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_stm8 python checker| |gen_stm8 python package| |github issues| |documentation status| |github contributors|

.. |gen_stm8 python checker| image:: https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python_checker.yml

.. |gen_stm8 python package| image:: https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_stm8.svg
   :target: https://github.com/vroncevic/gen_stm8/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_stm8.svg
   :target: https://github.com/vroncevic/gen_stm8/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-avr8/badge/?version=latest
   :target: https://gen-avr8.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_stm8 python3 build|

.. |gen_stm8 python3 build| image:: https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_stm8/actions/workflows/gen_stm8_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_stm8/releases

To install **gen_stm8** type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_stm8

Dependencies
-------------

**gen_stm8** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_stm8** is based on OOP.

Code structure

.. code-block:: bash

    gen_stm8
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

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 - 2024 by `vroncevic.github.io/gen_stm8 <https://vroncevic.github.io/gen_stm8>`_

**gen_stm8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
