## Welcome to the XR Python Development Challenge

#### Overview

Create a Python application that will read from 3 input files and use the data within to produce 2 output
files.

#### Constraints
* Code to be written for Python 2.7 or higher
* Code should only use built-in Python packages (and not use third-party packcages such as pandas)
* Deliverable should be a zip file containing project code, related files, and instructions for installing and executing the application
* While there is no specific guidance on the code, the resulting application should meet personal standards for a production-ready deployment 

#### Input Files

##### **Team Map**

* The Team Map file is a comma-separated text file where each line contains two values: an integer
uniquely identifying a team and the string name of the team. The unique id may be assumed to be positive. The
string team name is not quoted and may be assumed not to contain commas or non-ASCII characters. The file
does contain a header with the field names. An example file is as follows:

#### **Product Master**

* The Product Master file is a comma-separated text file where each line contains information about a
unique product. The fields of the file are as follows:
	- *ProductId* - an integer uniquely identifying the Product
	- *Name* - a string name for the Product
	- *Price* - a floating point price at which the Product is sold (per unit, not per lot)
	- *LotSize* - an integer representing how many of the product are sold in a single lot
The numerical fields may be assumed to be positive. The string fields are not quoted and may be assumed not
to contain commas or non-ASCII characters. The file does not contain a header. An example file is as follows:


#### **Sales**

* The Sales file is a comma-separated text file where each line contains information about a unique sale.
The fields of the file are as follows:
	- *SaleId* - an integer uniquely identifying the sale 
	- *ProductId* - an integer identifying the Product(matches the ProductId from the Product Master)
	- *TeamId* - an integer identifying the Sales Team (matches the TeamId from the Team Map)
	- *Quantity* - an integer representing how many lots of the product were sold 
	- *Discount* - a floating point discount percentage given on the sale (e.g. 2.5% discount as “2.50”)
All of the numerical fields may be assumed to be positive. The file does not contain a header with the field
names. An example file is as follows:

#### **Calculations**

* Sales calculations for the output reports should contain total gross revenues. Prices in the Product
Master are per unit, and Sales are given in lots. Gross revenue should not be reduced by the discounts.

#### **Output Files**

* **Team Report**
	- The Team Report file is a comma-separated text file where each line contains two values: the string
name of the sales team and the total gross revenue of their team’s sales. The file should contain a header with
the field names, and teams should be in descending order by their gross revenue. An example file is as follows:

* **Product Master**
	- The Product Report file is a comma-separated text file where each line summarizes the sales of a single
Product and contains four values as follows:
		- *Name* - name of the Product
		- *GrossRevenue* - gross revenue of the sales of the Product
		- *TotalUnits - total number of units sold in the product 
		- *DiscountCost* - total cost of all discounts provided on sales of the Product
The file should contain a header with the field names, and the products should be provided in descending order
of their gross revenue. An example file is as follows:




