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

function yes_no_prompt() {
	local promptText
	local yesCommand
	local noCommand

	promptText="$1"
	yesCommand="$2"
	noCommand="$3"

	read -p "$lbpPcgPrefix $promptText (Y/n): " confirm && \
	[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || "$noCommand"
	# I'll change this into a more readable format

	"$yesCommand"
}

function remove_virtual_env() {
	printf "$lbpPcgPrefix Removing Virtual Environment...\n" && \
	rm -rf "$VIRTUALENV"
}

function incomplete_message() {
	local quitMessage

	quitMessage="$1"

	read -p "$lbpPcgPrefix $quitMessage Press any key to continue..." -n1 -s && \
	exit 1
}

function quit_aborted() {
	"incomplete_message" "Setup Aborted."
}

function quit_success() {
	printf "$lbpPcgPrefix Quitting...\n" && \
	exit 0
}

# Sequence

function internet_package_confirm() {
	"yes_no_prompt" "This script requires connection to the Internet and Packages for Python's Virtual Environment System and GUI Library Tkinter. Continue?" "virtual_environment_setup" "quit_aborted"
}

function virtual_environment_setup() {
	# if there's a directory with the same name as '.venv_ubuntu'...
	if [ -d "$VIRTUALENV" ]; then
		"yes_no_prompt" "A directory named '.venv_ubuntu/' already exists. Overwrite all data within it?" "remove_virtual_env" "main_script_setup"
	fi

	printf "$lbpPcgPrefix Creating Virtual Environment...\n" && \
	python3 -m venv .venv_ubuntu && \
	printf "$lbpPcgPrefix Updating Pip...\n" && \
	.venv_ubuntu/bin/python -m pip install --upgrade pip && \
	printf "$lbpPcgPrefix Installing Requirements...\n" && \
	.venv_ubuntu/bin/python -m pip install -r src/requirements.txt && \

	"main_script_setup"
}

function main_script_setup() {
	# if there's a shell script with the same name as 'lbp_pcg.sh'...
	if [ -e "$SCRIPTFILE" ]; then
		"yes_no_prompt" "A script named 'lbp_pcg.sh' already exists. Overwrite all data within it?" "main_script_content" "setup_complete"
	else
		printf "$lbpPcgPrefix Creating $lbpPcgScript...\n"
		touch lbp_pcg.sh
		"main_script_content"
	fi
}

function main_script_content() {
	printf "$lbpPcgPrefix Giving contents to $lbpPcgScript...\n" && \

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

	printf "$lbpPcgPrefix Granting execution permissions to $lbpPcgScript...\n" && \
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
		printf "$lbpPcgPrefix Starting Main Script...\n" && \
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