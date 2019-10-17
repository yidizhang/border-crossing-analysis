# Border Crossing Analysis


To solve this problem, I first read in the data as a ordered_dictionary and tried iterating through the csv file to separate out the Border names, the dates, and the measures. Once then, I would try to establish a link betweeen the Border names, dates, and the measures via implementing several dictionary. Dictionaries are extremely useful because when looking up something inside a dictionary the time complexity is O(1). However, this did not work because iteravely updating a dictionary was tricky and it proved to be hard.

Next I tried implementing a stack to keep track of the valves for each border, date, and measure, but once again I ran into the issue of how to know when to update the stack if I changed either of those three cateogories. In addition, I would have to make 6000+ different stacks if I implemented this structure (for each border, date, and measure). This did not lead anywhere.

Hence, I arrived at my solution. I read in the csv file, and I sorted it (in a descending order) via Border, Date, and Measure and then I grouped the sorted list via these same 3 categories, so there would be a solid chunk of the same cateogies, but different values. This was essential because now all I had to do was aggregate these values and then calculate the average for each crossing!

Fun things I learned: iterating over Lists of Lists is (slightly) faster than iterating over a list of OrderedDictionaries! Itemgetter is faster than using a lambda function.

Moved all the helper function to the utils.py file in order to make things for clear and legible.
Pros and Cons

Pros of my methodology:

    Easy code to read, nothing very messy or hard to understand
    If instead of aggregating the valves of the crossings and you wanted to aggregate via the date, it's easy to implement and not much to change

Cons:

    Unfortunately because I sorted the list (the data read in the csv_file), my time complexity became O(n log(n)), which is both the best and worst case. And at one time I have two nested for-loops, so my overall time complexity for my main function is O(n^{2} + n log(n)) = O(n^{2}), which if scaled up to a LOT more elements would take too long. Although I tried to implement other data structures to prevent this from happening, I could not get them working. Hence, I opted to have something working than nothing at all. In order to avoid this for future iterations, I would use the Pandas libraries, which would avoid the need for sorting (though we would still need to use the groupby function which I think is O(n) time complexity). My space complexity was simply O(n).

How to run my work?

So the first step, is to run the run.sh bash file, which will call my border_crossing_statistics.py script. However, I have added in extra parameters:

YOU MUST SPECIFY THE INPUT AND OUTPUT FILE AS WELL AS THE ARGUMENTS THEMSELVES. I REPEAT SPECIFY THE INPUT AND OUTPUT. For example,

this will work: python3 src/border_crossing_statistics.py --input input/Border_Crossing_Entry_Data.csv --output output/report.csv

This will not work: python3 ./src/border_analytics.py ./input/Border_Crossing_Entry_data.csv ./output/report.csv

I did this because there is now a clear distinction between input and output.

Added in my own unit test cases to help debug and ran the test case provided!




