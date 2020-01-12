# STM8 project skeleton generator.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install this set of modules type the following:

```
cp -R ~/gen_stm8_scripts/bin/   /root/scripts/gen_stm8/ver.1.0/
cp -R ~/gen_stm8_scripts/conf/  /root/scripts/gen_stm8/ver.1.0/
cp -R ~/gen_stm8_scripts/log/   /root/scripts/gen_stm8/ver.1.0/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### Tool structure

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_stm8/dev/python-tool-docs/gen_stm8.png)

```
.
├── bin/
│   ├── factory_reset.sh
│   ├── gen_stm8.py
│   ├── gen_stm8_run.py
│   └── stm8_pro/
│       ├── __init__.py
│       ├── read_template.py
│       ├── stm8_setup.py
│       └── write_template.py
├── conf/
│   ├── gen_stm8.cfg
│   ├── gen_stm8_util.cfg
│   └── template/
│       ├── Makefile.template
│       ├── module.template
│       └── stm8s.template
└── log/
    └── gen_stm8.log

```

### COPYRIGHT AND LICENCE

Copyright (C) 2020 by https://vroncevic.github.io/gen_stm8/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:
