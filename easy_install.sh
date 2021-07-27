#!/usr/bin/env bash

# Variable

COMMAND=arpy
COMMAND_JW=بايثون

# Creating a link to local bin so that we do not required to add class path
cp $PWD/bin/cmd.sh bin/${COMMAND}
chmod +x  $PWD/bin/${COMMAND}

rm -f /usr/local/bin/${COMMAND}
rm -f /usr/local/bin/${COMMAND_JW}

ln -s $PWD/bin/${COMMAND} /usr/local/bin/${COMMAND}
ln -s $PWD/bin/${COMMAND} /usr/local/bin/${COMMAND_JW}

echo "Installation successful"
echo "ꦮꦸꦱ꧀ꦏꦱꦶꦭ꧀ꦏꦲꦶꦤ꧀ꦱ꧀ꦠꦭ꧀"