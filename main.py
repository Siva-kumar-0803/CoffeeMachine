MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

def calculate_price(user_choice):
  global total
  print('Please insert coins.')
  quater = int(input('How many quaters?: ')) * 0.25
  dime = int(input('How many dimes?: ')) * 0.10
  nickle =int(input('HOw many nickles?:')) * 0.05
  penny = int(input('How many pennies?: ')) * 0.01
  total = quater + dime + nickle + penny

def make_coffee(user_choice):
  global profit_money  
  if total >= MENU[user_choice]['cost']:
    profit_money = profit_money + MENU[user_choice]['cost'] 
    print(f'Here is your {user_choice}. Enjoy!')
    return_money = total - MENU[user_choice]['cost']
    if return_money > 0:
      print(f'Here is your change: ${return_money}')
  elif total < MENU[user_choice]['cost']:
    print('Sorry your money is not enough. Money refunded.')


def check_resources(user_choice):
  global show
  global check
  for i in resources.keys():
    if i == 'water':
        if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
            print('sorry,not enought water.')
            check = True
        else:
          resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    elif i =='milk':
        if i in  MENU[user_choice]:
            if resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
                print('sorry,not enough milk.')
                check = True
            else:
                resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
    elif i == 'coffee':
        if resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
            print('sorry,not enought coffee.')
            check = True
        else:
          resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]

machine_off = False
profit_money = 0
while not machine_off:

  user_choice = input('What would you like? (espresso/latte/cappuccino): ')
  if user_choice == 'espresso' or user_choice == 'latte' or  user_choice == 'cappuccino':
       total = 0
       check = False
       check_resources(user_choice)
       if not check:
           calculate_price(user_choice)
           make_coffee(user_choice)
  elif user_choice == 'report':
      for i,j in resources.items():
          print(i,":",j)   
      print('Money:',profit_money)               
  elif user_choice == 'off':
    machine_off = True
  else:
    print('Invalid Charcter')
