import random

def calculate_cdf(input_p):
  '''
  Takes a probability distribution input_p over the days of the week as input
  and returns the corresponding cumulative distribution function (CDF) as output.
  '''

  sorted_keys = ["08-12", "12-16", "16-20", "20-24"]

  output_dict = {"08-12":0, "12-16":0, "16-20":0, "20-24":0}
  output_dict["08-12"] = input_p["08-12"]

  for i in range(1,len(sorted_keys)):

    ###############################################################################
    ### Pseudocode:                                                             ###
    ### Get the current and the previous item's probability value from input_p  ###
    ##  Save it to the output_dict                                               ##
    ###############################################################################

  return output_dict


def one_trial(cdf):
  '''

  Takes the cumulative distribution function CDF as input, 
  generates a random number between 0 and 1,
  and returns the number of sunny-birthday according to the random number and cdf.

  '''
  sorted_keys = ["08-12", "12-16", "16-20", "20-24"]
  rand_number = random.uniform(0,1)

  for key in sorted_keys:
 
    ###############################################################################
    ### Pseudocode:                                                             ###
    ### Compare the random number and cdf[key] and return the key if the number ###
    ##  is smaller than or equal to that cdf value                               ##
    ###############################################################################
    

def simulate(cdf, num_trials=10000):

  '''
  Calls one_trial function num_trials times and returns the number of sunny-birthdays in all trials.
  '''
  count = 0

  for i in range(num_trials):

    hour = one_trial(cdf)
    condition = # ENTER CONDITION FOR THE POSITIVE OUTCOME (hour == ?)
    if condition:
      count += 1

  return count


input_p = {"08-12": 0.15, "12-16": 0.30, "16-20": 0.35, "20-24": 0.20}
num_trials = 100000

cdf = calculate_cdf(input_p)

print(cdf)
num = simulate(cdf, num_trials)
print("Number of visits: ", num, " in ", num_trials, " total visits.")

################################################################################################################# Question 2 ###################################
################################################################################
print("=====QUESTION 2======")

def is_route(source, routes):

  # Recursively checks routes for a route to routerZ

  '''
  Base case is when we have found routerZ 
  '''
  ###################################
  # Enter some code here:

  
  ###################################


  '''
  We iterate through the tuples. If we find *source*, we need to recursively investigate further by making *to* the next *source*. Also make sure you don't investigate the parts of *routes* that you have already processed(Hint: use slicing)
  '''
  for i,(fr, to) in enumerate(routes):
      ###################################
      # Enter some code here:
      pass
  
      ###################################

  '''
  If we searched through the list and didn't find any route:
  '''
  return False

# Test case 1
routes = [('routerA', 'routerM'), ('routerA', 'routerK'),('routerM', 'routerN'), ('routerN', 'routerO'), ('routerO', 'routerZ')]

print(is_route('routerA',routes)) # should print True

# Test case 2
routes = [('routerA', 'routerM'), ('routerA', 'routerK'),('routerN', 'routerO'), ('routerO', 'routerZ')]

print(is_route('routerA',routes)) # should print False