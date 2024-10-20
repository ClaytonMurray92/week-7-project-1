def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
def median(numbers):
    if not numbers:
        return 0
    sortedNumbers = sorted(numbers)
    n = len(sortedNumbers)
    if n % 2 == 1:
        return sortedNumbers[n // 2]
    else:
        mid1 = sortedNumbers[n // 2 - 1]
        mid2 = sortedNumbers[n // 2]
        return (mid1 + mid2) / 2
def mode(numbers):
    if not numbers:
        return 0
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num,0) + 1
    maxCount = max(counts.values())
    modeList = [num for num, count in counts.items() if count == maxCount]
    if len(modeList) == 1:
        return modeList[0]
    return min(modeList)
def main():
    userInput = input("Enter the numbers separated by spaces: ")
    numbers = list(map(float, userInput.split()))
    if not numbers:
        print("No numbers entered!")
        return
    print(f"Numbers: {numbers}")
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print (f"Mode: {mode(numbers)}")
if __name__ == "__main__":
    main()
