#!/bin/bash
#
# @brief   gen_stm8
# @version 1.4.8
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_stm8
pylint gen_stm8 > gen_stm8.report
echo "Done"
