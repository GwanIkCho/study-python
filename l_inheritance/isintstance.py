class A:
    pass

class B(A):
    pass


a = A()
b = B()

print(isinstance(a,A))
print(isinstance(b,B))
# 모든 자식의 타입은 부모의 타입이다.
print(isinstance(b,A))
# 부모는 절대 자식타입이 될수없다.
print(isinstance(a,B))