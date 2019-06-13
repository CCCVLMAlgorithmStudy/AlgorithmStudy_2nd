def solution(routes):
    routes.sort() 
    
    count = 0
    camera = 0
    camNum = 1
    
    for i in routes:
        if count == 0: 
            camera = i[1]
        else:
            if i[0]>camera: 
                camera = i[1] 
                camNum += 1 
            elif i[1]<camera: 
                camera = i[1] 
        count+=1
        
    return camNum