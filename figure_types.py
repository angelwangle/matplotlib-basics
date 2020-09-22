from matplotlib.pylot import *

# some simple data
x = [1, 2, 3, 4]
y = [5, 4, 3, 2]

# create a new figure
figure()

# divide subplots into 2*3 grid and select #1
subplot(231)
plot(x, y)

# select #2
subplot(232)
bar(x, y)

# horizontal bar-charts
subplot(233)
barh(x, y)

# create stacked bar charts
subplot(234)
barh(x, y)

# we need more data for stacked bar charts
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')

# box plot
subplot(235)
baxplot(x)

# scatter plot
subplot(236)
scatter(x, y)

show()



