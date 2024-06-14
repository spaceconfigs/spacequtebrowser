#!/bin/bash
echo "-------------> Installing Qutebrowser"
#$pminstall $PROGRAM

echo "-------------> Configurando Qutebrowser"
mkdir -p ~/.config/qutebrowser
ln -sf * $HOME/.config/qutebrowser/
