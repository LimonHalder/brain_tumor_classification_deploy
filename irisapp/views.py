from django.shortcuts import render
from joblib import load
model=load(".\savedModels\model.joblib")

def prediction(request):
    if request.method =='POST':
        sepal_length=request.POST['sepal_length']
        sepal_width=request.POST['sepal_width']
        petal_lenght=request.POST['petal_length']
        petal_width=request.POST['petal_width']
        y_pred=model.predict([[sepal_length,sepal_width,petal_lenght,petal_width]])
        
        if y_pred[0]==0:
            y_pred="Setosa"

        elif  y_pred[0]==1:
            y_pred="Verscicolor"
        else:
            y_pred='Virginica'



        return render(request, "main.html",{'result':y_pred})
    return render(request,'main.html' )

def result(request):
    sepal_length=request.GET['sepal_length']
    sepal_width=request.GET['sepal_width']
    petal_lenght=request.GET['petal_length']
    petal_width=request.GET['petal_width']
    y_pred=model.predict([[sepal_length,sepal_width,petal_lenght,petal_width]])
    
    if y_pred[0]==0:
        y_pred="Setosa"

    elif  y_pred[0]==1:
        y_pred="Verscicolor"
    else:
        y_pred='Virginica'



    return render(request, "result.html",{'result':y_pred})