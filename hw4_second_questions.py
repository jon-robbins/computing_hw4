
# Now, imagine you are given data from a website that has people's CVs.
# The data comes as a list of dictionaries and each dictionary looks like this:
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}

# list of CVs = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]


############################### Question 4 ############################################

# Create a function called "has_experience_as" that has two parameters:
# 1. A list of CV's. ----  2. A string (job_title)
# The function should return a list of strings representing the usernames of every user that
# has worked as job_title.

def has_experience_as (cvs, job_title):
    list_has_experience = list()
    for cv in cvs:
        if job_title in cv.get('jobs'):
            list_has_experience.append(cv.get('user'))
        else:
            continue
    print("List of users having experience as {} is {}".format(job_title,list_has_experience))

    return(list_has_experience)

#has_experience_as([{'user': 'john', 'jobs': ['analyst', 'finance']},
#                   {'user': 'jane', 'jobs': ['finance', 'software']},
#                   {'user': 'sam', 'jobs': ['not_finance', 'software']}],
#                  'finance')




############################### Question 5 ############################################

# Create a function called "job_counts" that has one parameter: list of CV's
# and returns a dictionary where the keys are the job titles and the values
# are the number of users that have done that job.

def job_counts(cvs):
    dict_job_counts = dict()
    for cv in cvs:
        for job in cv.get('jobs'):
            if job in dict_job_counts:
                dict_job_counts[job] = dict_job_counts[job] + 1
            else:
                dict_job_counts[job] = 0
    print(dict_job_counts)
    return(dict_job_counts)

#job_counts([
#            {'user': 'john', 'jobs': ['analyst', 'finance']},
#            {'user': 'jane', 'jobs': ['finance', 'software']},
#            {'user': 'sam', 'jobs': ['not_finance', 'software']}
#
#            ])





############################### Question 6 ############################################

# Create a function, called "most_popular_job" that has one parameter: a list of CV's,
# and returns a tuple (str, int) that represents the title of the most popular job and the number
# of times it was held by people on the site.

def most_popular_job(cvs):
        sorted_list = (sorted(job_counts(cvs).items(), key=lambda item: item[1]))
        print("Sorted list of the key value pair of job_counts dictionary:",sorted_list)
        print("Maximum  job count among  the key value pair of job_counts dictionary:",sorted_list[-1])
        return(sorted_list[-1])




#most_popular_job(
#                [{'user': 'john', 'jobs': ['analyst', 'finance']},
#                {'user': 'jane', 'jobs': ['analyst', 'software']},
#                {'user': 'sam', 'jobs': ['analyst', 'software']}
#                ])



