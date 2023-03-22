import matplotlib.pyplot as plt
import charts
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

def run():  
  # read_csv
  data = read_csv('data.csv')
  #filter by continent
  result= list(filter(lambda item:item["Continent"] == "South America",data))
  #filter by conuntry
  labels= [item["CCA3"] for item in result]
  #filter by World population percentage
  values=[float(item["World Population Percentage"]) for item in result]
  
  return values,labels



if __name__ == '__main__':
  values,labels=run()
  charts.generate_bar_cart(labels,values)
  charts.generate_pie_char(labels,values)
