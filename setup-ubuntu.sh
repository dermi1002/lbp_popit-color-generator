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

function yesNoPrompt() {
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
	printf "$lbp_pcg_prefix Removing Virtual Environment...\n" && \
	rm -rf "$VIRTUALENV"
}

function incompleteMessage() {
	local quitMessage

	quitMessage="$1"

	read -p "$lbp_pcg_prefix $quitMessage Press any key to continue..." -n1 -s && \
	exit 1
}

function quitAborted() {
	"incompleteMessage" "Setup Aborted."
}

function quitSuccess() {
	printf "$lbp_pcg_prefix Quitting...\n" && \
	exit 0
}

# Sequence

function internetPackageConfirm() {
	"yesNoPrompt" "This script requires connection to the Internet and Packages for Python's Virtual Environment System and GUI Library Tkinter. Continue?" "virtualEnvironment" "quitAborted"
}

function virtualEnvironment() {
	# if there's a directory with the same name as '.venv_ubuntu'...
	if [ -d "$VIRTUALENV" ]; then
		"yesNoPrompt" "A directory named '.venv_ubuntu/' already exists. Overwrite all data within it?" "removeVirtualEnv" "mainScript"
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
		"yesNoPrompt" "A script named 'lbp_pcg.sh' already exists. Overwrite all data within it?" "mainScriptContent" "setupComplete"
	else
		printf "$lbp_pcg_prefix Creating $lbp_pcg_script...\n"
		touch lbp_pcg.sh
		"mainScriptContent"
	fi
}

function mainScriptContent() {
	printf "$lbp_pcg_prefix Giving contents to $lbp_pcg_script...\n" && \

	# oh THANK GOODNESS! also using white spaces as tabs for the sake of this process
	cat > "$SCRIPTFILE" <<- EndOfScript
	#!/bin/bash

	# Text styling for LBP PCG Name
	text_bold=\$(tput bold)
	text_cyan=\$(tput setaf 6)
	text_reset=\$(tput sgr0) # resets all text style attributes

	lbp_pcg_prefix="\${text_bold}\${text_cyan}LBP Popit Color Generator\${text_reset}:"

	# Script's Code

	# Functions

	function errorMessage() {
	    local messageText

	    messageText="\$1"

	    read -p "\$lbp_pcg_prefix \$messageText Press any key to continue..." -n1 -s && \\
	    exit 1
	}
	
	function run_main_program() {
	    printf "\$lbp_pcg_prefix Starting Main Script...\n" && \\
	    .venv_ubuntu/bin/python src/main.py && \\
	    printf "\$lbp_pcg_prefix Quitting...\n"
	}

	function checkFiles() {
	    if [ ! -d .venv_ubuntu ]; then
	        "errorMessage" "The Virtual Environment directory doesn't exist. Execute the Setup script or make the Virtual Environment yourself."
	    elif [ ! -e src/main.py ]; then
	        "errorMessage" "Cannot find the Main Program in 'src/main.py'. Make sure you have left everything as it was when the project was downloaded."
	    else
	        "run_main_program"
	    fi
	}

	function main() {
	    trap 'printf "\$lbp_pcg_prefix Has an error occurred?\n"' ERR
	    "checkFiles"
	}

	"main"
	EndOfScript

	printf "$lbp_pcg_prefix Granting execution permissions to $lbp_pcg_script...\n" && \
	chmod +x lbp_pcg.sh

	"setupComplete"
}

function setupComplete() {
	"yesNoPrompt" "Setup successfully completed! Would you like to run the main script?" "runMainScript" "quitSuccess"
}

function runMainScript() {
	if [ ! -e src/main.py ]; then
		"incompleteMessage" "Cannot find the Main Program in 'src/main.py'. Make sure you have left everything as it was when the project was downloaded."
	else
		printf "$lbp_pcg_prefix Starting Main Script...\n" && \
		.venv_ubuntu/bin/python src/main.py && \
		"quitSuccess"
	fi
}

# Execution

function main() {
	trap 'echo "$lbp_pcg_prefix Has an error occurred?"' ERR
	"internetPackageConfirm"
}

"main"