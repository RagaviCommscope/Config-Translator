from django.shortcuts import render

# rendering the html form
def form(request):
    return render(request, 'form.html')

# slicing operation
def result(request):
    
    """result = request.POST['file']
    f = open(result, 'r')
    file_content = f.read()
    f.close()"""
    
    result = request.POST['dump']
    listID = result.split("\r\n \r\n    ")
    ids = []
    for id in listID:
        alone=id.split("\r\n")
        ids.append(alone)
    return render(request, 'result.html', {'dump':ids})