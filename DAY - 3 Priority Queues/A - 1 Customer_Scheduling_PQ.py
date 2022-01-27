
import queue

if __name__ == '__main__':
    
    n = int(input())
    qq = queue.PriorityQueue(n)
    po = []
    for i in range(n):
        po.append([int(x) for x in input().split()])
        
    po.sort(key=lambda x: x[0], reverse=True)
    wtime = 0
    lo = po.pop()
    lo.append(lo[0] + lo[1])
    wtime += lo[2] - lo[0]
    
    time = lo[2]
    for i in range(n-1):
        
        while(po and time >= po[-1][0]): 
            node = po.pop()
            qq.put((node[1], node))
            
        if qq:
            dl = qq.get()[1]
            dl.append(time + dl[1])
            wtime += dl[2] - dl[0]
            lo = dl
        else:
            temp = po.pop()
            temp.append(temp[0] + temp[1])
            wtime += temp[2] - temp[0]
            lo = temp
    
        time = lo[2]
        
    print(int(wtime/n))
    
    