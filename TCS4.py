def max_area_histogram(histogram):  
    stack = list()
    max_area = 0 
    index = 0
    while index < len(histogram):
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
        else: 
            top_of_stack = stack.pop() 
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index))
            max_area = max(max_area, area) 
    while stack: 
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index))
        max_area = max(max_area, area)
    return max_area 
  



g=int(input())
b,h=[int(x) for x in input().split()]
hist=[int(x) for x in input().split()]
volsum=sum(b*h*hist)
bigvol=(h*b*(max_area_histogram(hist)))
print(abs(volsum-bigvol))