# 实例1
# import pickle
#
# data1={'a':[1,2,3,4,54],
#        'b':('string',u'Unicode string'),
#        'c':None}
#
# selfref_list = [1, 2, 3]
#
# selfref_list.append(selfref_list)
#
# output = open("data.pkl","wb")
#
# pickle.dump(data1,output)
#
# pickle.dump(selfref_list,output,-1)
#
# output.close()


import pprint,pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl','rb')

data1 = pickle.load(pkl_file)

pprint.pprint(data1)

data2 = pickle.load(pkl_file)

pprint.pprint(data2)

pkl_file.close()