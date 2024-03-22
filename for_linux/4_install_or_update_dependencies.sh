source ./activate_nukediffusion-env.sh
pip install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location
deactivate
echo ""
echo - nukediffusion-env has been deactivated!
echo ""