# this to demonstrate how youtube asses you region and age to see whether you are allowed to view that video

region_locked = False
age = 20

if age < 18 :
    print("access denied:you are too young to access this content")
elif region_locked:
    print("access denied: this video is not available for youur region")
else:
    print("access granted")


    videos = [ "magic match", "90 day fiance" , "tom and jerry"]

    for video in videos:
        print("now playing:",video)

count = 0

while count < 4 :
    print("buffering:" , count)

    count +=1

        

        