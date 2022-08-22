from django.shortcuts import render

# rendering the html form
def form(request):
    return render(request, 'form.html')

# slicing operation
def result(request):
    
    """#fetching content of a text file
    result = request.POST['file']
    f = open(result, 'r')
    file_content = f.read()
    f.close()"""
    
    #getting form data
    result = request.POST['dump']

    #split the ids separately
    listID = result.split("\r\n \r\n    ")

    #split individual attributes
    ids = []
    for id in listID:
        alone=id.split("\r\n")
        ids.append(alone)
    
    #altering the first attribute of all the IDs
    i=0
    for id in ids:
        #delete the excess lines at the initial of the list
        if(id.count("ruckus# show wlan all")>0):
            id.remove("ruckus# show wlan all")
        if(id.count("WLAN Service:")>0):
            id.remove("WLAN Service:")
        if(id.count("  ID:")>0):
            id.remove("  ID:")

        #add WLAN service id as attribute name
        idVal = id[0].rstrip(':')
        idVal = idVal.strip()
        id[0] = "WLAN Service ID = "+idVal

        #trim the space before the attribute
        for i in range (1,len(id)):
            id[i].strip()

    return render(request, 'result.html', {'dump':ids})