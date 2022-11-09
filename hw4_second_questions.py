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