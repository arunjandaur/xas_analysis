/////PrenderTasks/////

Lev's Work on Monday:
+Implemented periodicity module


TODO:
+Use histogram to detect structural characteristics
+Look into Solid State Physics
+Need to input periodity module into relationship contstruction
+Need to alter nodes to stores numpy arrays of their coordinates and delete coordinate class
+Look into splining for finding best fit model
+Talk to Lev about how splining will be used because David and he thought of a few ideas
+Do the above bullet point
+Think about how to implement angle generation

+Change histogram from using a dictionary with a list that is split up into buckets. The reason is to be able to have buckets who have zero frequency because it has very useful properties for splining and finding important points.In addition, each node should now have its own histogram of the all the type of neighbors it has to compare with other nodes later.


TRAC instructions:
Make a trac account and get David to authorize you to pull the repo
ssh into hopper
cd /project/projectdirs/mftheory/www
mkdir USERNAME
chmod 755 USERNAME
git clone http://USERNAME@trac-foundry.lbl.gov/git/webtools.git
./configure.sh
