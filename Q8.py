#Q8 

prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt B

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): 
# Prompt B assigns a clear ROLE ("You are a data 
# analyst") which sets the AI's perspective and tone from the start. This 
# helps the AI respond as a domain expert rather than as a generic assistant.

# Your answer (Reason 2): 
# Prompt B breaks the request into NUMBERED STEPS, 
# making it harder for the AI to miss any deliverable. In Prompt A, the 
# three asks (age groups, complaints, executive summary) are buried in one 
# long run-on sentence, so the AI might under-deliver on one of them.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: 
# Prompt A provides richer CONTEXT and BACKGROUND STORY 
# (3-month campaign, online survey, spreadsheet format, CEO presentation). 
# This human context helps the AI understand the stakes and the real-world 
# situation, which can lead to more relevant and empathetic suggestions.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer:

prompt_b_improved = """
Role: You are a data analyst helping a retail marketing team.

Background: We just finished a 3-month customer campaign. The marketing 
team collected feedback through an online survey, and we now have about 
500 responses in a spreadsheet. The findings will be presented to the 
CEO next Friday.

Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.

Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.

Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# What I borrowed: The "Background" section, which I took from Prompt A's 
# rich storytelling about the 3-month campaign, online survey, and 
# spreadsheet format.
#
# Why: Prompt B's structure is excellent for clarity, but it stripped 
# away useful context about the situation. Adding a Background section 
# gives the AI the "why" behind the task — it now understands this is a 
# post-campaign review feeding a CEO presentation, not just a generic 
# data exercise. This helps the AI calibrate the depth, tone, and 
# strategic framing of its analysis. The result is a prompt that keeps 
# Prompt B's structural clarity AND Prompt A's situational richness.