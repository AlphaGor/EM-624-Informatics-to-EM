# Author: Ashutosh Laxminarayan Gor

from math import pi
import pandas as pd
from bokeh.plotting import figure, show, output_file
import numpy as np
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

data = pd.read_csv('SSE_Faculty.csv')
data = data.replace(np.nan, 0)

course = data.groupby('Program')[['Load 19-20', 'Load 20-21', 'Load 21-22', 'Load 22-23']].sum()
print("\nNumber of courses per program per academic year:")
print(course)

print("\nAverage number of Courses per faculty per academic year:")
average = data
average['Average number of Courses'] = data[['Load 19-20', 'Load 20-21', 'Load 21-22', 'Load 22-23']].mean(axis=1)
average['2019-2020'] = data[['Load 19-20']].mean(axis=1)
average['2020-2021'] = data[['Load 20-21']].mean(axis=1)
average['2021-2022'] = data[['Load 21-22']].mean(axis=1)
average['2022-2023'] = data[['Load 22-23']].mean(axis=1)
print(average[['ID', '2019-2020', '2020-2021', '2021-2022', '2022-2023']])

underload_1920 = 0
overload_1920 = 0

for item in data['Balance 19-20']:
    if item > 0:
        overload_1920 += 1
    elif item < 0:
        underload_1920 += 1
print("\nDuring academic year 2019-2020:")
print('Number of underloaded faculty:', str(underload_1920))
print('Number of overloaded faculty:', str(overload_1920))

underload_2021 = 0
overload_2021 = 0

for item in data['Balance 20-21']:
    if item > 0:
        overload_2021 += 1
    elif item < 0:
        underload_2021 += 1
print("\nDuring academic year 2020-2021:")
print('Number of underloaded faculty:', str(underload_2021))
print('Number of overloaded faculty:', str(overload_2021))

underload_2122 = 0
overload_2122 = 0

for item in data['Balance 21-22']:
    if item > 0:
        overload_2122 += 1
    elif item < 0:
        underload_2122 += 1
print("\nDuring academic year 2021-2022:")
print('Number of underloaded faculty:', str(underload_2122))
print('Number of overloaded faculty:', str(overload_2122))

underload_2223 = 0
overload_2223 = 0

for item in data['Balance 22-23']:
    if item > 0:
        overload_2223 += 1
    elif item < 0:
        underload_2223 += 1
print("\nDuring academic year 2022-2023:")
print('Number of underloaded faculty:', str(underload_2223))
print('Number of overloaded faculty:', str(overload_2223))

# Bokeh Plots
# Line Plot 1
output_file(filename="Courses_per_program_per_academic_year.html")
course_list = course[['Load 19-20', 'Load 20-21', 'Load 21-22', 'Load 22-23']].values.tolist()


x = [2019, 2020, 2021, 2023]
y1 = course_list[0]
y2 = course_list[1]
y3 = course_list[2]

line_plot1 = figure(title="# of courses per program per academic year", x_axis_label="Years", y_axis_label="Courses")

line_plot1.line(x, y1, legend_label="EM", color="red", line_width=2)
line_plot1.line(x, y2, legend_label="SSW", color="green", line_width=2)
line_plot1.line(x, y3, legend_label="SYS", color="blue", line_width=2)

show(line_plot1)

# Bar Plot
output_file("avg_number_of_courses_per_faculty.html")
ID = list(average['ID'].astype(str))
avg = list(average['Average number of Courses'])

print(ID)
print(avg)
bar_plot = figure(x_range=ID, height=350, title="Average number of courses per faculty over the years",
                  toolbar_location=None, tools="")
bar_plot.vbar(x=ID, top=avg, width=0.9)

bar_plot.y_range.start = 0
xa, ya = bar_plot.axis
xa.axis_label = 'Faculty'
ya.axis_label = 'Number of Courses'

show(bar_plot)

# Line Plot 2
output_file("Underloaded_faculty_per_academic_year.html")

x = [2019, 2020, 2021, 2023]
y = [underload_1920, underload_2021, underload_2122, underload_2223]

p = figure(title="Number of underloaded faculty per academic year",
           x_axis_label="Years", y_axis_label="Number of Faculty")

p.line(x, y, legend_label="Years.", line_width=2)

show(p)

# Pie Chart
output_file("Courses_by_program_in_22-23.html")
pie_data = list(course['Load 22-23'])
x = {
    'EM': pie_data[0],
    'SSW': pie_data[1],
    'SYS': pie_data[2],
}

Courses = ['EM', 'SSW', 'SYS']
data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'Program'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]

pie_chart = figure(title="Courses by program in academic year'22-'23", tooltips="@Program: @value", x_range=(-0.5, 1.0))
pie_chart.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                line_color="white", fill_color='color', legend_group='Program', source=data)

pie_chart.axis.axis_label = None
pie_chart.axis.visible = False
pie_chart.grid.grid_line_color = None

show(pie_chart)

# Source:
# https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_1.html
# https://docs.bokeh.org/en/latest/docs/user_guide/basic/lines.html
# https://docs.bokeh.org/en/latest/docs/user_guide/basic/bars.html
# https://docs.bokeh.org/en/latest/docs/user_guide/topics/pie.html
# https://www.geeksforgeeks.org/python-bokeh-plotting-a-line-graph/
# https://towardsdatascience.com/data-grouping-in-python-d64f1203f8d3
# https://stackoverflow.com/questions/52905360/summing-multiple-row-values-of-various-columns-in-pandas
# https://stackoverflow.com/questions/26806054/how-to-use-lists-as-values-in-pandas-dataframe
