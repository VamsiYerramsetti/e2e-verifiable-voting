import random

def generate_votes(num_voters=10000):          #upto 10000 votes (default if not given)
    candidates = ["A", "B", "C"]
    weights = [0.45, 0.35, 0.20]            #instead of random 

    votes = random.choices(candidates, weights=weights, k=num_voters)
    return votes

if __name__ == "__main__":
    votes = generate_votes(20)
    print(votes)