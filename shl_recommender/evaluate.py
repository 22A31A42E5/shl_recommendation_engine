def apk(actual, predicted, k=3):
    if not actual:
        return 0.0

    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    return score / min(len(actual), k)


def mapk(actual_list, predicted_list, k=3):
    return sum(apk(a, p, k) for a, p in zip(actual_list, predicted_list)) / len(actual_list)


def recall_at_k(actual, predicted, k=3):
    predicted = predicted[:k]
    return len(set(predicted) & set(actual)) / float(len(actual))


def mean_recall_at_k(actual_list, predicted_list, k=3):
    return sum(recall_at_k(a, p, k) for a, p in zip(actual_list, predicted_list)) / len(actual_list)


# Sample data
actual = [["Java 8 (New)"], ["Business Communications"], ["Python 3"]]
predicted = [
    ["Java 8 (New)", "C#", "Visual Basic"],
    ["Business Communications", "Communication Skills", "HR Basics"],
    ["Python", "Java", "SQL"]
]

print("MAP@3:", mapk(actual, predicted, k=3))
print("Mean Recall@3:", mean_recall_at_k(actual, predicted, k=3))
