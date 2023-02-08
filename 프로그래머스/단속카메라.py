def solution(routes):
    answer = 1 
    for i in range(len(routes)):
        routes[i].sort()
    routes.sort(key = lambda x : (x[1]))
    camera_point = routes[0][1]
    for i in range(1,len(routes)):
        if routes[i][0] <= camera_point <= routes[i][1]:
            camera_point = min(camera_point, routes[i][1])
        else:
            camera_point = routes[i][1]
            answer += 1
    
    return answer