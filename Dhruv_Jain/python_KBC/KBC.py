a="a"
b="b"
c="c"
d="d"
questions=[
          ["who invented facebook ?","mark zuckerberg","mukesh ambani","bill gates","physics wallah",a], 
  
          ["which is best engineering college in world ?","IIT","MIT","JUET","NIT",c],
  
          ["which person landed on moon first ?","kalpana chawla","lord puneet","salman khan","neel arm strong",d],
  
          ["which is the most played game in india ?","football","cricket","hide n seek","snake n ladder",b]
  
          ]
level=[1000,2000,5000,10000]
reward=0
i=0
for i in range(0,len(questions)):
  que=questions[i]
  print(f"questions for RS {level[i]} is\n")
  print(f"Q{i+1}.{que[0]}")
  print(f"a.{que[1]}           b.{que[2]}")
  
  print(f"c.{que[3]}           d.{que[4]}")
  ans=input("enter the ans = ")
  if(ans==que[5]):
    print("correct answer")
    reward=reward+level[i]
    print(f"total reward={reward}.Rs\n\n")
  else:
    print("wrong answer")
    break
print(f"well played ! \n you won : {reward}.Rs")