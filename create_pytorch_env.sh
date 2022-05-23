#!/bin/bash 

###################################################################
#Script Name : create_pytorch_env.sh
#Description : Create a conda env for pytorch
#### How to remove: ####
# conda env remove -p /tigress/cw55/envs/pytorch
###################################################################
# exit when any command fails
set -e
# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

# command starts here
conda create -y --prefix /tigress/cw55/envs/pytorch python=3.10 numpy=1.21
conda activate /tigress/cw55/envs/pytorch
conda install -y pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
conda install -y -c conda-forge matplotlib=3 cartopy scipy scikit-learn numba ipykernel
python -m ipykernel install --user --name pytorch
conda deactivate 
echo 'conda enviroment for pytorch created!'
exit
