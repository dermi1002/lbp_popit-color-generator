#!/bin/bash

# Text Styling
text_bold=$(tput bold)
text_cyan=$(tput setaf 6)
text_yellow=$(tput setaf 3)
text_reset=$(tput sgr0) # resets all text style attributes

# Styled Phrases
lbp_pcg_prefix="${text_bold}${text_cyan}LBP Popit Color Generator${text_reset}:"
lbp_pcg_script="${text_bold}${text_yellow}lbp_pcg.sh${text_reset}"

# File/Directory Paths
VIRTUALENV=.venv_ubuntu/ # "Env" being short for "Environment"
SCRIPTFILE=lbp_pcg.sh

# Script's Code

# Functions

function confirmTestPrompt() {
	local promptText
	local yesCommand
	local noCommand

	promptText="$1"
	yesCommand="$2"
	noCommand="$3"

	read -p "$lbp_pcg_prefix $promptText (Y/n): " confirm && \
	[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || "$noCommand"
	# I'll change this into a more readable format

	"$yesCommand"
}

function removeVirtualEnv() {
	printf "$lbp_pcg_prefix Removing Virtual Environment...\n"
	rm -rf "$VIRTUALENV"
}

function quitAborted() {
	printf "$lbp_pcg_prefix Setup Aborted.\n"
	exit 1
}

function quitSuccess() {
	printf "$lbp_pcg_prefix Quitting...\n"
	exit 0
}

# Sequence

function internetPackageConfirm() {
	trap 'echo "$lbp_pcg_prefix Has an error occurred?"' ERR
	"confirmTestPrompt" "This script requires connection to the Internet and Packages for Python's Virtual Environment System and GUI Library Tkinter. Continue?" "virtualEnvironment" "quitAborted"
}

function virtualEnvironment() {
	# if there's a directory with the same name as '.venv_ubuntu'...
	if [ -d "$VIRTUALENV" ]; then
		"confirmTestPrompt" "A directory named '.venv_ubuntu/' already exists. Overwrite all data within it?" "removeVirtualEnv" "mainScript"
	fi

	printf "$lbp_pcg_prefix Creating Virtual Environment...\n" && \
	python3 -m venv .venv_ubuntu && \
	printf "$lbp_pcg_prefix Updating Pip...\n" && \
	.venv_ubuntu/bin/python -m pip install --upgrade pip && \
	printf "$lbp_pcg_prefix Installing Requirements...\n" && \
	.venv_ubuntu/bin/python -m pip install -r src/requirements.txt && \

	"mainScript"
}

function mainScript() {
	# if there's a shell script with the same name as 'lbp_pcg.sh'...
	if [ -e "$SCRIPTFILE" ]; then
		"confirmTestPrompt" "A script named 'lbp_pcg.sh' already exists. Overwrite all data within it?" "mainScriptContent" "setupComplete"
	else
		printf "$lbp_pcg_prefix Creating $lbp_pcg_script...\n"
		touch lbp_pcg.sh
		"mainScriptContent"
	fi
}

function mainScriptContent() {
	printf "$lbp_pcg_prefix Giving contents to $lbp_pcg_script...\n"

	# oh THANK GOODNESS! also using white spaces as tabs for the sake of this process
	cat > "$SCRIPTFILE" <<- EndOfScript
	#!/bin/bash

	# Text styling for LBP PCG Name
	text_bold=\$(tput bold)
	text_cyan=\$(tput setaf 6)
	text_reset=\$(tput sgr0) # resets all text style attributes

	lbp_pcg_prefix="\${text_bold}\${text_cyan}LBP Popit Color Generator\${text_reset}:"

	# Script's Code
	run_main_program() {
	    trap 'printf "\$lbp_pcg_prefix Has an error occurred?\n"' ERR
	    printf "\$lbp_pcg_prefix Starting Main Script...\n" && \\
	    .venv_ubuntu/bin/python src/main.py && \\
	    printf "\$lbp_pcg_prefix Quitting...\n"
	}

	if [ ! -d .venv_ubuntu ]; then
	    printf "\$lbp_pcg_prefix The Virtual Environment directory doesn't exist. Execute the Setup script or make the Virtual Environment yourself.\n"
	else
	    run_main_program
	fi
	EndOfScript

	printf "$lbp_pcg_prefix Granting execution permissions to $lbp_pcg_script...\n"
	chmod +x lbp_pcg.sh

	"setupComplete"
}

function setupComplete() {
	"confirmTestPrompt" "Setup successfully completed! Would you like to run the main script?" "runMainScript" "quitSuccess"
}

function runMainScript() {
	printf "$lbp_pcg_prefix Starting Main Script...\n" && \
	.venv_ubuntu/bin/python src/main.py && \
	"quitSuccess"
}

# Execution

"internetPackageConfirm"