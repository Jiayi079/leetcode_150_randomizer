# LeetCode Top 150 Randomizer

A simple Python script to randomize LeetCode's Top 150 interview questions and track your solving time.

## Usage

Run the script with Python:

```bash
python randomize_leetcode.py
```

Or make it executable and run directly (Unix-like systems):

```bash
chmod +x randomize_leetcode.py
./randomize_leetcode.py
```

## Features

- Randomly selects one question at a time from LeetCode's Top 150 list
- Generates proper LeetCode URLs for each question
- Opens selected question in your web browser
- Built-in timer to track how long you spend solving the problem
- Simple command-line interface

## Example

```
LeetCode Top 150 Question Randomizer
----------------------------------------

Your random question:
----------------------------------------
Question: Two Sum
URL: https://leetcode.com/problems/two-sum/description/
----------------------------------------
Do you want to open this question in your browser? (y/n): y

Timer started! Press Ctrl+C when you're done to see your total time.
Time elapsed: 5 mins 23 secs

^C
Timer stopped!
Total time: 5 mins 23 secs

Get another question? (Enter to continue, 'q' to quit): 
----------------------------------------
```

## Instructions

1. When the script starts, it automatically selects a random question
2. Choose whether to open it in your browser with 'y' or 'n'
3. If you choose 'y', a timer will start automatically
4. Solve the problem and press Ctrl+C when you're done to stop the timer
5. Press Enter to get another random question or 'q' to quit