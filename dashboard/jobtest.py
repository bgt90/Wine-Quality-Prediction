import joblib

model=joblib.load('modelAdmission')

print(model.predict([[337,118,4,4.5,4.5,9.65,1]])[0])
