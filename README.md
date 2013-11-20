/////PrenderTasks/////

TODO:
Linear algebra module
Use histogram to detect structural characteristics
Revise nodal graph for efficiency
Look into Solid State Physics
Implement periodicity


Write a command line tool:
	Input: One .xyz file that contains many snapshots and a list of excited atoms with line numbers
	Output: A bunch of text that lists every single distance, angle, and/or dihedral around each excited atom

	Other functionality: Provide a snapshot and excited atom, and fetch xyz coordinates


TRAC instructions:
Make a trac account and get David to authorize you to pull the repo
ssh into hopper
cd /project/projectdirs/mftheory/www
mkdir USERNAME
chmod 755 USERNAME
git clone http://USERNAME@trac-foundry.lbl.gov/git/webtools.git
./configure.sh
