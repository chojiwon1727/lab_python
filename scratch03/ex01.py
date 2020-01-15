import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o')
plt.title('GDP')
plt.xlabel('year')
plt.ylabel('GDP(Billions of $)')


plt.savefig('../image_output/year_gdp.png')
plt.show()


movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

plt.bar(movies, num_oscars)
font_name = {'fontname': "Gulim"}
plt.title('아카데미 수상작', font_name)
plt.show()


grades = [93, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

from collections import Counter

histogram = Counter(min(x//10*10, 90) for x in grades)
print(histogram)

plt.bar(histogram.keys(), histogram.values())
plt.yticks([0,1,2,3,4,5])
plt.show()

plt.hist(grades)
plt.show()

mentions = [500, 505]
years = [2013, 2014]

plt.bar(years, mentions)
plt.xticks(years)
plt.show()




















