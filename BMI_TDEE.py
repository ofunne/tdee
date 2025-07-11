

units = input("\nWould you like to input your measurements in imperial or metric? ").lower()

if units == "metric":

  def extract_digits(text):
    return int(''.join(ch for ch in text if ch.isdigit()))
  
  start_weight_input = input("\nPlease enter your starting weight in kilograms: ")
  start_weight = extract_digits(start_weight_input)

  height_input = input("\nPlease enter your height in centimeters: ")
  height = extract_digits(height_input)/100

  sex = input("\nPlease enter sex here ('male', 'female' or 'other'): ").lower()

  age_input = input("\nPlease enter your age in years: ")
  age = extract_digits(age_input)

  male_BMR = (10 * start_weight) + (6.25 * height * 100) - (5 * age) + 5
  female_BMR = (10 * start_weight) + (6.25 * height * 100) - (5 * age) + 161

  activity_level = input("""\nWhat is your activity level? Enter a letter:
                         a. Sedentary (office job)
                         b. Light (1-2 times/week)
                         c. Moderate (3-5 times/week)
                         d. Heavy (6-7 times/week)
                         e. Athlete (2 times/day)? """).lower()
  activity_level = activity_level[0]

  if start_weight < 20:
    print("Weight must be greater than 20kg")

  if height < 0.9:
    print("Height must be greater than 90cm")

  BMI = round(start_weight/(height**2), 2)
  low_ideal = round(18.5 * (height ** 2), 2)
  high_ideal = round(25 * (height ** 2), 2)

  if BMI < 18.5:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are underweight.")
  elif BMI >= 18.5 and BMI < 25:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are within the ideal weight range for your height.")
  elif BMI >= 25 and BMI < 30:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are overweight.")
  elif BMI >= 30 and BMI < 40:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are obese.")
  else:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are morbidly obese.")

  print("\nBased on BMI, your ideal weight range would be " + str(low_ideal) + "kg to " + str(high_ideal) + "kg.")

  if BMI < 18.5:
    print("\nYou would need to gain " + str(round((low_ideal - start_weight), 2)) + "kg to be within this range")
  elif BMI > 25:
    print("\nYou would need to lose " + str(round((start_weight - high_ideal), 2)) + "kg to be within this range")

  print("""\nPlease note that BMI is a screening tool, and it is not a perfect measure for everyone.
        \nIt does not account for factors like muscle mass, bone density, and age.
        \nA BMI outside of the \'normal\' range does not always mean someone is unhealthy, and vice versa.
        \nIt is important to consider other factors alongside BMI when assessing overall health.\n""")

  activity_multipliers = {
    "a": 1.2,
    "1": 1.2,
    "b": 1.375,
    "2": 1.375,
    "c": 1.55,
    "3": 1.55,
    "d": 1.725,
    "4": 1.725,
    "e": 1.9,
    "5": 1.9
  }
  
  if sex == "male":
    TDEE = male_BMR * activity_multipliers.get(activity_level, 0)
  elif sex == "female":
    TDEE = female_BMR * activity_multipliers.get(activity_level, 0)
  elif sex == "other":
    fem_TDEE = female_BMR * activity_multipliers.get(activity_level, 0)
    mal_TDEE = male_BMR * activity_multipliers.get(activity_level, 0)
  else:
    TDEE = ""

  if sex == "other":
    print("The best estimate for your TDEE is between " + str(fem_TDEE) + " and " + str(mal_TDEE) + " calories per day based on the Mifflin-St Jeor Formula, which is widely known to be the most accurate.\n")
    print("Scientists recommend eating up to 1000 calories above or below your TDEE for effective, sustainable weight gain or loss.\n\nThis should result in a gain or loss (respectively) of up to 1kg/week.\n")
  elif TDEE:
    print("The best estimate for your TDEE is " + str(TDEE) + " calories per day based on the Mifflin-St Jeor Formula, which is widely known to be the most accurate.\n")
    print("Scientists recommend eating up to 1000 calories above or below your TDEE for effective, sustainable weight gain or loss.\n\nThis should result in a gain or loss (respectively) of up to 1kg/week.\n")
  else:
    print("We were unable to determine your TDEE. Please start again.\n")


  if sex != "other" and TDEE != "":
    if_goal = input("Do you have a goal weight? ").lower()
  else:
    if_goal = "no"

  if if_goal == "yes":

    goal_weight_input = input("\nPlease enter your goal weight in kilograms: ")
    goal_weight = extract_digits(goal_weight_input)

    valid_choices = {"a", "b", "c", "d"}
    weekly_loss_rates = {
        "a": 0.25,
        "b": 0.5,
        "c": 0.75,
        "d": 1.0
    }

    while True:
      weekly_change = input("""\nHow much weight are you aiming to lose/gain per week? Enter a letter:
                              a. 0.25kg
                              b. 0.5kg
                              c. 0.75kg
                              d. 1kg?\n """).strip().lower()
      if weekly_change[0] in valid_choices:
          weekly_change = weekly_change[0]
          break
      else:
          print("Invalid input. Please enter a, b, c, or d.")

    rate = weekly_loss_rates[weekly_change]
    weight_diff = round(abs(start_weight - goal_weight), 2)

    if (BMI > 30 and start_weight < goal_weight) or (BMI < 18.5 and start_weight > goal_weight):
        print("\nWe were unable to determine a safe weight management plan. Please speak with a healthcare provider.\n")
    else:
        loss_time = weight_diff / rate
        daily_deficit = (7700 * rate) / 7
        calories = TDEE - daily_deficit if start_weight > goal_weight else TDEE + daily_deficit

        direction = "lose" if start_weight > goal_weight else "gain"

        print(f"\nYou want to {direction}: {weight_diff} kg.\n")
        print(f"At a rate of {rate} kg/week, this will take approximately {round(loss_time, 1)} weeks.\n")
        print(f"To do this, you should aim to eat around {round(calories)} calories per day.\n")

        print("Please note that these values are based purely on calculations, and that TDEE will vary from person to person based on a number of different factors.\n\nWe recommend recalulating your TDEE every few weeks based on weight changes, and adjusting for personal preference.")
        print("\nThank you for using this weight management tool!\n")

  else:
    print("Thank you for using this weight management tool!\n")

elif units == "imperial":

  def extract_digits(text):
    return int(''.join(ch for ch in text if ch.isdigit()))
  
  start_weight_input = input("\nPlease enter your starting weight in pounds: ")
  start_weight = extract_digits(start_weight_input)

  ft_input = input("\nPlease enter your height - feet (if you are 5ft7, enter '5'): ")
  ft = extract_digits(ft_input)

  inch_input = input("\nPlease enter your height - inches (if you are 5ft7, enter '7'): ")
  inch = extract_digits(inch_input)

  height = ((ft * 12) + inch)

  sex = input("\nPlease enter sex here ('male', 'female' or 'other'): ").lower()

  age_input = input("\nPlease enter your age in years: ")
  age = extract_digits(age_input)

  male_BMR = (10 * (start_weight * 0.45359237)) + (6.25 * height * 2.54) - (5 * age) + 5
  female_BMR = (10 * (start_weight * 0.45359237)) + (6.25 * height * 2.54) - (5 * age) + 161

  activity_level = input("""\nWhat is your activity level? Enter a letter:
                         a. Sedentary (office job)
                         b. Light (1-2 times/week)
                         c. Moderate (3-5 times/week)
                         d. Heavy (6-7 times/week)
                         e. Athlete (2 times/day)? """).lower()
  activity_level = activity_level[0]

  if start_weight < 40:
    print("Weight must be greater than 40lbs")

  if height < 36:
    print("Height must be greater than 3'")

  BMI = round((start_weight*703)/(height**2), 2)
  low_ideal = round((18.5 * (height ** 2))/703, 2)
  high_ideal = round((25 * (height ** 2))/703, 2)


  if BMI < 18.5:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are underweight.")
  elif BMI >= 18.5 and BMI < 25:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are within the ideal weight range for your height.")
  elif BMI >= 25 and BMI < 30:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are overweight.")
  elif BMI >= 30 and BMI < 40:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are obese.")
  else:
    print("\nYour BMI is " + str(BMI) + ". This suggests that you are morbidly obese.")

  print("\nBased on BMI, your ideal weight range would be " + str(low_ideal) + "lbs to " + str(high_ideal) + "lbs.")

  if BMI < 18.5:
    print("\nYou would need to gain " + str(round((low_ideal - start_weight), 2)) + "lbs to be within this range")
  elif BMI > 25:
    print("\nYou would need to lose " + str(round((start_weight - high_ideal), 2)) + "lbs to be within this range")

  print("""\nPlease note that BMI is a screening tool, and it is not a perfect measure for everyone.
        \nIt does not account for factors like muscle mass, bone density, and age.
        \nA BMI outside of the \'normal\' range does not always mean someone is unhealthy, and vice versa.
        \nIt is important to consider other factors alongside BMI when assessing overall health.\n""")

  activity_multipliers = {
    "a": 1.2,
    "1": 1.2,
    "b": 1.375,
    "2": 1.375,
    "c": 1.55,
    "3": 1.55,
    "d": 1.725,
    "4": 1.725,
    "e": 1.9,
    "5": 1.9
  }
  
  if sex == "male":
    TDEE = male_BMR * activity_multipliers.get(activity_level, 0)
  elif sex == "female":
    TDEE = female_BMR * activity_multipliers.get(activity_level, 0)
  elif sex == "other":
    fem_TDEE = female_BMR * activity_multipliers.get(activity_level, 0)
    mal_TDEE = male_BMR * activity_multipliers.get(activity_level, 0)
  else:
    TDEE = ""

  if sex == "other":
    print("The best estimate for your TDEE is between " + str(fem_TDEE) + " and " + str(mal_TDEE) + " calories per day based on the Mifflin-St Jeor Formula, which is widely known to be the most accurate.\n")
    print("Scientists recommend eating up to 1000 calories above or below your TDEE for effective, sustainable weight gain or loss.\n\nThis should result in a gain or loss (respectively) of up to 2lbs/week.\n")
  elif TDEE:
    print("The best estimate for your TDEE is " + str(TDEE) + " calories per day based on the Mifflin-St Jeor Formula, which is widely known to be the most accurate.\n")
    print("Scientists recommend eating up to 1000 calories above or below your TDEE for effective, sustainable weight gain or loss.\n\nThis should result in a gain or loss (respectively) of up to 2lbs/week.\n")
  else:
    print("We were unable to determine your TDEE.\n")


  if sex != "other" and TDEE != "":
    if_goal = input("Do you have a goal weight? ").lower()
  else:
    if_goal = "no"

  if if_goal == "yes":

    goal_weight_input = input("\nPlease enter your goal weight in pounds: ")
    goal_weight = extract_digits(goal_weight_input)

    valid_choices = {"a", "b", "c", "d"}
    weekly_loss_rates = {
        "a": 0.5,
        "b": 1,
        "c": 1.5,
        "d": 2
    }

    while True:
      weekly_change = input("""\nHow much weight are you aiming to lose/gain per week? Enter a letter:
                              a. 0.5lbs
                              b. 1lb
                              c. 1.5lbs
                              d. 2lbs?\n """).strip().lower()
      if weekly_change[0] in valid_choices:
          weekly_change = weekly_change[0]
          break
      else:
          print("Invalid input. Please enter a, b, c, or d.")

    rate = weekly_loss_rates[weekly_change]
    weight_diff = round(abs(start_weight - goal_weight), 2)

    if (BMI > 30 and start_weight < goal_weight) or (BMI < 18.5 and start_weight > goal_weight):
        print("\nWe were unable to determine a safe weight management plan. Please speak with a healthcare provider.\n")
    else:
        loss_time = weight_diff / rate
        daily_deficit = (3500 * rate) / 7
        calories = TDEE - daily_deficit if start_weight > goal_weight else TDEE + daily_deficit

        direction = "lose" if start_weight > goal_weight else "gain"
        pound_s = "lb" if rate == 1 else "lbs"

        print(f"\nYou want to {direction}: {weight_diff} lbs.\n")
        print(f"At a rate of {rate} {pound_s}/week, this will take approximately {round(loss_time, 1)} weeks.\n")
        print(f"To do this, you should aim to eat around {round(calories)} calories per day.\n")

        print("Please note that these values are based purely on calculations, and that TDEE will vary from person to person based on a number of different factors.\n\nWe recommend recalulating your TDEE every few weeks based on weight changes, and adjusting for personal preference.")
        print("\nThank you for using this weight management tool!\n")
        
  else:
    print("Thank you for using this weight management tool!\n")

else:
  print("\nError: units not recognised. Please start again.")