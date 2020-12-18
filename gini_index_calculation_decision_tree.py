class DecisionTree:
    def __init__(self, data):
        self.data = data
    def _findBestSplit(self):
        num_of_features = len(self.data[0]) 
        #Assume that all inner lists have same length.
        #number of features includes label
        features = []
        #The following for loop below will return a list of lists 
        #where the first up to the second last list is the features of the data, 
        #each list representing a column of one feature.
        #The last list represents a single column of the labels.
        for i in range(num_of_features):
            y = [item[n] for item in aList for n in range(len(item)) if n == i] #Returns a list
            features.append(y)
        print(f"features == {features}")
        #the last list/column is the labels
        labels = features[-1]
        print()
        print()
        
        #Append each feature column to he corresponding label(zip them together)
        #as one in a list.
        #print zipped to see.
        zipped = []
        for i in range(num_of_features - 1): #4-1=3=> range(3) => 0,1,2
            tmp = []
            for i,j in zip(features[i], labels):
                tmp2 = []
                tmp2.append(i)
                tmp2.append(j) #[i,j]
                tmp.append(tmp2) #[[i,j],[i,j],[i,j],[i,j],[i,j],[i,j],[i,j]]
            zipped.append(tmp)
        print(zipped)
        print()
        print("Printing sorted zipped features")
        
        gini_index = float("inf")
        midpoint=0
        previous=0
        left = []
        right = []
        possible_labels = list(set(labels))
        print(f"possible_labels == {possible_labels}")
        
        for n_feature in zipped:
            print(n_feature)
            n_feature_sorted = sorted(first_feature_zipped_with_label,key=lambda x: x[0])
            print(n_feature_sorted)
            #Loop through the sorted list
           #take the items in the first index, find non-equal values and get midpoint between the two values
          #the get the proportions of the label on both sides of the midpoint
         #applying this to the Gini index equation:
        #
       #   gini_index_for_one_side_of_midpoint = 
      #             (1 - label_0_proportion^2 - label_1_proportion^2) x (proportion of items on this side of the midpoint)

 
            for i in range(len(n_feature_sorted)):
                print(n_feature_sorted[i][0])
                # If i is 0 then, we're at the first index and we have no previous item to compare to
                #so we only work with indices from here to 
                #get the midpoint
                if i > 0:
                    #if label at previous index is not equal to label at current index
                    if previous != n_feature_sorted[i][0]:
                        print(f"Comparing {previous} and {n_feature_sorted[i][0]} for equality")
                        
                        tally = [0] * (len(possible_labels))
                        
                        print(f"tally =={tally}")
                        left_prop = 0
                        right_prop = 0
                        proportion = 0
                        for j in range(len(n_feature_sorted)):
                            if j == i:
                                for x in tally:
                                    proportion += (x/i)**2
                                print(f"tally when j==i and i =={i} = {tally}")
                                left_prop = proportion
                                proportion = 0
                                tally = [0] * (len(possible_labels))
                            for n in range(len(possible_labels)):
                                if n_feature_sorted[j][1] == possible_labels[n]:
                                    tally[n] = tally[n] + 1
                                    break
                            #We now have tallies for all labels before the midpoint
                            #Now we can get the the proportions for these labels 
                        
                        for x in tally:
                            proportion += (x/(len(n_feature_sorted)-i))**2
                        right_prop = proportion
                        gini_index_after_midpoint = (1 - right_prop) * ((len(n_feature_sorted) - i) / (len(n_feature_sorted)))
                        print(f"gini_index_after_midpoint == {gini_index_after_midpoint}")
                        proportion = 0
                        tally = [0] * (len(possible_labels))
                        gini_index_before_midpoint = (1 - left_prop) * (i / (len(n_feature_sorted)))
                        print(f"gini_index_before_midpoint == {gini_index_before_midpoint}")
                        gini_sum = gini_index_before_midpoint + gini_index_after_midpoint
                        
                        if gini_index > gini_sum:
                            gini_index = gini_sum
                            print(f"gini_index whne gini_index > gini_sum ==> {gini_index}")
                            left = n_feature_sorted[0:i]
                            right = n_feature_sorted[i:]
                            midpoint = (previous + n_feature_sorted[i][0]) / 2                        
        
                previous = first_feature_sorted[i][0]
        return (gini_index, midpoint, left, right)                    
                
        
aList = [[1,0,2,0], [0,0,4,0], [10,1,17,1], [8,0,8,1], [3,1,12,0], [6,1,9,1], [0,0,0,1]]
aList2 =  [[1,0], [0,0], [10,1], [8,1], [3,0], [6,1], [0,1]]
decisionTree = DecisionTree(aList2)
(gini,mid,l,r) = decisionTree._findBestSplit()
print(f"gini == {gini}; midpoint == {mid}; left = {l}; right == {r}")
