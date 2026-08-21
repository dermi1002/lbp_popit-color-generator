#!/bin/bash

# Text Styling
textBold=$(tput bold)
textCyan=$(tput setaf 6)
textYellow=$(tput setaf 3)
textReset=$(tput sgr0) # resets all text style attributes

# Styled Phrases
lbpPcgPrefix="${textBold}${textCyan}LBP Popit Color Generator${textReset}:"
lbpPcgScript="${textBold}${textYellow}lbp_pcg.sh${textReset}"

# File/Directory Paths
VIRTUALENV=.venv_ubuntu/ # "Env" being short for "Environment"
SCRIPTFILE=lbp_pcg.sh

# Script's Code

# Functions

function custom_print() {
	local printText

	printText="$1"

	printf "$lbpPcgPrefix $printText\n"
}

function yes_no_prompt() {
	local promptText
	local yesCommand
	local noCommand

	promptText="$1"
	yesCommand="$2"
	noCommand="$3"

	# this process repeats if the user doesn't answer yes/no
	while true; do
		read -p "$lbpPcgPrefix $promptText (Y/n): " promptAnswer && \
		if [[ $promptAnswer == [yY] || $promptAnswer == [yY][eE][sS] ]]; then
			"$yesCommand"
		elif [[ $promptAnswer == [nN] || $promptAnswer == [nN][oO] ]]; then
			"$noCommand"
		fi
	done
}

function incomplete_message() {
	local quitMessage

	quitMessage="$1"

	read -p "$lbpPcgPrefix $quitMessage Press any key to continue..." -n1 -s && \
	# line break so terminal text doesn't clutter up
	printf "\n" && \ 
	exit 1
}

function quit_aborted() {
	"incomplete_message" "Setup Aborted."
}

function quit_success() {
	"custom_print" "Quitting..." && \
	exit 0
}

# Sequence

function internet_package_confirm() {
	"yes_no_prompt" "This script requires connection to the Internet and Packages for Python's Virtual Environment System and GUI Library Tkinter. Continue?" "virtual_environment_check" "quit_aborted"
}

function virtual_environment_check() {
	# if there's a directory with the same name as '.venv_ubuntu'...
	if [ -d "$VIRTUALENV" ]; then
		"yes_no_prompt" "A directory named '.venv_ubuntu/' already exists. Overwrite all data within it?" "remove_virtual_env" "main_script_setup"
	else
		"virtual_environment_setup"
	fi
}

function remove_virtual_env() {
	"custom_print" "Removing Virtual Environment..." && \
	rm -rf "$VIRTUALENV" && \
	"virtual_environment_setup"
}

function virtual_environment_setup() {
	"custom_print" "Creating Virtual Environment..." && \
	python3 -m venv .venv_ubuntu && \

	"custom_print" "Updating Pip..." && \
	.venv_ubuntu/bin/python -m pip install --upgrade pip && \

	"custom_print" "Installing Requirements..." && \
	.venv_ubuntu/bin/python -m pip install -r src/requirements.txt && \

	"main_script_setup"
}

function main_script_setup() {
	# if there's a shell script with the same name as 'lbp_pcg.sh'...
	if [ -e "$SCRIPTFILE" ]; then
		"yes_no_prompt" "A script named 'lbp_pcg.sh' already exists. Overwrite all data within it?" "main_script_content" "setup_complete"
	else
		"custom_print" "Creating $lbpPcgScript..." && \
		touch lbp_pcg.sh
		"main_script_content"
	fi
}

function main_script_content() {
	"custom_print" "Giving contents to $lbpPcgScript..." && \

	# oh THANK GOODNESS! also using white spaces as tabs for the sake of this process
	cat > "$SCRIPTFILE" <<- EndOfScript
	#!/bin/bash

	# Text styling for LBP PCG Name
	textBold=\$(tput bold)
	textCyan=\$(tput setaf 6)
	textReset=\$(tput sgr0) # resets all text style attributes

	lbpPcgPrefix="\${textBold}\${textCyan}LBP Popit Color Generator\${textReset}:"

	# Script's Code

	# Functions

	function error_message() {
	    local messageText

	    messageText="\$1"

	    read -p "\$lbpPcgPrefix \$messageText Press any key to continue..." -n1 -s && \\
	    exit 1
	}
	
	function run_main_program() {
	    printf "\$lbpPcgPrefix Starting Main Script...\n" && \\
	    .venv_ubuntu/bin/python src/main.py && \\
	    printf "\$lbpPcgPrefix Quitting...\n"
	}

	function check_files() {
	    if [ ! -d .venv_ubuntu ]; then
	        "error_message" "The Virtual Environment directory doesn't exist. Execute the Setup script or make the Virtual Environment yourself."
	    elif [ ! -e src/main.py ]; then
	        "error_message" "Cannot find the Main Program in 'src/main.py'. Make sure you have left everything as it was when the project was downloaded."
	    else
	        "run_main_program"
	    fi
	}

	function main() {
	    trap 'printf "\$lbpPcgPrefix Has an error occurred?\n"' ERR
	    "check_files"
	}

	"main"
	EndOfScript

	"custom_print" "Granting execution permissions to $lbpPcgScript..." && \
	chmod +x lbp_pcg.sh

	"setup_complete"
}

function setup_complete() {
	"yes_no_prompt" "Setup successfully completed! Would you like to run the main script?" "run_main_python" "quit_success"
}

function run_main_python() {
	if [ ! -e src/main.py ]; then
		"incomplete_message" "Cannot find the Main Program in 'src/main.py'. Make sure you have left everything as it was when the project was downloaded."
	else
		"custom_print" "Starting Main Script..." && \
		.venv_ubuntu/bin/python src/main.py && \
		"quit_success"
	fi
}

# Execution

function main() {
	trap 'echo "$lbpPcgPrefix Has an error occurred?"' ERR
	"internet_package_confirm"
}

"main"