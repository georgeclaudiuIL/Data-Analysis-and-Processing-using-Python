
culori = ["alb", "rosu", "negru", "verde"]

def lungimea_5(cuvant):
    return len(cuvant) == 5

print(list(filter(lungimea_5, culori)))

print(list(filter(lambda x: len(x) == 4, culori)))