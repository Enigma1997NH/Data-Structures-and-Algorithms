# Time Complexity = O(n) ------My implementaion

def linear_search(arr1,element_search):
    
    position = -1
    for i in range(0,len(arr1)):
        if arr1[i] == element_search:
            position += 1
            print("Index of element is : ",i)
            break
        
    if(position == -1):
        print("Element not found")
        
arr1 = [3,5,1,2,16,90,4,0]
element_search = 4
linear_search(arr1,element_search)
'''

#Geeks for Geeks

def search(arr,search_element):
    left = 0
    length = len(arr)
    position = -1
    right = length - 1

    for left in range(0,right,1):
        if (arr[left] == search_element):
            print("left = ",left)
            position = left
            print("Element found in Array at",position +1,
                  "Position with",left+1,"attempt")
            break
        if (arr[right] == search_element):
            print("right = ",right)
            position = right
            print("Element found in Array at",position +1,
                  "Position with",length - right,"attempt")
            break
        left +=1
        right -=1

    if(position == -1):
        print("Not Found in Array",left,"Attempts")




        
arr = [10,20,30,40,5,60,55,12]
search_element = 30
search(arr,search_element)
'''
