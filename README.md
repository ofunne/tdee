## About the Project

### Description

This application was designed to assist users in managing their weight loss, maintenance, or gain. Users enter details such as their current weight, height, activity levels, and goal weight, and the application calculates their BMI, ideal weight range, TDEE, and other useful information.

### Built with

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![VSCode](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=fff)

### Features

<b>BMI Calculator:</b> Calculates the user's BMI based on their height and current weight.<br>

<b>TDEE Calculator:</b> Calculates the user's TDEE based on their current weight, height, age, sex, and activity levels.<br>

<b>Weight management plan:</b> Uses the user's goal weight input and desired weight loss/gain pace to give an estimated time frame and calorie deficit/surplus (respectively).<br>

### Prerequisites

- Basic knowledge of python.
- A code editor like VSCode

### Installation and Execution

1. Clone the repository to your local machine
```
git clone https://github.com/ofunne/tdee.git
```
2. Navigate to the cloned repository
```
cd tdee
```
3. Run the program
```
python main.py
```

### Other Features & Limitations

- Users can opt in/out of creating a weight management plan by responding "no" when asked if thei have a goal weight.
- The programme will not create a weight loss plan if the user's BMI already puts them within the "underweight" range.
- The programme will not create a weight gain plan if the user's BMI already puts them within (or beyond) the "obese" range.

### Contact me

Feel free to [pop me an email](mailto:ofunnemordi1@outlook.com).

### Useful Resources

- [Project Link](github.com/ofunne/tdee)
- [Weight Management Calculator](https://calculator-online.net/weightloss-calculator/)
