# Car-Resale-Value-Prediction

This is a small scale project which predicts the resale value of a car based upon several features like original price, kms driven, seller type, transition type, years used etc.  

### Display  
![Display](/Display/display.png)

### Technogies Used  
The sklearn.ensemble.RandomForestRegresser is used to train the model on a dataset from kaggle.  
For the website, nodejs and express frameworks are used.  

### Prerequisites  
python3 (or python for Windows - Read Rectifying Errors)  
node and npm  
sklearn, pandas and numpy

### Execute it on your machine  
Step 1: Download all the contents on this repo into your system  
Step 2: Open your terminal and change its location to project's directory (cd path/Car-Resale-Value-Prediction/)  
Step 3: Run "python3 price\_prediction.py" (python price\_prediction.py for Windows)  
Step 4: Change your directory to Website/ (cd Website/)  
Step 5: Run "npm start"  
Step 6: Go to your browser and open localhost:3000  
Step 7: Fill in the fields required and predict the value for your hypothetical car  

### Recitfying Errors  
#### Getting error from child_process on script.py  
This application was build on a Linux machine.  
If you are running it on a windows machine, you will have to change python3 to python in app.js:20.  
#### On clicking calculate, the application keeps on loading (waiting for localhost)  
Delete model.sav in the main folder and execute the python script price_prediction.py  
This will refresh the model that has been trained for predicting values (might take about 10-30 seconds)  
