#!/bin/bash
echo "-------------> Installing Qutebrowser"
#$pminstall $PROGRAM

echo "-------------> Configurando Qutebrowser"
ln -sf $(pwd) $HOME/.config/qutebrowser
