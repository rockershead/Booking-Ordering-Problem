import sys
import math
import os




#assume we have parsed json data from the input and inserted these data into 3 different arrays;start,end and id/uid.from here on we work with these arrays

start=[3,1,3,2,3,2,1,1,3,3,3,3,1,1,3,3,1,3]
end=[1,3,1,2,1,3,3,1,3,2,3,2,1,3,2,2,3,3]
uid=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]



length=len(start)




#what we need to achieve is end[i]=start[i+1]=>so called best case scenario
#number_of_elements=len(start);
#each round must check number of events of end[i]=start[i+1].....and make sure that those number of events are lesser than the previous round


def numof_relocation():                 #function to count number of times relocation is needed.that means no of times end[i]!=start[i+1]
 num_relocation=0
 for t in range (0, (length-1)):
  if(end[t]!=start[t+1]):
   num_relocation=num_relocation+1
 
 return num_relocation

for i in range (0,(length-1)):        
 
 if(end[i]!=start[i+1]):             #checking each element from left to right and checking whether end[i]=start[i+1].if its not the same,look out for  elements in the start array(indicated by index j) that have the same value as end[i] and do the neccessary shifting elements
  for j in range (0,length):
   if(i!=j):                         #prevent checking with its own 'start' data
    if(end[i]==start[j]):
     start_firsthalf=[]             #initialize some temporary arrays for each iteration.
     end_firsthalf=[]
     uid_firsthalf=[]
     start_lasthalf=[]
     end_lasthalf=[]
     uid_lasthalf=[]
     original_start=[]
     original_end=[]
     original_uid=[]
     k=i                                #k and r are used to mark the respective indices in the array
     r=j
     for q in range(0,length):            #store the original sequence of numbers for this iteration of all the arrays temporarily      
      original_start.append(start[q])
      original_end.append(end[q])
      original_uid.append(uid[q])
     initial_numrelocation=numof_relocation()  #getting initial number of times end[i]!=start[i+1] 
     
     
     temp_start=start[r]                      #store the value temporarily before deletion
     temp_end=end[r]
     temp_uid=uid[r]
     
     del start[r]
     del end[r]
     del uid[r]
     
     
     if(k<r):
      for z in range(0,(k+1)):
       start_firsthalf.append(start[z])
       end_firsthalf.append(end[z])
       uid_firsthalf.append(uid[z])
      for s in range((k+1),(length-1)):            #insert back the deleted element.By doing so sequence has changed to ensure end[i]=start[i+1].
       start_lasthalf.append(start[s])
       end_lasthalf.append(end[s])
       uid_lasthalf.append(uid[s])
      start=start_firsthalf+[temp_start]+start_lasthalf           
      end=end_firsthalf+[temp_end]+end_lasthalf
      uid=uid_firsthalf+[temp_uid]+uid_lasthalf
      
      
      
      final_numrelocation=numof_relocation()             #getting final number of times end[i]!=start[i+1]
      
      if(final_numrelocation>initial_numrelocation):      #if number of relocations needed is more than the previous sequence, revert back to the previous original sequence
       start=original_start
       end=original_end
       uid=original_uid
       
       
      
      
      
     
     else:
      
      
      new_k=k-1
      for z in range(0,(new_k)+1):
       start_firsthalf.append(start[z])
       end_firsthalf.append(end[z])
       uid_firsthalf.append(uid[z])
      for s in range((new_k)+1,(length-1)):
       start_lasthalf.append(start[s])
       end_lasthalf.append(end[s])
       uid_lasthalf.append(uid[s])
      start=start_firsthalf+[temp_start]+start_lasthalf
      end=end_firsthalf+[temp_end]+end_lasthalf
      uid=uid_firsthalf+[temp_uid]+uid_lasthalf
      
      
      
      final_numrelocation=numof_relocation()
      
      if(final_numrelocation>initial_numrelocation):
       
       start=original_start
       end=original_end
       uid=original_uid
       
       
      
      
      
      
	  
     
   
   
 
#there is a possibilty that the last element in the end[] list has not undergone any check.Hence the following code is to ensure that the last element is checked. 



#this part involves ONLY checking the last element of the sequence(to see if end[length-1] equals any value in start array). If the last element shifts places, the new last element will be checked again.

for p in range (0,length):
 
 original_start2=[]                    #original***2 is needed to store original sequence.
 original_end2=[]
 original_uid2=[]
 
 for w in range(0,length):
  original_start2.append(start[w])
  original_end2.append(end[w])
  original_uid2.append(uid[w])    
 
 
 
 
 present_numrelocation=numof_relocation()
 for x in range (0,length):
  if((end[length-1])==start[x]):
   start_firsthalf=[]
   end_firsthalf=[]
   uid_firsthalf=[]

   start_lasthalf=[]
   end_lasthalf=[]
   uid_lasthalf=[]
   
   original_start=[]
   original_end=[]
   original_uid=[]
   
   k=x
   
   temp_start=start[length-1]
   temp_end=end[length-1]
   temp_uid=uid[length-1] 
   for q in range(0,length):
    original_start.append(start[q])
    original_end.append(end[q])
    original_uid.append(uid[q]) 
   del start[length-1]
   del end[length-1]
   del uid[length-1]
  
  
   for z in range(0,k):
    start_firsthalf.append(start[z])
    end_firsthalf.append(end[z])
    uid_firsthalf.append(uid[z])
   for s in range(k,(length-1)):
    start_lasthalf.append(start[s])
    end_lasthalf.append(end[s])
    uid_lasthalf.append(uid[s])
   start=start_firsthalf+[temp_start]+start_lasthalf
   end=end_firsthalf+[temp_end]+end_lasthalf
   uid=uid_firsthalf+[temp_uid]+uid_lasthalf
  
   final_numrelocation=numof_relocation()
   
   if(final_numrelocation>present_numrelocation):
    
    start=original_start
    end=original_end
    uid=original_uid
    
   
   
 if(start==original_start2):                    #means that the sequence did not change at all so stop checking
  break
   
   
 
  

print(start)
print(end)
print(uid)
print("Number of relocations now are "+str(numof_relocation()))	   

	
