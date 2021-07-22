class Cuts(object):
    def __init__(self):
        #Numbers given from company
        self.cuts = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}
    def __getitem__(self,key):
        return dict.__getitem__(self,key)
    #Adds or changes a key and value
    def __setitem__(self, key, value):
        value = int(value)
        if value < 0:
            raise ValueError('{v} cannot be negative'.format(v=value))
        dict.__setitem__(self,key,value)
    #Deletes key and value    
    def __delitem__(self, key):
        dict.__delitem__(self,key)
        
    def __iter__(self):
        return dict.__iter__(self)
    
    def __len__(self):
        return dict.__len__(self)
    
    def __contains__(self, x):
        return dict.__contains__(self,x)


# c = Cuts()
# #Examples that show CutsDic works
# #Gets amount wanted for 125" 
# print(c.cuts['125'])
# print(c.cuts)
# #Changes the amount for 125"
# c.cuts.__setitem__('125',9)
# print(c.cuts)
# #Adds on a new length with an amount wanted
# c.cuts.__setitem__('135',30)
# print(c.cuts)
# #Gets amount wanted for 108"
# print(c.cuts.__getitem__('108'))
# #Deletes the length that was just added
# c.cuts.__delitem__('135')
# print(c.cuts)
# #Sets 125" back to the oringinal amount
# c.cuts.__setitem__('125',10)
# print(c.cuts)
# print('')