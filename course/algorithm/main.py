# smallest value in the array.

def find_minimum(nums):
    if len(nums) == 0:
        return None
    min = float("inf")
    for num in nums:
        if num < min:
            min = num
    return min


# Add two number

def summation(nums):
    if len(nums) == 0:
        return 0
    summation = 0
    for num in nums:
        summation += num
    return summation

# get_estimated_spread social media problem.


def get_estimated_spread(audiences_followers):
    if len(audiences_followers) == 0:
        return 0
    sm = 0
    for num in audiences_followers:
        sm += num
    avg = sm / len(audiences_followers)
    return avg * (len(audiences_followers) ** 1.2)


def get_follower_prediction(follower_count, influencer_type, num_months):
    total = 0
    if influencer_type == "fitness":
        total += follower_count * 4**num_months
        return total
    elif influencer_type == "cosmetic":
        total += follower_count * 3**num_months
    else:
        total += follower_count*2**num_months
    return total

    # total = a1 × r^n
