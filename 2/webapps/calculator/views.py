from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

template_name = 'calculator/index.html'
valuelist = []
def index(request):
    return render(request, template_name, { 'calcValue': 0 })

def get(request):
    value = ""
    displayValue=""
    result = ""
    calcValue = ""
    opsign=""
    if 'number' in request.GET:
        value = request.GET.get('number')
        valuelist.append(value)
        second = request.GET.get('second')
        first = request.GET.get('first')
        calcValue = request.GET.get('first')
        opsign = request.GET.get('operation')
        for val in valuelist:
            displayValue += val
        calcValue += value
        try:
            if value == "0" and first.strip() == "" and second.strip() =="":
                return render(request, template_name, {'first': 0, 'second': second, 'calcValue': 0, 'operation': opsign})
            elif not isinstance(calcValue, int):
                return render(request, template_name, {'first': calcValue, 'second': second, 'calcValue': calcValue, 'operation': opsign})
            else:
                return render(request, template_name, {'calcValue': "Error"})
        except ValueError:
            return render(request, template_name, {'calcValue': "Error"})
    elif 'operator' in request.GET:
        firstValue = request.GET.get('first')
        if request.GET.get('operator') == '+':
            opsign = request.GET.get('operation')
            valuelist.append(opsign)
            second = request.GET.get('second')
            first = request.GET.get('first')
            if second.strip() != "":
                try:
                    if opsign == '+':
                        result = int(first) + int(second)
                    elif opsign == '-':
                        result = int(first) - int(second)
                    elif opsign == "*":
                        result = int(first) * int(second)
                    elif opsign == "/":
                        result = int(first) / int(second)
                    else:
                        result = int(first) or int(second)
                except ValueError:
                    return render(request, template_name, { 'calcValue': "Error"})
                except ZeroDivisionError:
                    return render(request, template_name, { 'calcValue': "Error"})
            else:
                try:
                    result = int(first)
                except ValueError:
                    return render(request, template_name, {'first': calcValue, 'second': result, 'calcValue': 0, 'operation': '+'})
            return render(request, template_name, {'first': calcValue, 'second': result, 'calcValue': int(result), 'operation': '+'})
        elif request.GET.get('operator') == '-':
            opsign = request.GET.get('operation')
            valuelist.append(opsign)
            first = request.GET.get('second')
            second = request.GET.get('first')
            if first.strip() != "":
                try:
                    if opsign == '+':
                        result = int(first) + int(second)
                    elif opsign == '-':
                        result = int(first) - int(second)
                    elif opsign == "*":
                        result = int(first) * int(second)
                    elif opsign == "/":
                        result = int(first) / int(second)
                    else:
                        result = int(first) or int(second)
                except ValueError:
                    return render(request, template_name, { 'calcValue': "Error"})
                except ZeroDivisionError:
                    return render(request, template_name, { 'calcValue': "Error"})
            else:
                try:
                    result = int(second)
                except ValueError:
                    return render(request, template_name, { 'calcValue': "Error"})
            return render(request, template_name, {'first': calcValue, 'second': result, 'calcValue': int(result), 'operation': '-'})
        elif request.GET.get('operator') == '*':
            opsign = request.GET.get('operation')
            valuelist.append(opsign)
            second = request.GET.get('second')
            first = request.GET.get('first')
            if first.strip() == "" and second.strip() == "":
                return render(request, template_name, { 'calcValue': 0, 'operation': '*'})
            if second.strip() != "":
                try:
                    if opsign == '+':
                        result = int(first) + int(second)
                    elif opsign == '-':
                        result = int(second) - int(first)
                    elif opsign == "*":
                        result = int(first) * int(second)
                    elif opsign == "/":
                        result = int(first) / int(second)
                    else:
                        result = int(first) or int(second)
                except ValueError:
                    return render(request, template_name, { 'calcValue': "Error"})
                except ZeroDivisionError:
                    return render(request, template_name, { 'calcValue': "Error"})
            else:
                result = int(first)
            return render(request, template_name, {'first': calcValue, 'second': result, 'calcValue': int(result), 'operation': '*'})
        elif request.GET.get('operator') == '/':
            opsign = request.GET.get('operation')
            valuelist.append(opsign)
            second = request.GET.get('first')
            first = request.GET.get('second')
            if first.strip() == "" and second.strip() == "":
                return render(request, template_name, { 'calcValue': 0, 'operation': '/'})
            if first.strip() != "":
                try:
                    if opsign == '+':
                        result = int(first) + int(second)
                    elif opsign == '-':
                        result = int(second) - int(first)
                    elif opsign == "*":
                        result = int(first) * int(second)
                    elif opsign == "/":
                        result = int(first) / int(second)
                    else:
                        result = int(first) or int(second)
                except ValueError:
                    return render(request, template_name, { 'calcValue': "Error"})
                except ZeroDivisionError:
                    return render(request, template_name, { 'calcValue': "Error"})
            else:
                result = int(second)
            return render(request, template_name, {'first': calcValue, 'second': firstValue, 'calcValue': int(result), 'operation': '/'})
    if request.GET.get('equals') == '=':
        firstValue = request.GET.get('second')
        secondValue = request.GET.get('first')
        opsign = request.GET.get('operation')
        if (firstValue.strip() != "" and not isinstance(firstValue, int)) and (secondValue.strip() != "" and not isinstance(firstValue, int)):
                try:
                    if opsign == '+':
                        result = int(firstValue) + int(secondValue)
                    elif opsign == '-':
                        result = int(firstValue) - int(secondValue)
                    elif opsign == "*":
                        result = int(firstValue) * int(secondValue)
                    elif opsign == "/":
                        result = int(firstValue) / int(secondValue)
                except ValueError:
                    return render(request, template_name, { 'calcValue': "Error"})
                except ZeroDivisionError:
                    return render(request, template_name, { 'calcValue': "Error"})
        else:
            return render(request, template_name, { 'calcValue': "Error"})
        return render(request, template_name, {'first': "", 'second': "", 'calcValue': int(result)})