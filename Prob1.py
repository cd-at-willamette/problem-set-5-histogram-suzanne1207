from pgl import *
gw = GWindow(400, 400)

#1a
def create_histogram_array(pi):
    HISTOGRAM = [0,1,2,3,4,5,6,7,8,9]
    for i in HISTOGRAM: # examines each number in the HISTOGRAM list
        count = 0 # sets count to zero each time so it's specific to each number
        if i in pi: # if the number is in pi
            for j in pi: # examines each number in pi
                if j == i: # if number in pi is in histogram
                    count += 1 # adds one to the count for that number
        else: # if the number is not in pi,
            count = 0 # count stays at zero
        HISTOGRAM[i] = count # replaces the number with its count
    return HISTOGRAM
         
#1b
def print_histogram(hist):
    number = -1 # count starts at -1 so 1 can be added each time
    for i in hist: # for each value in the histogram list,
        asterisks = "*" * i # the asterisks are equal to i
        number += 1 # the number increases by one each time
        ASTERISKS = str(asterisks) # turns asterisks into a string
        NUMBER = str(number) # turns number into a string
        print(NUMBER + ": " + ASTERISKS) # prints histogram


#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    x = 0 # first x is zero
    for i in hist: # for each number in historam list,
        w = width / 10 # width is the gwindow width divided by 10 bars
        h = i * 100 # because height of window is 400, bar height must be multiplied by 100 so it's proportional
        y = height - h # sets y based on bar height
        color = "red" # sets color to red
        my_rect(x,y,w,h,color) # adds bar
        x += w # changes x so it increases by one bar width each time

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test

