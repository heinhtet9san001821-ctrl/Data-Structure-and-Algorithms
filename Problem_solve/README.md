# 🚀 Python Problem Solving for Beginners

Welcome! This repository contains simple, beginner-friendly Python implementations for classic algorithmic problems like **Palindromes** and **Factorials**. 

---

## 📄 File Overview

### 1. 🔄 Palindrome Checker (Recursion) — `Palindrome.py`
This script checks if a string is a palindrome using a **recursive algorithm**.
* **How it works:** It continuously compares the first and last characters of the string.
* **Recursion mechanism:** The `check(str[1:-1])` function breaks the string down into smaller substrings by removing the verified outer characters until it confirms the match.

### 2. 📍 Palindrome Checker (Two-Pointers) — `Palindrome1.py`
This script solves the same palindrome problem but uses an efficient **two-pointer technique** instead of recursion.
* **How it works:** It uses two index variables: `l` (left pointer, starting at the beginning) and `r` (right pointer, starting at the end). It moves them toward the middle to compare characters step-by-step.
* > ⚠️ **Important Tip for Beginners:** Avoid using conditions like `while r != l` to control your loop. If the string has an even number of characters, the pointers will cross each other without ever being equal, causing an infinite loop. Use `while l < r` instead!

### 3. 🔢 Factorial Calculator (Recursion) — `factorial.py`
A straightforward guide to understanding how **recursion** works using factorials. When writing recursive functions, always remember the two structural requirements:
* **Base Case:** The crucial condition that stops the function from looping forever (ends the recursion).
* **Recursive Case:** The operation where the function calls itself to break the problem down into smaller parts.
* *Note: If you forget to define these cases properly, your code will encounter an infinite loop and crash with a stack overflow error.*

---

## 💬 Suggestions & Feedback

I am a learner open to suggestions, optimization ideas, and feedback! Please feel free to reach out or open a topic in the **Discussion Forum** if you have any questions.

* 🌐 **Language Support:** You can contact me in English or **Burmese language (မြန်မာဘာသာ)**.
