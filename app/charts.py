import matplotlib.pyplot as plt

def generate_bar_cart(labels,values):
  fig,ax=plt.subplots()
  ax.bar(labels,values)
  plt.savefig('bar.png')
  plt.close()

def generate_pie_char(labels,values):
  fig,ax =plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels=["a","b","c"]
  values=[30,40,60]
  generate_bar_cart(labels,values)