from firebase import firebase
import json
#example of sending and recieving data from firebase server


myDataBase = 'https://mydatabase-f7de1.firebaseio.com/'

#start fire base
firebase = firebase.FirebaseApplication(myDataBase,None)

#make some random data
data = {'a':1,'b':2,'c':3}

#encode as json
data_j = json.dumps(data)

#post to server (creates a new snapshot)
result = firebase.post('/fc_data/test',data_j)
print(result)
print('')

#gets all snapshots
result = firebase.get('/fc_data/test',None)
print(result)
print('')

#put on server specifying snapshot name
result = firebase.put('fc_data/test2','SnapShot1',json.dumps(data))
print(result)
print('')

#get specific snapshot
result = firebase.get('/fc_data/test2','SnapShot1')
print(result)
print('')
