

def time_we_need_in_a_day(to_do_list_of_a_day):
    sum_of_times = 0
    for index in range(0,len(to_do_list_of_a_day)):
        time = to_do_list_of_a_day[index][1]
        sum_of_times = sum_of_times + time
    return sum_of_times

def review_steps(s1,s2,s3,s4,s5,s6,s7,s8):
    step1 = s1
    step2 = s2
    step3 = s3
    step4 = s4
    step5 = s5
    step6 = s6
    step7 = s7
    step8 = s8
    return step1,step2, step3, step4, step5, step6, step7, step8
step1,step2, step3, step4, step5, step6, step7, step8 = review_steps(1,2,4,8,16,32,64,128)

def make_list_of_days(number_of_days):
    list_of_days = [[] for _ in range(number_of_days)]
    return list_of_days
list_of_days = make_list_of_days(300)

def add_new_task(task_description , estimated_time , input_day):
    index = (input_day)-1
    list_of_days[index+step1].append((task_description,estimated_time))
    list_of_days[index+step2].append(('review ' + task_description,int(estimated_time/2)))
    list_of_days[index+step3].append(('review ' + task_description,int(estimated_time/2)))
    list_of_days[index+step4].append(('review ' + task_description,int(estimated_time/2)))
    list_of_days[index+step5].append(('review ' + task_description,int(estimated_time/3)))
    list_of_days[index+step6].append(('review ' + task_description,int(estimated_time/3)))
    list_of_days[index+step7].append(('review ' + task_description,int(estimated_time/3)))
    list_of_days[index+step8].append(('review ' + task_description,int(estimated_time/3)))
    return list_of_days


# list of tasks
def headway_mainbook():
    list_of_headway_tasks = []
    for unit in range(1,13):
        for part in range(1,3):
            string = 'headway mainbook Unit ' + str(unit) + '   part ' + str(part)
            list_of_headway_tasks.append(string)
    return list_of_headway_tasks 
def headway_workbook():
    list_of_headwayworkbook_tasks = []
    for unit in range(1,13):
        for part in range(1,3):
            string = 'headway workbook Unit ' + str(unit) + '   part ' + str(part)
            list_of_headwayworkbook_tasks.append((string))
    return list_of_headwayworkbook_tasks
def english_grammar_in_use():
    list_of_EGIU_tasks = []
    for unit in range(1,101):
        string = 'English Grammar In Use Unit ' + str(unit)
        list_of_EGIU_tasks.append((string))
    return list_of_EGIU_tasks
def english_vocabulary_in_use():
    list_of_EVIU_tasks = []
    for unit in range(1,101):
        string = 'English Vocabulary In Use Unit ' + str(unit)
        list_of_EVIU_tasks.append((string))
    return list_of_EVIU_tasks
def mini_stories():
    list_of_mini_story_tasks = []
    for unit in range(1,60):
        string = 'Mini Story Unit ' + str(unit)
        list_of_mini_story_tasks.append((string))
    return list_of_mini_story_tasks
def effortless_english():
    list_of_effortless_english_tasks = []
    for unit in range(1,60):
        string = 'Effortless English Unit ' + str(unit)
        list_of_effortless_english_tasks.append((string))
    return list_of_effortless_english_tasks
def videos():
    list_of_videos = []
    for unit in range(1,101):
        string = 'Video number ' + str(unit)
        list_of_videos.append((string))
    return list_of_videos


max_time_per_day = 65
counter = 0
while counter <100:
    print (counter)

    # every period of the plan
    while time_we_need_in_a_day(list_of_days[counter]) > max_time_per_day:
        counter = counter +1

    if counter <13:
        list_of_days = add_new_task(headway_mainbook()[counter], 40 , counter)
    if counter <61:
        list_of_days = add_new_task(english_grammar_in_use()[counter], 30 , counter)
    if counter <60:
        list_of_days = add_new_task(mini_stories()[counter], 20 , counter)
    list_of_days[counter].append(('15 minute Shadow ',15))
    list_of_days[counter].append(('ANKI ',15))




    counter = counter + 1
    while time_we_need_in_a_day(list_of_days[counter]) > max_time_per_day:
        counter = counter +1
    print (counter)
    if counter <13:
        list_of_days = add_new_task(headway_mainbook()[counter], 40 , counter)
    if counter <61:
        list_of_days = add_new_task(english_grammar_in_use()[counter], 30 , counter)
    if counter <60:
        list_of_days = add_new_task(mini_stories()[counter], 20 , counter)
    list_of_days[counter].append(('15 minute Shadow ',15))
    list_of_days[counter].append(('ANKI ',15))
    



    counter = counter + 1
    while time_we_need_in_a_day(list_of_days[counter]) > max_time_per_day:
        counter = counter +1    
    print (counter)
    
    if counter <13:
        list_of_days = add_new_task(headway_workbook()[counter], 40 , counter)
    if counter <61: 
        list_of_days = add_new_task(english_grammar_in_use()[counter], 30 , counter)
    if counter <60:
        list_of_days = add_new_task(mini_stories()[counter], 20 , counter)
    list_of_days[counter].append(('15 minute Shadow ',15))
    list_of_days[counter].append(('ANKI ',15))
   
   


    counter = counter + 1
    while time_we_need_in_a_day(list_of_days[counter]) > max_time_per_day:
        counter = counter +1
    print (counter)

    if counter <13:
        list_of_days = add_new_task(headway_workbook()[counter], 40 , counter)
    if counter <61:
        list_of_days = add_new_task(english_grammar_in_use()[counter], 30 , counter)
    if counter <60:
        list_of_days = add_new_task(mini_stories()[counter], 20 , counter)
    list_of_days[counter].append(('15 minute Shadow ',15))
    list_of_days[counter].append(('ANKI ',15))




    counter = counter + 1
    while time_we_need_in_a_day(list_of_days[counter]) > max_time_per_day:
        counter = counter +1
    print (counter)
    if counter <61:
        list_of_days = add_new_task(mini_stories()[counter], 20 , counter)
    list_of_days[counter].append(('Video ',15))
    list_of_days[counter].append(('15 minute Shadow ',15))
    list_of_days[counter].append(('ANKI ',15))
    counter = counter + 1





###########################################show#######################################################
day = 1
for x in list_of_days:
    print("day  ", day)
    day = day + 1
    for y in x:
        print (y)

x = []
y = []

for day_counter in range(0,len(list_of_days)):
    print("day  ", day_counter)

    x.append(day_counter)
    y.append(time_we_need_in_a_day(list_of_days[day_counter]))

    print (time_we_need_in_a_day(list_of_days[day_counter]))




import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()


