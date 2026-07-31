f1 = open("foo.txt", "w")

messageList = ["apples", "bananas", "cucumbers", 69, True, 2.71828]

messageList[:] = [str(x) + "\n" for x in messageList]

f1.writelines(messageList)
f1.close()
