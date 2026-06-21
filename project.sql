#first creating a database
create database walmart_analysis;
USE walmart_analysis;

#Importing the dataset
SET GLOBAL local_infile = 1;
LOAD DATA LOCAL INFILE 'C:/walmart_cleaned.csv'
INTO TABLE walmart_analysis.walmart_cleaned
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#Checking if the data imported successfully
SELECT * FROM walmart_analysis.walmart_cleaned
LIMIT 10;

#Total sales
select sum(weekly_sales) as total_sales
from walmart_cleaned;

#Average Weekly sales
select avg(weekly_sales) as total_sales
from walmart_cleaned;

#Top 10 stores with high weekly sales
select store,
sum(weekly_sales) as total_sales
from walmart_cleaned
group by store
order by total_sales desc
limit 10;

# Stores with low weekly sales
select store,
sum(weekly_sales) as total_sales
from walmart_cleaned
group by store
order by total_sales 
limit 10;

#Sales by Department
select dept,
sum(weekly_sales) as total_sales
from walmart_cleaned
group by dept
order by total_sales desc
limit 10;

#Effect of Holidays on sales
select IsHoliday,
avg(weekly_sales) as avg_sales
from walmart_cleaned
group by IsHoliday;

#Counting Yearly Sales
SELECT YEAR(Date) AS year,
SUM(Weekly_Sales) AS yearly_sales
FROM walmart_cleaned
GROUP BY YEAR(Date)
ORDER BY YEAR(Date);

#Counting Monthly Sales
SELECT MONTH(Date) AS month,
SUM(Weekly_Sales) AS monthly_sales
FROM walmart_cleaned
GROUP BY MONTH(Date)
ORDER BY MONTH(Date);

#Top 10 high sales by Department and Store
select store,
dept,
sum(Weekly_sales) as sales
from walmart_cleaned
group by store, dept
order by sales desc
limit 10;

#Average Unemployement
select avg(Unemployment) as avg_unemployment
from walmart_cleaned;

#Average Fuel PRice
select avg(Fuel_Price) as avg_fuel
from walmart_cleaned;

#Average CPI
select avg(CPI) as avg_CPI
from walmart_cleaned;



