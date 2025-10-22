#!/bin/bash

bold=$(tput bold)
normal=$(tput sgr0) # resets all text style attributes

lbp_pcg_prefix="${bold}LBP Popit Color Generator${normal}:"

read -p "$lbp_pcg_prefix This script requires connection to the internet. Continue? (y/n): " confirm && \
[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

trap 'echo "$lbp_pcg_prefix Has an error occurred?"' ERR
echo "$lbp_pcg_prefix Creating Virtual Environment..." && \
python3 -m venv .venv && \
echo "$lbp_pcg_prefix Activating Virtual Environment..." && \
source .venv/bin/activate && \
echo "$lbp_pcg_prefix Upgrading Pip, Setuptools, Wheel..." &&\
python3 -m pip install --upgrade pip --upgrade setuptools --upgrade wheel && \
echo "$lbp_pcg_prefix Installing Requirements..." && \
pip install -r requirements.txt && \
echo "$lbp_pcg_prefix Deactivating Virtual Environment..." && \
deactivate && \
echo "$lbp_pcg_prefix Setup Success!"
