source ./activate_nukediffusion-env.sh
pip freeze | xargs pip uninstall -y
deactivate
echo ""
echo - nukediffusion-env has been deactivated!
echo ""