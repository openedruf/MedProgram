name = input('What is your name?')
surname = input('What is your surname?')
age = int(input('What is your age?'))
weight = int(input('What is your weight?'))

if (0 < age < 30) and (weight >= 50):
    print('Patient: ', name, surname, ', Age: ', age, ' , Weight: ', weight)
    print('The patient is in good condition. See you!')
elif (age >= 30) and (0 < weight < 50):
    print('Patient: ', name, surname, ', Age: ', age, ' , Weight: ', weight)
    print('The patient is in bad condition. Ask for a consultation.')
elif (age >= 30) and (weight >= 50):
    print('Patient: ', name, surname, ', Age: ', age, ' , Weight: ', weight)
    print('The patient is in good condition. See you!')
elif (0 < age < 30) and (0 < weight < 50):
    print('Patient: ', name, surname, ', Age: ', age, ' , Weight: ', weight)
    print('The patient is in bad condition. Ask for a consultation.')
else:
    print('Error. Try again.')
