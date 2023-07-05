# a,b,c = map(int,input().split())
# print((7-a)+(7-b)+(7-c))
# # elist = []
# # count = 0
# # for i in range(1,7):
# #     if a==i or b== i or c== i:
# #         continue
# #     else:
# #         elist.append(i)
# # for i in elist:
# #     count +=i
# # print(count)

# a = input()
# b= ""
# for i in range(len(a)):
#     if a[i]== "0":
#         b+="0"
#     elif a[i]=="1":
#         b+="1"
#     elif a[i] == "6":
#         b+="9"
#     elif a[i]=="9":
#         b+="6"
#     elif a[i]=="8":
#         b+="8"
# print(b[::-1])

# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = list(map(int,input().split()))
# count = 0
# for i in range(n):
#     for j in range(n):
#         k = c[j]
#         l = a[i]
#         m = b[len(b)-k]
#         # print(k,l,m)
#         if k == len(b):
#             if l == m:
#                 count += 1
#         else:
#             if l == b[k]:
#                 # print(b[k])
#                 count+=1
# print(count)