Troubleshooting and Debugging Techniques
========================================

Topics covered
--------------
- What is debugging
- Problem Solving Steps
- Understanding the Problem
  - Creating a Reproduction Case
  - Finding the Root Cause
  - Dealing with Intermitent Issues
- Understanding Slowness
    - >top command 
    - >iotop
    - >iftop
    - How Computer Use Resources
    - Possible Causes for Slowness
    - Slow Web Server
- Slow Code
    - Writing Efficient Code
    - Using the Right Data Structures
    - Expensive Loops
    - Parallelizing Operations
- Programs Crash
    - Internal Server Error
    - Accessing Invalid Memory
    - Unhandled Errors and Exceptions
    - Debugging a Segmentation Fault
    - Crashes in Complex Systems
    - Communication and Documentation During Incidents
- Postmortems
- Managing Computer Resources

Binary Searching a Problem
--------------------------

**What is binary search**

Linear search works but the longer the list, the longer it can take to search.

If the list is sorted, we can use an alternative algorithm for searching called binary search.

- It may take more time to sort an unsorted list to perform binary search
- It can still make sense to do it if we're going to search through it several times
- It doesn't make sense to sort the list and then use binary search to only find one element. In that case, using linear search is simpler and faster.

**Applying Binary Search in Troubleshooting**

In troubleshooting, we can apply bisecting to go through and test a long list of hypotheses. When doing this, the list of elements contains all the possible causes of the problem and we keep reducing the problem by half until only one option is left.

When using Git for version control, we can use a Git command called bisect. Bisect receives two points in time in the Git history and repeatedly lets us try the code at the middle point between them until we find the commit that caused the breakage.

**Finding Invalid Data**

wc command - counts characters, words, and lines in a file head command - prints the first lines in the file, and the tail command to print the last lines