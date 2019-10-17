# Border Crossing Analysis

This problem is fairly easy compared to the challenge I did three and four years ago. This is the third time I have applied for Insight Data Engingeer Program. Traditionally, people would use sql to perform this task. I used basic data structure list, set and dictionary. Some basic libraries were used, such as math, iterate tools. The main challenge is to really understand the input data. I thought data includes multiple different dates during each month and one would need to search through all these dates to find the sum, but clearly I was wrong. Sorting and organize the input data using column border, date, measure, value really make this take a lot easier, but it costs O(nlogn). The time complexity for my code is O(n^2) because of my nested for loop and space complexity is O(n). I have not used python for some time since I have main taught Java for past year, so please forgive the style of my coding. I had to spend some time checking to make sure the syntax is good. I did unit testing for each of functions I created.  


To run my code, please type the following in linux terminal:

python3 src/border_crossing_statistics.py --input input/Border_Crossing_Entry_Data.csv --output output/report.csv






