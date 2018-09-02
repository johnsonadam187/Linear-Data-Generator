# Projects
Linear Data Genereator
Function for dataset generator which randomly chooses y values based randomly from an inital regression derived from user inputs/specifications.
x_axis_start is the first value on the x axis
x_axis_end is the last value on the x axis
m_value = slope of the linear regression line that the secondary dataset is created around (this is not the slope value of the resulting dataset)
c_value is the y intercept of the best fits line created of the initial dataset.

The function creates an initial best fits line, then generates an array of new y data based on a randomly assigned(+/-) variation from the line.
Next it removes a random amount of the data points(x and y). Also there is built in functionality to output to a pandas dataframe, then to a csv file,
so users can create data sets, and then practice importing the data and analysing for themselves. Some of the parts of the code have been commented, 
plotting of the initial regression line, the secondary regression line, and code for file output are included as comments which can be included 
dependant on the users requirements. File output requires an argument 'filepath' to be added to the definition of the function, which subsequnetly will
require the user to enter the filepath if they require the dataset to be saved for later analysis. Also for uniformity a seed 
(np.random.seed(x)), can be added to ensure replication. 

I created this as i was studying linear regression and couldnt find practice datasets to analyse.

