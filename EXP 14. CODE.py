
# Decision Tree Implementation

# Dataset
data = [
    [1, 1, "Yes"],
    [1, 0, "Yes"],
    [0, 1, "No"],
    [0, 0, "No"]
]

# Decision Tree
def decision_tree(a):
    if a[0] == 1:
        return "Yes"
    else:
        return "No"

# Test the model
print("Decision Tree Prediction")

for row in data:
    prediction = decision_tree(row)
    print("Input:", row[0:2], "Prediction:", prediction)
