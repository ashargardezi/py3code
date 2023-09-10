questions=[
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistani","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4],
    ["whic is capital of pakistan","karachi","lahore", "peshawar","islamabad","None",4]
    
    
    
    
    
    
    
    ]
print(len(questions))
levels=[1000,2000,30000,4000,5000,6000,7000,8000,9000,10000,14000,150000,160000,170000]
money=0
for i in range(len(questions)):
    question=questions[i]
    print(question)
    print(f"question for Rs {levels[i]}")
    print(f" a={question[1]},    b={question[2]},   c={question[3]},        d={question[4]}")
    reply=int(input("plese enter your Answer from 1-4"))
    if reply==question[-1]:
        print(f'you have won ,Rs{levels[i]}')
        if (i==4):
            money=10000
        elif(i==9):
                money=150000
        elif(i==14):
                money=170000
    else:
        print("wrong answer")
        break
print(f"your take home money is { money}")