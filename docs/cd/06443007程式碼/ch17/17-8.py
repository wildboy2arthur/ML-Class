from imblearn.over_sampling import SMOTE

model_pl = make_pipeline(CountVectorizer(stop_words='english'), 
                         SMOTE(),
                         MultinomialNB())
model_pl.fit(X_train, y_train)
y_pred = model_pl.predict(X_test)
score = model_pl.score(X_test, y_test)
print('測試集的結果', score.round(3))
y_pred = model_pl.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print('綜合報告')
print(classification_report(y_test, y_pred))