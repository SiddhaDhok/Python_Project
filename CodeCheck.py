def CheckIfHit(MajorList, hit_pos):
    if hit_pos in MajorList:
        print("Hit!")
        MajorList.remove(hit_pos)
    else:
        print("Miss")

MajorList=[[3,4], [8,9], [9,1], [1,2], [4,4], [5,6], [6,7], [1,1]]
hit_pos=[1,2]
CheckIfHit(MajorList, hit_pos)
print(MajorList)