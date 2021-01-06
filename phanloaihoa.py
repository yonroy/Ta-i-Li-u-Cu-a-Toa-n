from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
iris_X = iris.data # data (petal length, petal width, sepal length, sepal width)
iris_y = iris.target # label

print(type(iris_X))

a = [1,2,3]
print(type(a))

a = np.array(a)
print(type(a))

# shuffle by index
index = np.array([2,0,1])
a = a[index]
print(a)