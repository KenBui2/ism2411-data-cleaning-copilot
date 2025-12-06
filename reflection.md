# Reflection

# What Copilot Generated
I used GitHub Copilot to help generate two of my functions: `load_data()` and `clean_column_names()`.  
To prompt Copilot, I wrote a short comment above each function explaining what the function should do.  
Copilot produced a reasonable starting point with the import statements and the basic structure.

# What I Modified
I modified Copilot's suggestions to better fit the assignment:

- I changed variable names to be more consistent.
- I simplified the column cleaning logic so that it used `.str.lower()`, `.str.strip()`, and `.str.replace()`.
- For the missing values function, Copilot originally suggested filling missing values with 0, but I changed it to `dropna()` because that made more sense for this dataset.
- I added comments explaining why each step mattered — something Copilot did not include.

These modifications ensured that the code followed good data-cleaning practices and matched the assignment requirements.

# What I Learned
I learned how important it is to clearly define cleaning rules before writing code.  
I also learned that Copilot is helpful for generating boilerplate code and function structure, but it does not always make the best cleaning decisions. For example, it tried to fill missing prices with 0, which would distort analysis.

The biggest takeaway was that **Copilot accelerates coding, but I still need to understand the logic well enough to correct or improve its output**.
