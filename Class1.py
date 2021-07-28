import csv

with open("class1.csv", newline = "") as f :
    reader = csv.reader(f)
    fileData = list(reader)

#Removing header
fileData.pop(0)

#Mean
totalMarks = 0
totalStudents = len(fileData)

for i in fileData :
    totalMarks = totalMarks + float(i[1])

mean = totalMarks/totalStudents
print("Mean = " + str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")
figure = px.scatter(df, x = "Student Number", y = "Marks")
figure.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean, 
        y1 = mean,
        x0 = 0,
        x1 = totalStudents
    )
])

figure.update_yaxes(rangemode = "tozero")

figure.show()