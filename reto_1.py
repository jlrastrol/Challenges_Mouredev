def isAnagrama(text1, text2):
    if(text1 == text2 or sorted(list(text1)) !=  sorted(list(text2))): return False
    return True

print(isAnagrama("texto", "txte"))
