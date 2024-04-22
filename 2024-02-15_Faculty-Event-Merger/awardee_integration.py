import pandas as pd
from rapidfuzz import fuzz

# Load data
awards_df = pd.read_excel("AllAwards.xlsx")
invites_df = pd.read_excel("FebInvites.xlsx")

# Standardize names
awards_df['PI Name'] = awards_df['PI Name'].str.strip()
awards_df['CoPIs & Other Key Personnel'] = awards_df['CoPIs & Other Key Personnel'].str.strip()
invites_df['PI Name'] = invites_df['PI Name'].str.strip()

# Initialize lists to store matched and unmatched names
matched_names = []

# Fuzzy matching for every name in the invites list
for name in invites_df['PI Name']:
    # Fuzzy matching for each name using partial ratio
    partial_ratio_scores = []
    
    # First, search in 'PI Name' column
    for award_name in awards_df['PI Name']:
        partial_ratio_scores.append((fuzz.partial_ratio(name, award_name), award_name))
    
    # If not found in 'PI Name' column, search in 'CoPIs & Other Key Personnel' column
    if all(score[0] == 0 for score in partial_ratio_scores):
        for award_name in awards_df['CoPIs & Other Key Personnel']:
            partial_ratio_scores.append((fuzz.partial_ratio(name, award_name), award_name))
    
    max_partial_ratio = max(partial_ratio_scores, key=lambda x: x[0])
    
    # Select the maximum score between partial ratio and token sort ratio
    max_score = max_partial_ratio[0]
    
    if max_score >= 90:  # Adjust the threshold as needed
        matched_names.append(max_partial_ratio[1])  # Append the matched name

# Filter awards dataframe based on matched names
matching_awards_df = awards_df[(awards_df['PI Name'].isin(matched_names)) | 
                               (awards_df['CoPIs & Other Key Personnel'].isin(matched_names))]

# Sort by PI Name A-Z
matching_awards_df.sort_values(by='PI Name', inplace=True)

# Save to Excel
matching_awards_df.to_excel("matching_awards.xlsx", index=False)

# Print out matched names
print("Matched Names:")
print(matched_names)

# Print out names from invites that don't appear or have a similar appearance in the matched_names list
unmatched_names = set(invites_df['PI Name']) - set(matched_names)
print("\nUnmatched Names from Invites:")
print(unmatched_names)