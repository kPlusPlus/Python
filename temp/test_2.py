class Apple:
    pass

class Orange:
    pass

𝐚 = 𝐀𝐩𝐩𝐥𝐞()
𝐛 = 𝐎𝐫𝐚𝐧𝐠𝐞()
𝐛 = 𝐚

𝐀 = 𝐭𝐲𝐩𝐞(𝐚)
𝐁 = 𝐭𝐲𝐩𝐞(𝐀𝐩𝐩𝐥𝐞)
𝐂 = 𝐭𝐲𝐩𝐞(𝐛)
𝐃 = 𝐭𝐲𝐩𝐞(𝐎𝐫𝐚𝐧𝐠𝐞)

print(B == A)
print(type(B) == type(D))
print(type(A))
print(B == C)