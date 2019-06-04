import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd  

def linear_generator(x_axis_start, x_axis_end, m_value, b_value):
    #generate x axis
    x_axis = np.arange(x_axis_start, x_axis_end, step=abs(x_axis_start))

    #generate best fits line
    y_coords = np.empty(len(x_axis))
    for i in range(len(x_axis)):
        y_coords[i] = m_value*x_axis[i]+b_value

    #generate new y values
    y_value_spread = (y_coords[i]/np.random.randint(0, 10))
    new_y = np.empty(len(x_axis))
    for i in range(len(x_axis)):
        coinflip = np.random.randint(0, 2)
        if coinflip == 0:
            new_y[i] = np.random.uniform(y_coords[i], y_coords[i]+y_value_spread, size = 1)
        else:
            new_y[i] = np.random.uniform(y_coords[i], y_coords[i]-y_value_spread, size = 1)

    #remove amount of data for random x spread
    missing_vals = np.random.uniform(0, 1.0)
    delete_vals = np.empty(int(len(x_axis)*missing_vals))
    for i in range(int(len(x_axis)*missing_vals)):
        delete_vals[i] = np.random.randint(x_axis_start, len(x_axis)) 
    next_x = np.delete(x_axis, delete_vals) 
    next_y = np.delete(new_y, delete_vals)

    #plot new dataset
    plt.plot(next_x, next_y, marker='.', linestyle='none')
    #new_linear = np.polyfit(next_x, next_y, 1)
    #new_poly = np.poly1d(new_linear)
    #plot new regression
    #plt.plot(next_x, new_poly(next_x), color='red')

    # store the dataset as a csv file
    # x_pd = pd.Series(next_x)
    # y_pd = pd.Series(next_y)
    # data = pd.concat([x_pd, y_pd], axis=1)
    # data.columns = ['x axis', 'y axis']
    #path = '{}'.format(filepath)
    #file_out = pd.DataFrame.to_csv(data, path_or_buf=path, sep=',')

    #plot old linear regression
    #plt.plot(x_axis, y_coords, color='k')
    plt.show()

linear_generator(1, 50, 3, -10)
