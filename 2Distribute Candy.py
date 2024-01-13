def distributeCandies(candyType):
    unique_candies = len(set(candyType))
    max_candies = len(candyType) // 2
    return min(unique_candies, max_candies)
candyType = [1,1,2,2,3,3]