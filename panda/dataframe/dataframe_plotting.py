import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for this block of code to see what it does

# groupby() without as_index
if False:
    first_even = example_df.groupby('even').first()
    print (first_even)
    print (first_even['even']) # Causes an error. 'even' is no longer a column in the DataFrame
    
# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print (first_even)
    print (first_even['even']) # Now 'even' is still a column in the DataFrame

path = "C:\\Users\\gv01\\Desktop\\googleSync\\LEarning\\Udacity\\Data Scientists Foundation\\python\\Resources\\"
filename = 'nyc-subway-weather.csv'
subway_df = pd.read_csv(path+filename)

## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!

data_by_location = subway_df.groupby(['longitude','latitude'],as_index=False).mean() 
#as_index argument, picks the column which is now transformed to index/row because of group by operation
scaled_entries = (data_by_location['ENTRIESn_hourly']/data_by_location['ENTRIESn_hourly'].std())
plt.scatter(data_by_location['latitude'],data_by_location['longitude'],s=scaled_entries)
plt.show()