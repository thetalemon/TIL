#!/bin/sh

echo "exit on subshell"
$(exit 1)
echo "resultcode:$?"

echo "do exit"
exit 1
echo "resultcode:$?"

echo "end"
