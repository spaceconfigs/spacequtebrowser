echo "-------------> Installing Qutebrowser"
#$pminstall $PROGRAM

echo "-------------> Configurando Qutebrowser"
mkdir -p $HOME/.qutebrowser
ln -sf $(pwd)/Qutebrowser/* $HOME/.qutebrowser
