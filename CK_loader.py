import pickle

def load_data():    
    dataFile = open('data.pickle', 'rb')
    training_data, test_data = pickle.load(dataFile)
    return(training_data, test_data)

