# Surfs Up Weather Analysis

## Project Overview

The purpose of this project is to provide temperature statistics from the months of June and December in order to help invenstors decide if running a surf and ice cream shop in Oahu is sustainable year-round. The data is stored in a SQLite database and queried in order to be converted to a list and then into a dataframe in order to run summary statistics on temperature for the two months.

## Resources

- Data Sources: hawaii.sqlite
- Software: Software: Python 3.7.6, Pandas 1.3.4, Jupyter Notebook 6.4.5

## Results

- June has a mean temperature of aproximately 75° with a max of 85° and a minimum of 64° from 1700 data points

![June Stats](https://github.com/mein0819/Surfs_Up/blob/main/ReadMe_images/June_stats.png)

- December has a mean temperature of 71° with a max of 83° and a minimum of 56° from 1517 data points

![Dec Stats](https://github.com/mein0819/Surfs_Up/blob/main/ReadMe_images/Dec_stats.png)

- Both months have similar mean and min/max temperatures, and the standard deviations show that there is a wider range of 
  temperatures in December but there does not appear to be dramatic fluctuations for either month
  
## Summary

There is little fluctuation in temperature throughout the year in Oahu, with overall great surfing temperature in the 70's. Further analysis into precipitation and wind data could potentially show that an investment in Surf n' Shake at this location could prove to be successful. Expanding the queries to analyze more of what the weather is doing during the winter months as well will help solidify whether this a viable year-round business. 
