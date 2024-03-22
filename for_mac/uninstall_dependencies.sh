source ./activate_nukediffusion-env.sh
pip3 freeze | xargs pip uninstall -y
deactivate
echo ""
echo - nukediffusion-env has been deactivated!
echo ""