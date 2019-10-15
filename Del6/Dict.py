import pickle


database = pickle.load(open('userData/database.p','rb'))

userName = raw_input('Please enter your name: ')
if userName in database:
	print('Welcome back ' + userName + '.')
else:
	database[userName] = {}
	print('Welcome ' + userName + '.')
print(database)

pickle.dump(database,open('userData/database.p','wb')) #First time

pickle.dump(database,open('userData/database.p','wb')) #Second time