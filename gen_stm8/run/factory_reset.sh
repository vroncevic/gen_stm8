#!/bin/bash
#
# @brief   Factory reset fir uC stm8s103f3
# @version ver.1.4.3
# @date    Sun Jan 12 17:05:40 CET 2020
# @company None, free software to use 2020
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

echo "00 00 ff 00 ff 00 ff 00 ff 00 ff" | xxd -r -p > factory_defaults.bin
stm8flash -c stlinkv2 -p stm8s103f3 -s opt -w factory_defaults.bin

