#!/usr/bin/env python3
import random
import re
import webbrowser
import time
import sys
import threading

# List of all 150 LeetCode questions
questions = [
    "Merge Sorted Array",
    "Remove Element",
    "Remove Duplicates from Sorted Array",
    "Remove Duplicates from Sorted Array II",
    "Majority Element",
    "Rotate Array",
    "Best Time to Buy and Sell Stock",
    "Best Time to Buy and Sell Stock II",
    "Jump Game",
    "Jump Game II",
    "H-Index",
    "Insert Delete GetRandom O(1)",
    "Product of Array Except Self",
    "Gas Station",
    "Candy",
    "Trapping Rain Water",
    "Roman to Integer",
    "Integer to Roman",
    "Length of Last Word",
    "Longest Common Prefix",
    "Reverse Words in a String",
    "Zigzag Conversion",
    "Find the Index of the First Occurrence in a String",
    "Text Justification",
    "Valid Palindrome",
    "Is Subsequence",
    "Two Sum II - Input Array Is Sorted",
    "Container With Most Water",
    "3Sum",
    "Minimum Size Subarray Sum",
    "Longest Substring Without Repeating Characters",
    "Substring with Concatenation of All Words",
    "Minimum Window Substring",
    "Valid Sudoku",
    "Spiral Matrix",
    "Rotate Image",
    "Set Matrix Zeroes",
    "Game of Life",
    "Ransom Note",
    "Isomorphic Strings",
    "Word Pattern",
    "Valid Anagram",
    "Group Anagrams",
    "Two Sum",
    "Happy Number",
    "Contains Duplicate II",
    "Longest Consecutive Sequence",
    "Summary Ranges",
    "Merge Intervals",
    "Insert Interval",
    "Minimum Number of Arrows to Burst Balloons",
    "Valid Parentheses",
    "Simplify Path",
    "Min Stack",
    "Evaluate Reverse Polish Notation",
    "Basic Calculator",
    "Linked List Cycle",
    "Add Two Numbers",
    "Merge Two Sorted Lists",
    "Copy List with Random Pointer",
    "Reverse Linked List II",
    "Reverse Nodes in k-Group",
    "Remove Nth Node From End of List",
    "Remove Duplicates from Sorted List II",
    "Rotate List",
    "Partition List",
    "LRU Cache",
    "Maximum Depth of Binary Tree",
    "Same Tree",
    "Invert Binary Tree",
    "Symmetric Tree",
    "Construct Binary Tree from Preorder and Inorder Traversal",
    "Construct Binary Tree from Inorder and Postorder Traversal",
    "Populating Next Right Pointers in Each Node II",
    "Flatten Binary Tree to Linked List",
    "Path Sum",
    "Sum Root to Leaf Numbers",
    "Binary Tree Maximum Path Sum",
    "Binary Search Tree Iterator",
    "Count Complete Tree Nodes",
    "Lowest Common Ancestor of a Binary Tree",
    "Binary Tree Right Side View",
    "Average of Levels in Binary Tree",
    "Binary Tree Level Order Traversal",
    "Binary Tree Zigzag Level Order Traversal",
    "Minimum Absolute Difference in BST",
    "Kth Smallest Element in a BST",
    "Validate Binary Search Tree",
    "Number of Islands",
    "Surrounded Regions",
    "Clone Graph",
    "Evaluate Division",
    "Course Schedule",
    "Course Schedule II",
    "Snakes and Ladders",
    "Minimum Genetic Mutation",
    "Word Ladder",
    "Implement Trie (Prefix Tree)",
    "Design Add and Search Words Data Structure",
    "Word Search II",
    "Letter Combinations of a Phone Number",
    "Combinations",
    "Permutations",
    "Combination Sum",
    "N-Queens II",
    "Generate Parentheses",
    "Word Search",
    "Convert Sorted Array to Binary Search Tree",
    "Sort List",
    "Construct Quad Tree",
    "Merge k Sorted Lists",
    "Maximum Subarray",
    "Maximum Sum Circular Subarray",
    "Search Insert Position",
    "Search a 2D Matrix",
    "Find Peak Element",
    "Search in Rotated Sorted Array",
    "Find First and Last Position of Element in Sorted Array",
    "Find Minimum in Rotated Sorted Array",
    "Median of Two Sorted Arrays",
    "Kth Largest Element in an Array",
    "IPO",
    "Find K Pairs with Smallest Sums",
    "Find Median from Data Stream",
    "Add Binary",
    "Reverse Bits",
    "Number of 1 Bits",
    "Single Number",
    "Single Number II",
    "Bitwise AND of Numbers Range",
    "Palindrome Number",
    "Plus One",
    "Factorial Trailing Zeroes",
    "Sqrt(x)",
    "Pow(x, n)",
    "Max Points on a Line",
    "Climbing Stairs",
    "House Robber",
    "Word Break",
    "Coin Change",
    "Longest Increasing Subsequence",
    "Triangle",
    "Minimum Path Sum",
    "Unique Paths II",
    "Longest Palindromic Substring",
    "Interleaving String",
    "Edit Distance",
    "Best Time to Buy and Sell Stock III",
    "Best Time to Buy and Sell Stock IV",
    "Maximal Square"
]

# Convert question names to LeetCode URLs
def to_url(question):
    # Convert the question name to a URL-friendly format
    url_name = question.lower().replace(' ', '-')
    # Remove any special characters except hyphen
    url_name = re.sub(r'[^a-z0-9-]', '', url_name)
    # Handle special cases like 3Sum
    url_name = re.sub(r'^(\d+)([a-z])', r'\1-\2', url_name)
    return f"https://leetcode.com/problems/{url_name}/description/"

def get_random_question():
    """Get a random question from the list."""
    question = random.choice(questions)
    return question, to_url(question)

def format_time(seconds):
    """Format seconds into minutes and seconds."""
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes} mins {seconds} secs"

def display_timer(stop_event):
    """Display a live timer in the console."""
    start_time = time.time()
    
    while not stop_event.is_set():
        elapsed = int(time.time() - start_time)
        # Simply print the time on a new line each update
        print(f"Time elapsed: {format_time(elapsed)}", end='\r')
        sys.stdout.flush()
        time.sleep(1)
    
    # Final time display
    elapsed = int(time.time() - start_time)
    print(f"\nTotal time: {format_time(elapsed)}")
    return elapsed

def main():
    print("LeetCode Top 150 Question Randomizer")
    print("-" * 40)
    
    while True:
        question, url = get_random_question()
        
        print("\nYour random question:")
        print("-" * 40)
        print(f"Question: {question}")
        print(f"URL: {url}")
        print("-" * 40)
        
        # Ask if user wants to open the link in browser
        open_link = input("Do you want to open this question in your browser? (y/n): ")
        if open_link.lower() == 'y':
            webbrowser.open(url)
            
            # Start the timer
            print("\nTimer started! Press Ctrl+C when you're done to see your total time.")
            stop_event = threading.Event()
            timer_thread = threading.Thread(target=display_timer, args=(stop_event,))
            timer_thread.daemon = True
            timer_thread.start()
            
            # Wait for keyboard interrupt
            try:
                # This keeps the main thread alive until interrupted
                while True:
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\nTimer stopped!")
                stop_event.set()
                timer_thread.join(1)  # Wait up to 1 second for thread to finish
        
        # Ask if user wants to continue
        continue_prompt = input("\nGet another question? (Enter to continue, 'q' to quit): ")
        if continue_prompt.lower() == 'q':
            break
        
        print("-" * 40)

if __name__ == "__main__":
    main() 