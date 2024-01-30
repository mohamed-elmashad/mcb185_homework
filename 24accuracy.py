# authors: Mo, Aidan

def accuracy(TP, FP, TN, FN):
	if TP < 0 or FP < 0 or TN < 0 or FN < 0:
		print("Invalid inputs!")

	# Calculate accuracy
	accuracy_numerator = TP + TN
	accuracy_denominator = TP + FN + TN + FP
	if accuracy_denominator > 0:
		accuracy = accuracy_numerator / accuracy_denominator
	else:
		accuracy = 0

	# Calculate F1
	precision = TP / (TP + FP) if TP + FP > 0 else 0
	recall = TP / (TP + FN) if TP + FN > 0 else 0
	f1_numerator = (2 * precision * recall)
	f1_denominator = (precision + recall)
	f1 = f1_numerator / f1_denominator if f1_denominator > 0 else 0

	print("accuracy: ", accuracy)
	print("f1: ", f1)
	return accuracy, f1

print("TP = 2, FP = 3, TN = 1, FN = 10")
print(accuracy(2, 3, 1, 10))

print("TP = 10, FP = 13, TN = 21, FN = 1")
print(accuracy(10, 13, 21, 1))

print("TP = 0, FP = 0, TN = 0, FN = 0")
print(accuracy(0, 0, 0, 0))