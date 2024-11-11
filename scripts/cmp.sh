#!/usr/bin/env bash

cmp -l $1 $2 | awk '{printf "%s %02X %02X\n", $1, $2, $3}'