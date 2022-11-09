# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x):
    return x*3

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(x, y):
    return y-x

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
def dictionary_maker(input_list):
    map = {}
    for x in input_list:
        map[x[0]]=x[1]
    return map



############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#



#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.
def has_experience_as(input_list,job_title):
    list = []
    for temp in input_list:
        job_list = temp['jobs']
        for job in job_list:
            if job == job_title:
                list.append(temp['user'])
                break
    return list


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.
def job_counts(input_list):
    map = {}
    for temp in input_list:
        job_list = temp['jobs']
        for job in job_list:
            if job in map.keys():
                map[job] = map[job]+1
            else:
                map[job] = 1
    return map;


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
def most_popular_job(input_list):
    jon_name = ""
    job_num = 0
    job_map = job_counts(input_list)
    for item in job_map.items():
        if item[1] > job_num:
            job_num = item[1]
            jon_name = item[0]
    return jon_name,job_num


##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country
def total_registered_cases(raw_data,country_name):
    for item in raw_data.items():
        if item[0] == country_name:
            return sum(item[1])

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
def total_registered_cases_per_country(raw_data):
    map = {}
    for item in raw_data.items():
        map[item[0]] = sum(item[1])
    return map

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(raw_data):
    country = ""
    cases = 0
    for item in raw_data.items():
        if  sum(item[1]) > cases :
            cases = sum(item[1])
            country = item[0]
    return country,cases


###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
