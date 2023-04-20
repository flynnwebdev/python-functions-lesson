def hello(name, age=21):
  print(f'Hello {name}, you are {age} years old!')

def get_answer(number):
  match number:
    case 1:
      print('It is certain')
    case 2:
      print('It is decidely so')
    case 3:
      print('Yes')
    case 4:
      print('Try again later')
    case 5:
      print('No')
    case 6:
      print('Very doubtful')
    case _:
      print('Not sure')


# main
# print('Start Main')
# hello(input('What is your name? '), age=50)
# print('End Main')
# import random
# get_answer(random.randint(1, 6))

# Add GST to an amount and return the result
def add_gst(amount):
  # Set local variable to the GST rate
  gst_rate = 0.1
  # Calculate amount plus GST
  amount_plus_gst = amount + (amount * gst_rate)  
  # Return from the function with a value
  return amount_plus_gst

# Read subtotal from user and convert to float
subtotal = float(input('Subtotal: $'))
# Call add_gst, passing the entered subtotal as an argument
# Store the returned result in a new variable called total
total = add_gst(subtotal)
# Print out the total
print(f'Total: ${total:.2f}')
