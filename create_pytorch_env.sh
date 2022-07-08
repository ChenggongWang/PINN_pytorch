#!/bin/bash 

###################################################################
#Script Name : create_pytorch_env.sh
#Description : Create a conda env for pytorch
#### run with interactive bash
# bash -i create_pytorch_env
#### How to remove: ####
# conda env remove --name pytorch_env --all
###################################################################
# exit when any command fails
set -e
# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

# command starts here
conda create -y -n pytorch_env python=3.10 numpy=1.21
conda activate pytorch_env
conda install -y pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
conda install -y -c conda-forge matplotlib=3 cartopy scipy scikit-learn numba ipykernel
python -m ipykernel install --user --name pytorch
conda deactivate 
echo 'conda enviroment for pytorch created!'
exit
