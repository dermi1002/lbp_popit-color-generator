#!/bin/bash

# Text Styling
text_bold=$(tput bold)
text_cyan=$(tput setaf 6)
text_yellow=$(tput setaf 3)
text_reset=$(tput sgr0) # resets all text style attributes

lbp_pcg_prefix="${text_bold}${text_cyan}LBP Popit Color Generator${text_reset}:"
lbp_pcg_script="${text_bold}${text_yellow}lbp_pcg.sh${text_reset}"

# Script's Code
read -p "$lbp_pcg_prefix This script requires connection to the internet. Continue? (Y/n): " confirm && \
[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

trap 'echo "$lbp_pcg_prefix Has an error occurred?"' ERR
printf "$lbp_pcg_prefix Creating Virtual Environment...\n" && \
python3 -m venv .venv_ubuntu && \
printf "$lbp_pcg_prefix Activating Virtual Environment...\n" && \
source .venv_ubuntu/bin/activate && \
printf "$lbp_pcg_prefix Upgrading Pip, Setuptools, Wheel...\n" &&\
python3 -m pip install --upgrade pip --upgrade setuptools --upgrade wheel && \
printf "$lbp_pcg_prefix Installing Requirements...\n" && \
pip install -r src/requirements.txt && \

SCRIPTFILE=lbp_pcg.sh

# if there's a shell script with the same name as 'lbp_pcg.sh'...
if [ -e $SCRIPTFILE ]; then
	read -p "$lbp_pcg_prefix A script named 'lbp_pcg.sh' already exists. Overwrite all data within it? (Y/n): " confirm && \
	[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
else
	printf "$lbp_pcg_prefix Creating $lbp_pcg_script...\n"
	touch lbp_pcg.sh
fi

printf "$lbp_pcg_prefix Giving contents to $lbp_pcg_script...\n"
cat > $SCRIPTFILE << EndOfScript
#!/bin/bash

# Text styling for LBP PCG Name
text_bold=\$(tput bold)
text_cyan=\$(tput setaf 6)
text_reset=\$(tput sgr0) # resets all text style attributes

lbp_pcg_prefix="\${text_bold}\${text_cyan}LBP Popit Color Generator\${text_reset}:"

# Script's Code
run_main_program() {
	trap 'printf "\$lbp_pcg_prefix Has an error occurred?\n"' ERR
	printf "\$lbp_pcg_prefix Activating Virtual Environment...\n" && \\
	source .venv_ubuntu/bin/activate && \\
	printf "\$lbp_pcg_prefix Starting Main Script...\n" && \\
	python3 src/main.py && \\
	printf "\$lbp_pcg_prefix Deactivating Virtual Environment...\n" && \\
	deactivate && \\
	printf "\$lbp_pcg_prefix Quitting...\n"
}

if [ ! -d .venv ]; then
	printf "\$lbp_pcg_prefix The Virtual Environment directory doesn't exist. Execute the Setup script or make the Virtual Environment yourself."
else
	run_main_program
fi
EndOfScript

printf "$lbp_pcg_prefix Granting execution permissions to $lbp_pcg_script...\n"
chmod +x lbp_pcg.sh

read -p "$lbp_pcg_prefix Setup completed successfully! Would you like to run the main script? (Y/n): " confirm && \
[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

printf "$lbp_pcg_prefix Starting Main Script...\n" && \
python3 src/main.py && \
printf "$lbp_pcg_prefix Deactivating Virtual Environment...\n" && \
deactivate && \
printf "$lbp_pcg_prefix Quitting...\n"
