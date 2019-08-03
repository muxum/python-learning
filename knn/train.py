import numpy as np
import matplotlib.pyplot as plt
import operator
#############################
###    build some data   ####
data_size_1 =100
data_size_2 =200
data_size_3 =300
data_size_all =data_size_1 + data_size_2 + data_size_3
np.random.seed(200)
x1_1 =np.random.normal(loc =5.0,scale =1.0,size =data_size_1)
x1_2 =np.random.normal(loc =7.0,scale =1.0,size =data_size_1)

x2_1 =np.random.normal(loc =7.0,scale =1.0,size =data_size_2)
x2_2 =np.random.normal(loc =4.0,scale =1.0,size =data_size_2)

x3_1 =np.random.normal(loc =10.0,scale =1.0,size =data_size_3)
x3_2 =np.random.normal(loc =7.0,scale =1.0,size =data_size_3)
'''
plt.scatter(x1_1,x1_2)
plt.show()
plt.scatter(x2_1,x2_2)
plt.show()
plt.scatter(x3_1,x3_2)
plt.show()
'''
#set the tips   ,y means tips here
y1 =[1 for _ in range(data_size_1)]
y2 =[2 for _ in range(data_size_2)]
y3 =[3 for _ in range(data_size_3)]
#concatenate data
x1 =np.concatenate((x1_1,x2_1,x3_1),axis =0)
x2 =np.concatenate((x1_2,x2_2,x3_2),axis =0)
x =np.hstack((x1.reshape(-1,1),x2.reshape(-1,1)))#turn 1D into 2D
y =np.concatenate((y1,y2,y3),axis =0)
'''
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()
'''
###        FINISH          ### 
##############################

##################################
### cut train_data & test_data ###
shuffled_index =np.random.permutation(data_size_all)
x = x[shuffled_index]
y = y[shuffled_index]

splited_index = int(data_size_all * 0.7)
x_train = x[: splited_index]
y_train =y[: splited_index]

x_test =x[splited_index:]
y_test =y[splited_index:]
'''
plt.scatter(x_train[:,0],x_train[:,1],c=y_train,marker ='x')
plt.show()
plt.scatter(x_test[:,0],x_test[:,1],c=y_test,marker ='*')
plt.show()
'''
#limit data between 0&1
x_train =(x_train - np.min(x_train,axis = 0))/(np.max(x_train,axis = 0)- np.min(x_train,axis = 0))
x_test =(x_test - np.min(x_test,axis = 0))/(np.max(x_test,axis = 0)- np.min(x_test,axis = 0))
###             FINISH          ###
###################################

####################
###  define KNN  ###
####################
class KNN(object):
    
    def _init_(self,k=3):
        self.k=k
        
    def train(self,x,y):
        self.x =x
        self.y =y
        
    def dist(self,v1,v2):
       return np.sum(np.abs(v1-v2))##L1 distance
   
    def vote(self,ys):
      vote_dict = {}
      for y in ys:
           if y not in vote_dict.keys():
               vote_dict[y] = 1
           else:
               vote_dict[y] += 1
      sorted_vote_dict = sorted(vote_dict.items(),key=operator.itemgetter(1),reverse=True)
      return sorted_vote_dict[0][0]
  
    def predict(self,x):
        Ypred = []
        for i in range(len(x)):
            dist_arr =[self.dist(x[i],self.x[j]) for j in range(len(x))]
            sorted_index = np.argsort(dist_arr)
            top_k = sorted_index[:3]
            Ypred.append(self.vote(ys = self.y[top_k]))
        return np.array(Ypred)
    
    def score(self,y_ture = None,Ypred =None):
        if y_ture is None or Ypred is None:
            Ypred = self.predict(self.x)
            y_ture = self.y
        scores = 0.0
        for i in range(len(y_ture)):
            if y_ture[i] == Ypred[i]:
                scores += 1
        scores /= len(y_ture)
        return scores
####################

#####################
        #BEGIN#
####################
#1
clf=KNN()
clf.train(x_train,y_train)
score_of_train = clf.score()
print('train accuracy: {:.3}'.format(score_of_train))
        
    
