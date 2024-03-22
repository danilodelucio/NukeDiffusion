source ./activate_nukediffusion-env.sh
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu --no-warn-script-location
deactivate
echo ""
echo - nukediffusion-env has been deactivated!
echo ""