import torch


x = torch.empty(1,1)
print(x)

y = torch.ones(2,2)
print(y)

z = torch.zeros(3,3)
print(z)

a = torch.add(x,x)

print(a)

print(y.add_(y))

b = torch.sub(y,y) # .mul() for multiplication ||  .div() for division
print(b)

x = torch.rand(5,3)
print(x)

print(x[1,1].item())

y = x.view(15)
print(y)