def arebalnced(expresion):
    stack=[]
    for char in expresion:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return False
    
            curent_char=stack.pop()
            
            if curent_char=="(":
                if char!=")":
                    return False        
            
            if curent_char=="{":
                if char!="}":
                    return False        
            
            if curent_char=="[":
                if char!="]":
                    return False        
    if stack:
        return False
    else:
        return True
Expression=input("Enter expression: ")   

if(arebalnced(Expression)):
    print("Balanced")
else:
    print("Not Balanced")            
