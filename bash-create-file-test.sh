#!/bin/bash

SCRIPTFILE=lbp_pcg.sh

# if there's a shell script with the same name as 'lbp_pcg.sh'...
if [ -e $SCRIPTFILE ]; then
	read -p "A script named 'lbp_pcg.sh' already exists. Overwrite all data within it? (y/n): " confirm && \
	[[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
else
	touch lbp_pcg.sh
fi

cat > $SCRIPTFILE << EndOfScript
#!/bin/bash

run_main_program() {
	trap 'echo "Has an error occurred?"' ERR
	echo "Activating Virtual Environment..." && \\
	source .venv/bin/activate && \\
	echo "Starting Main Script..." && \\
	python3 main.py && \\
	echo "Deactivating Virtual Environment..." && \\
	deactivate && \\
	echo "Quitting..."
}

if [ ! -d .venv ]; then
	echo "The Virtual Environment directory doesn't exist. Execute the Setup script or make the Virtual Environment yourself."
else
	run_main_program
fi
EndOfScript
