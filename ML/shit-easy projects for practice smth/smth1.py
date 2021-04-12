from sklearn.ensemble import RandomForestClassifier
# [height, weight, shoe size]
X = [[181, 80, 44], [170, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
    [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42],
    [181, 84, 43]]
Y = ["male", "female", "female", "female", "male", "male", "male", "female",
    "male", "female", "male"]

clf = RandomForestClassifier(1000)
clf = clf.fit(X, Y)
prediction = clf.predict([[182, 65, 45]])

print("prediction: " + str(prediction))

#Decision tree predicted "male" (TRUE)
#KNeigbors predicted "female" (FALSE)
#LogisticRegression predicted "male" (TRUE)
#RandomForestClassifier predicted "male" (TRUE)
