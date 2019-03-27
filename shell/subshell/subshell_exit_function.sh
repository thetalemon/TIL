#!/bin/sh

function test_exit(){
    exit 1
}

echo "do exit function on subshell"
$(test_exit)
echo "resultcode:$?"

echo "do exit function"
test_exit
echo "resultcode:$?"

echo "end"
