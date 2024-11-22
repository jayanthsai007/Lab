import matplotlib.pyplot as map
import numpy as poo
# simple line plots
a_ordinate = [1, 5, 9]
b_ordinate = [3, 5, 7]
'''map.plot(a_ordinate, b_ordinate)
map.xlabel('x axis')
map.ylabel('y label')
map.title('line plots')
map.show()'''
# simple scatter plot
'''map.scatter(a_ordinate, b_ordinate)
map.xlabel('x axis')
map.ylabel('y axis')
map.title('scatter plot')
map.show()'''
# histogram
'''data = poo.random.randn(3000)
map.hist(data, bins=10, color='crimson', edgecolor='black')
map.xlabel('a ordinate')
map.ylabel('b ordinate')
map.title('histogram')
map.show()'''
# boxplot
'''data = poo.random.normal(0, 4, 360)
map.boxplot(data)
map.title('boxplot')
map.show()'''
# colourbars
# Import the necessary libraries
# Use the 'classic' style for the plot
map.style.use('classic')

# Generate data
x = poo.linspace(0, 10, 1000)
I = poo.sin(x) * poo.cos(x[:, poo.newaxis])

# Create the plot
map.imshow(I, cmap='Dark2')
map.colorbar()
map.show()  # This line ensures the plot displays in non-notebook environments like VS Code
