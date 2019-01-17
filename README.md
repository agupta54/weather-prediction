# Weather Prediction

In this project I try to build a weather prediction tool in python to predict if ihe weather is *good* to go on a holiday to Fort Lauderdale. All data is collected from [here](https://climatecenter.fsu.edu/products-services/data). 

## Data Inspection 

A lot of discrepencies can arise in data. It is best to manually inspect it before building any models on it. In our data we have the year, month, day, precipitation, max. temperature, min temperature and mean temperature. Some first look observations just by going through the data - 

* The identification number for each day is an integer. 
* The year, month and day are all integers. 
* Precipitation and temperatures are float type and have five decimal places of accuracy. We cannot be sure about it though since we don't know as to how the observations were made. 
* To specify missing data in precipitation a value of -99.99000 is used. Good choice since this vaule cannnot be actually observed by the instrument. 
* Similarly missing values in temperature are reported as -99.90000. Since this temperature is very less likely to be observed in Florida. 
* The transition from missing to non-missing values occurs at Feb 1 1953.
* Even if the year is not leap Feb 29 is included in the data set by reporting missing values for that particular day. 
* We also observe that starting in November 1966 the data goes missing again untill 1998! 
* After looking through a lot of precipitation values we can see that it is reported till only two decimal places. 
* The min. and max. temperature are rounded off to integers. 
* The mean temperature are also always round numbers or end in .5 
* A closer inspection reveals that in fact it is the average of the min. and max. temperature. Thus in fact it is mid range temperature and mean temperature as stated in the data header! 
* Starting 2015 the mean temperature is not even reported in the data file. As stated earlier it could be easily calculted in the first place. 

A cursory inspection of the data by just opening in a text editor gives us so many useful insights. 

More details are presented in the ipython notebook. Once we are done exploring the data and deciding what model to use for prediction in the ipython notebook we can deploy our model using buy_tickets.py. predict_weather.py and tools.py contains similar code as in the ipython notebook but in a more modular form for deployment. Sample usage of the code is *python buy_tickets.py <year> <month> <day> <temperature>*.

```python
python buy_tickets.py 2013 8 23 92 
For year= 2013, month= 8, day= 23, temp= 92.0
predicted temperature is 90.1802339193452
Buy those tickets.
```

