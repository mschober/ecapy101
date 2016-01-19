
fruits = []

def add_fruit(a_fruit):
    fruits.append(a_fruit)

for f in "kiwi apple plum banana".split():
    add_fruit(f)


## Write a for loop to print the fruit and its color

#HINT - you can create an index by doing range(len(fruits))

#color = ['green', 'red', 'purple', 'yellow']
#
#for i in range(len(fruits)):
#    print "%s has color %s" % (fruits[i], color[i])


import csv
chores_list = {}

#with open('chores_list.csv') as chores:
#    rows = csv.DictReader(chores)
#    for row in rows:
#        for key, value in row.iteritems():
#            if key in chores_list:
#                chores_list[key].append(value)
#            else:
#                chores_list[key] = [value]

print chores_list
#for row in chores_dict:
#    print row['name'], row['chore_description'], row['hour_of_day'], row['day_of_week'], row['points_earned']
#
#print chores_dict['name']

#header=['name','chore_description','hour_of_day','day_of_week','points_earned']
with open('chores_list.csv') as chores:
    rows = csv.reader(chores)
    for row in rows:
        print row
