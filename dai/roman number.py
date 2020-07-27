def find(s):
    values={'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    }
    n=len(s)
    ans=0
    previ=0
    for i in range(n-1,-1,-1):
        if values[s[i]]>=previ:
            ans+=values[s[i]]
        else:
            ans-=values[s[i]]
        previ=values[s[i]]
    return ans
s=input()
print(find(s))
