from sklearn import tree

x = [[140, 1], [130, 1], [150, 0], [170, 0]]
y = [5, 5, 10, 10]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

print(clf.predict([[145, 0]]))