class Solution:
    # In: A list of strings
    # Out: A list of strings identical to the input
    # Con:
    # - We need an encode/decode algorithm that works for
    #    - all variations of 256 ASCII characters
    #    - a list of up to 100 words
    #    - each word being up to 200 characters

    # Alg 1: Concatenate
    # "Hello", "World" --> HelloWorld
    # How do we decode? Can't
    # Can't use an ASCII divider?

    # Alg 2: Use a breaker?
    # How do we do this?
    # Have a "breaker" symbol followed by a number 5#HELLO,
    
    # Encoding:
    # res = ""
    # For s in strs
    # len(s) + # + s

    # Decoding:
    # res = []
    # idx = num
    # While ptr < len(s)
    # 1. Get the number
    #    iterate until we see a breaker.
    # 2. Hit the breaker
    #    Stop iterating, grab the number.
    # 3. Get the string
    #    res.append(s[idx:idx+number])

    # 5#HELLO --> iterate until we see #
    # '5' num --> convert to int
    # res.append(s[0:0+5])

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s): # 5#HELLO
            # 1. Get the number
            #    iterate until we see a breaker.
            num_as_str = ""
            while s[idx] != "#":
                num_as_str = num_as_str + s[idx]
                idx += 1
            # 2. Hit the breaker
            #    Stop iterating, grab the number.
            len_str = int(num_as_str)
            idx += 1
            # 3. Get the string
            #    res.append(s[idx:idx+number])
            res.append(s[idx:idx+len_str])
            idx += len_str
        
        return res


