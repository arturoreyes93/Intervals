#  File: Intervals.py

#  Description: reads a text file with interval numbers in strings and prints the non intersecting intervals

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 04/18

#  Date Last Modified: 04/19

def main():

	file = open('intervals.txt', 'r')

	intervals = []

	for line in file:

		intervals.append(line.split())

	file.close()

	for i in range(len(intervals)):

		intervals[i] = tuple([int(intervals[i][0]),int(intervals[i][1])])

	intervals.sort()

	non_intersecting = []

	for i in range(len(intervals)):

		if i != (len(intervals)-1):

			if intervals[i][1] >= intervals[i+1][0]:

				if intervals[i][1] <= intervals[i+1][1]:


					intervals[i+1] = tuple([intervals[i][0], intervals[i+1][1]])

				else:

					intervals[i+1] = intervals[i]

			else:

				non_intersecting.append(intervals[i])

		else:

			if intervals[i-1][1] >= intervals[i][0]:

				if intervals[i-1][1] <= intervals[i][1]:


					intervals[i] = tuple([intervals[i-1][0], intervals[i][1]])

				else:

					intervals[i] = intervals[i-1]

			non_intersecting.append(intervals[i])

	extra_credit = {}

	extra_credit_list = []

	for i in range(len(non_intersecting)):

		extra_credit[i] = (non_intersecting[i][1]-non_intersecting[i][0])

	import operator

	extra_credit = sorted(extra_credit.items(), key=operator.itemgetter(1))

	for i in extra_credit:

		extra_credit_list.append(non_intersecting[i[0]])

	print('Non-intersecting Intervals:')

	for i in non_intersecting :

		print(i)

	print(' ')
	print('Non-intersecting Intervals in order of size:')

	for i in extra_credit_list:
		print(i)

main()