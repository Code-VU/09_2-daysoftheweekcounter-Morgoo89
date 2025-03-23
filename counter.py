def countDayOfTheWeek():
    # This first line is provided for you
    day_counts = dict()
    file_name = input("Enter a file name: ")
    try:
        file_hand = open(file_name)
    except:
        print('File cannot be opened:', file_name)
        exit()
        
    for line in file_hand:
        words = line.split()
        if len(words) < 3 or words[0] != 'From':
            continue
        else:
            if words[2] not in day_counts:
                day_counts[words[2]] = 1    #First entry
            else:
                day_counts[words[2]] += 1   #Additional entries
    print(day_counts)  
    
   
    



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
