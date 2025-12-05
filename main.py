from sklearn.datasets import load_wine
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
import matplotlib as plt


wine = load_wine()
x,y = wine.data, wine.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.80, test_size=0.20, random_state= 1, shuffle=True)

clf = tree.DecisionTreeClassifier(max_depth=2)
clf = clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

tree.plot_tree(clf)

rules = export_text(clf, feature_names=wine.feature_names)
print(rules)

plt.pyplot.show()