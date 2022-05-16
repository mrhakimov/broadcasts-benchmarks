from datetime import datetime

epoch = datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def calc():
	f = open("/Users/mukkhakimov/Documents/itmo/thesis/logs.txt")
	data = f.read().split('\n')
	f.close()

	lstDate, lstTime = None, None
	strtDate, strtTime = None, None

	millis = []

	for line in data:
		# print(lstTime, strtTime)
		comps = line.split(' ')
		if len(comps) < 2 or comps[2].startswith("broadcast"):
			if len(comps) >= 2:
				if (not lstDate is None) and (not strtDate is None):
					lst = lstDate + ' ' + lstTime
					lstTm = datetime.strptime(lst, '%Y/%m/%d %H:%M:%S.%f')

					strt = strtDate + ' ' + strtTime
					strtTm = datetime.strptime(strt, '%Y/%m/%d %H:%M:%S.%f')

					# print(unix_time_millis(lstTm))
					# print(unix_time_millis(strtTm))

					# print(lst, strt)

					millis.append(unix_time_millis(lstTm) - unix_time_millis(strtTm))

				strtDate, strtTime = comps[:2]

		if len(comps) >= 2:
			lstDate, lstTime = comps[:2]

	def avg(lst):
		return sum(lst) / len(lst)

	# print(avg(millis))
	# print(min(millis))
	# print(max(millis))
	# print(millis)

	return (avg(millis), min(millis), max(millis))
