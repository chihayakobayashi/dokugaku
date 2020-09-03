w = input("単語を入力")
wb = input("もう一つ単語を入力")

def anagram(w,wb):
    w = w.lower()
    wb = wb.lower()
    return sorted(w) == sorted(wb)

print(anagram(w,wb))
