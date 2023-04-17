Input1 = input('Please press 1 to begin\n')


new_balance = int(0)

while Input1 != '0':
  Input1 = input('\nPlease select what you would like to do.\nExit - 0\nCheck balance - 1\nDeposit - 2\nWithdraw - 3\nCreate Account - 4\nDelete Account - 5\nModify Account - 6\n')
  if Input1 == '1':
    print(f'\nYour balance is {new_balance}')
    
  if Input1 == '2':
    deposit_value = int(input('How much would you like do deposit'))
    new_balance = deposit_value + new_balance
    print(f'Your new balance is {new_balance}')
    
  if Input1 == '3':
    withdraw_value = int(input('\nHow much would you like to withdraw?\n'))
    if withdraw_value > new_balance:
      print('You do not have enough funds to withdraw this.\n')
    else:
      new_balance = new_balance - withdraw_value
      print(f'Your new balance is {new_balance}')
  #if Input1 == '4':
  
  #if Input1 == '5':
  
  #if Input1 == '6':
  
  

print('Goodbye')