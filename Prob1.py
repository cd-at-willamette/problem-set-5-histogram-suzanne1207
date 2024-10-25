from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    HISTOGRAM = [0,1,2,3,4,5,6,7,8,9]
    for i in HISTOGRAM: # examines each number in the HISTOGRAM list
        count = 0 # sets count to zero each time so it's specific to each number
        if i in PI_DIGITS: # if the number is in pi
            for j in PI_DIGITS: # examines each number in pi
                if j == i: # if number in pi is in histogram
                    count += 1 # adds one to the count for that number
        else: # if the number is not in pi,
            count = 0 # count stays at zero
        HISTOGRAM[i] = count # replaces the number with its count
    print(HISTOGRAM) # prints the HISTOGRAM list
         


#1b
def print_histogram(hist:list[int]) -> None:
    pass

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    pass

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
#print_histogram(hist) # uncomment to test
#graph_histogram(hist, 400, 400) # uncomment to test

