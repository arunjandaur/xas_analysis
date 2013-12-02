/////PrenderTasks/////

Lev's Work on Monday:
+Implemented periodicity module


TODO:
+IMPORTANT: Fix distance generation. We are generating repeats. If you use a bucket size of .000000001, then you will realize that everything maps to its own bucket, but that there are 2 occurrences for each. This bucket width is so small that the only way we are getting a frequency of 2 is that there are exactly 2 of every angle. Also, if you slightly larger and larger values, you will notice horizontal lines emerging for higher frequencies. These frequencies stride by 2's. Lev, ask Arun for a demo.
+Use histogram to detect structural characteristics
+Look into Solid State Physics
+Need to input periodity module into relationship construction
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
