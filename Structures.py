ue = ["Ireland", "Estonia", "Denmark", "Italy", "Slovenia"]
print(ue[3:3]) # writes empty tab - only "[]"
print(ue[-2]) # writes content of penultimate element (ue[3])  - Italy
print(ue[-6]) # error
print(ue[0:5]) # writes whole tab - ['Ireland', 'Estonia', 'Denmark', 'Italy', 'Slovenia']
print(ue[0:3], ue[3:5]) # writes separately two tabs - ['Ireland', 'Estonia', 'Denmark'] and ['Italy', 'Slovenia']
print(ue[3:-1]) # writes only the penultimate element
print(ue[-2:-4]) # writes empty tab - only []
print(ue[-4:-2]) # writes tab with two elements (ue[1] and ue[2]) - ['Estonia', 'Denmark']