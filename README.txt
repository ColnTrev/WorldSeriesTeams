---------
Overview:
---------
This software package contains the python scripts used to conduct
the final project for CSS581A Machine Learning. The project examines the
effectiveness of classifying World Series winners and losers based of their
total regular season statistics. The contents of the package as well as how to
replicate the experiment are detailed below.
If there are any issues with the files please send an email to the program's creator
Collin Gordon at colntrev@gmail.com with a detail of your problem.  
---------------
Included Files:
---------------
classification.py
data_combiner.py
features_and_labels.py
observations.py
reorder.py
testharness.py
team.csv
postseason.csv

Screen Captures of the various program steps can be found inside the
Screencaps folder.
-------------------
Required Libraries:
-------------------
This program requires python3 and the following libraries:
Scikit Learn
Pandas
These libraries can be downloaded using the pip package manager.
It is recommended that this package is run on Linux or Mac OSX so that the
included run.sh can be used.

To configure the bash script for execution simply type:
chmod u+x run.sh
Then the program can be run by typing ./run.sh into the terminal.
If executing without the bash script, open the script and run each python file in the order the
script runs them.
------------------
Program Execution:
------------------
This program begins by running the preprocessing stage followed by the test harness concluded
by the classification.
After the preprocessing four csv files should be added to your directory:
data_combiner.csv
data_ordered.csv
features.csv
labels.csv
After the test harness is complete, a bar graph will appear. You must close the window
to the bar graph to begin the classification. First, the classification will output the adaboost
confusion matrix for 50%. Upon closing this window the confusion matrix for the polynomial SVM at
50% will be displayed. If you desire to see the results with a different test size, simply open the
classification.py file and in the line containing: 
"X_train, X_test, Y_train, Y_test = train_test_split(f_adjust, l_data, test_size = 0.5, random_state = 0)"
set the test_size to a decimal between 0.0 and 1.0.

NOTE: If you wish to run the script again the above mentioned csv files must be deleted.
--------------- 
Execution Time:
---------------
52 seconds on Linux Ubuntu 16.04
-------------------
Additional Scripts:
-------------------
An observation.py script is included in the package. This script may be run after creating the data_ordered.csv
file to make observations about individual data points. Simply, plug in the values you wish to view inside the brackets
at the line containing:
"d1 = data[['year', 'team_id', 'soa']]"
and change the parameter in the line containing:
"sorted = pd.DataFrame.sort_values(d1, 'soa')"
from 'soa' to any of the parameters you selected to get a print out to the console or piped file of every team's information
for that statistic.
--------------------

