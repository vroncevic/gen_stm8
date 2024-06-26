/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * main.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * new_simple_test is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * new_simple_test is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "stm8s.h"

int main() {
    int i,j;
    PB_DDR|=0x20;
    PB_CR1|=0x20;
    PB_CR2|=0x00;
    while(1) {
        PB_ODR^=0xf0;
        for(i=0;i<200;i++)
        for(j=0;j<800;j++);
    }
}

