#!/bin/sh

function test_return(){
    return 1
}

echo "do return function on subshell"
$(test_return)
echo "resultcode:$?"

echo "do return function"
test_return
echo "resultcode:$?"

echo "end"
