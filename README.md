# k-means-from-scratch
This program reads numbers from a text file and prompts the user to enter the number of clusters (k).
First k numbers read from the text file are considered as the centroids of the clusters. After k points, each number 
is placed in a cluster whose centroid is closest. Then, the algorithm updates the locations of centroids of the k clusters.
All numbers are reassigned to updated clusters. This is repeated until convergence occurs, where numbers don't
change clusters anymore and centroids stabilize. Numbers in new clusters are printed out to a text file.
