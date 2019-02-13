from sklearn.metrics import jaccard_similarity_score

a=[0,1,3,5]
b=[2,1,5,5]

print(jaccard_similarity_score(a,b))
print(jaccard_similarity_score(a,b, normalize=False))
