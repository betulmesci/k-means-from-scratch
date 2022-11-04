
#Get path of working directory
path = %pwd

#Path of the input file
input_file_path = path + '\\' + 'prog2-input-data.txt'

#Read input file's content and save numbers to file_content as floats
file_content = [float(i.rstrip()) for i in open(input_file_path)]
# Find each number's closest centroid:
def find_distance(centroids, numbers):
    '''
    DESCRIPTION:
        For a given set of numbers and centroids, this function
        assigns each number to the closest centroid.
    ----------
    Parameters
    ----------
    centroids : list
        List of centroids.
    numbers : list
        List of numbers.

    Returns
    -------
    centroids_numbers : dictionary
        A dictionary of clusters and numbers closest to those clusters.

    '''
    #Create dictionary that will hold cluster numbers and numbers 
    centroids_numbers = {}
    #Initialize the dictionary with cluster numbers (k) as keys 
    for centroid in range(len(centroids)):
        centroids_numbers[centroid] = []
    #Go through numbers list, for each number, calculate it's distance to 
    #each centroid, find the centroid it is closest to, update centroids_numbers
    #dictionary with this centroid and number.
    for number in numbers:
        dist_to_centroid = []
        
        for centroid in centroids:
            dist_to_centroid.append(abs(number-centroid))
            
        min_index = dist_to_centroid.index(min(dist_to_centroid))
        centroids_numbers[min_index].append(number) 
    return centroids_numbers

#Calculate mean of each cluster and update the centroid
def update_centroids(clust_dict):
    '''
    Description:
        This function takes in a dictionary whose content is the number of 
        clusters and points in each cluster. It calculates the mean value of 
        the points (new centroids) and returns a new dictionary with cluster 
        numbers and updated centroids.

    Parameters
    ----------
    clust_dict : dictionary
        This dictionary consists of the cluster numbers and old centroids.

    Returns
    -------
    updated_centroids : dictionary
        This dictionary consists of the cluster numbers and new centroids.

    '''
    updated_centroids = {}
    for k, v in clust_dict.items():
        updated_centroids[k] = round(sum(v)/len(v), 2)
    return updated_centroids

#Prompt the user to enter the number of clusters.
k = int(input("Enter the number of clusters: "))

#The first iteration selects first k numbers as the centroids
print("\nIteration 1")
#After kth point in the input file, assign each point to the nearest
#cluster. 
first_iteration = find_distance(file_content[:k], file_content[:])

#Print out assignments for the first iteration
for key, value in first_iteration.items():
    print(str(key) + ' ' + str(value))

#Update the centroids 
mean1 = update_centroids(first_iteration)

#The first iteration's centroids are assigned to "previous_centroids"
previous_centroids = list(mean1.values())

#To count iterations initialize n: number of iterations
n=1

#Rest of the iterations will be done in a while loop until
#centroids do not move any more
while True:
    #Increase count of iterations by one
    n += 1
    #Assign points in the file to clusters based on the updated centroids
    next_try = find_distance(previous_centroids, file_content[:])
    #Print out the results of the current iteration
    print("\nIteration " +str(n))
    for key, value in next_try.items():
        print(str(key) + ' ' + str(value))
    #Update the centroids for the next iteration
    next_mean = update_centroids(next_try)
    #Save updated centroids
    next_centroids = list(next_mean.values())
    #If updated centroids are the same as the previous one's, stop iterations 
    if sorted(previous_centroids) == sorted(next_centroids):
        break
    #If updated centroids are different, then they become the previous 
    #ones and iterations continue.
    else:
        previous_centroids = next_centroids

print()

#Initialize the list that will hold lines of the output file.
output_strings = []

#Go through the points, print out which cluster each point ended up in.
#Also save this string in the output_strings to be written into the output file 
#later on.
for i in range(len(file_content)):
            hold_key = 0
            for key, value in next_try.items():
                if file_content[i] in value:
                    hold_key = key
                    print("Point {} in cluster {}".format(str(file_content[i]),str(hold_key)))
                    output_strings.append("Point {} in cluster {}".format(str(file_content[i]),str(hold_key)))

#Specify the path of the output file
output_file_path = path + '\\' + 'prog2-output-data.txt'

#Open the output file in 'write' mode, write each line of output_strings 
#into the file. 
with open(output_file_path, 'w') as f:
    for string in output_strings:
        f.write(string)
        f.write('\n')