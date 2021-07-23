# Python_practice-questions

**iPOD Inventory**

There is a company which has started selling the ipods ONLINE . But they want to sell these ipods online at the best price.
i) They have ipod Inventories in Brazil and Argentina. Each of the inventory can store only 100 ipods.
ii) iPods in Brazil are sold at 100$/unit and in Argentina they are sold at 50$/unit.
iii) after every order the stock at both brazil and argentina inventories are again back to 100 units.
iv) the no of transport ipods ordered should be only in multiple of 10.(i.e no of ipods ordered shouldn't be im number like 123 etc. )
v) the order placed should be either fulfilled completely or nothing
vi) if the order is placed like 120 ipods from brazil then the remaining ipods can be brought from the other inventory i.e.argentina. but here the shipping price of 400$ per 10 units is applied.
We have to select the best price solution.
Input - [Country] : [iPod required]
Output - [Best Price] : [Remaining iPod in Brazil] : [Remaining iPod in Argentina]
Examples
i) Brazil : 5
500 : 95 : 100
ii) Brazil : 50
4500 : 100 : 50
iii) Argentina : 120
7800 : 80 : 0
iv) Argentina : 250
Out of stock!!!!

**Sales Tax:**
Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.
When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), finishing with the total cost of the items, and the total amounts
of sales taxes paid. The rounding rules for sales tax are that for a tax rate of n%,
a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.
Write an application that prints out the receipt details for these shopping baskets?
Input 1:
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85
Input 2:
1 imported box of chocolates at 10.00
1 imported bottle of perfume at 47.50

**Hotel management:**

A well renowned hotel has three branches in miami. Namely x,y and z (Actually they gave names). Each has two types of customers. Regular and Rewardee. Also each branch has its own ratings x is given a 3 star rating while y has 5 star rating and z has 4 star rating. Each hotel has specific rates for weekends and weekdays. x charges $100 for regular customers on weekdays and $120 on weekends While it is $90 for rewardee on weekdays  and $60 on weekends. Similarly y charges $130 for regular customers on weekdays and $150 on weekends. While it's $100 for rewardee on weekdays and $95 on weekends. While z charges $195 for regular customers on weekdays and $150 on weekends. While it's $120 for rewardee on weekdays and $90 on weekends.
Now when the customer requests for a particular detail you need to find which hotel would yield the customer profit.
In case of tie between hotels compare the ratings and provide the result.
Input format: regular:16Mar2010(sun),19Mar2010(wed),21Mar2010(Fri)

**MARS ROVER**

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. 
          A rover's position and location is represented by a combination of x and y coordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
          In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

INPUT:

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

OUTPUT:
The output for each rover should be its final coordinates and heading.

INPUT AND OUTPUT:

Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Expected Output:
1 3 N
5 1 E


**Electricity Problem**

Given an integer U denoting the amount of KWh units of electricity consumed, the task is to calculate the electricity bill with the help of the below charges: 
 

1 to 100 units – Rs. 10/unit
100 to 200 units – Rs. 15/unit
200 to 300 units – Rs. 20/unit
above 300 units – Rs. 25/unit
Examples: 
 

Input: U = 250 
Output: 3500 
Explanation: 
Charge for the first 100 units – 10*100 = 1000 
Charge for the 100 to 200 units – 15*100 = 1500 
Charge for the 200 to 250 units – 20*50 = 1000 
Total Electricity Bill = 1000 + 1500 + 1000 = 3500





