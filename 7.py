# Input : a b c d , 4 , a b , c , c d , c

# Required skills: {a, b, c, d}
# Number of candidates: 4
# Candidate skills:
# Candidate 0 → {a, b}
# Candidate 1 → {c}
# Candidate 2 → {c, d}
# Candidate 3 → {c}

import sys
from itertools import combinations

def min_team_selection():
    # Step 1: Read input
    input_str = sys.stdin.read().strip()

    # Step 2: Parse the input
    parts = input_str.split(" , ")
    required_skills = set(parts[0].split())  # Convert required skills to a set
    num_candidates = int(parts[1])
    candidate_skills = [set(skills.split()) for skills in parts[2:]]  # Convert each candidate's skills to a set

    # Step 3: Try all possible team combinations
    for r in range(1, num_candidates + 1):  # Start from 1 person to N people
        for team in combinations(range(num_candidates), r):  # Get all possible teams of size r
            covered_skills = set()  # Track skills covered by this team
            
            for idx in team:
                covered_skills.update(candidate_skills[idx])  # Add skills of this candidate

            if covered_skills >= required_skills:  # Check if all required skills are covered
                print(" ".join(map(str, team)))  # Print the indices of the chosen candidates
                return  # Since we are looking for the smallest team, return immediately

    print("")  # If no valid team found, print an empty string



result = min_team_selection()
print("Result",result)