import sys
import joblib

model = joblib.load('../model.sav')

l = list(sys.argv[1].split(','))
print('%.2f lakhs' % float(model.predict([l])))

