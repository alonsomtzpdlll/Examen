# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import datos
import pandas as pd
import numpy as np
import csv
import tkinter
import matplotlib.pyplot as plt
import io
import urllib
import base64

def inicio(request):
    dato = datos.objects.all()
    contexto = {
    'datos':dato,
    }
    return render(request,"index.html",contexto)

def bv(request):
    return render(request,"Bienvenido.html")

def altura(request):
    df = pd.read_csv("/home/alonso/Examen/Exm/Book1.csv")
    lis = df["Altura"].unique()
    dat = pd.DataFrame(lis, columns=["Altura"])
    datafi = pd.crosstab(index=df["Altura"], columns = "fi")
    li=datafi.values
    dat["fi"]=li
    datahi = 100 * datafi["fi"] / 30
    datahi = datahi.values
    dat["hi"]=datahi
    Hi = dat["hi"].values
    a = []
    b = 0
    for c in Hi:
        b = c + b
        a.append(b)
    dat["Hi"] = a
    Fi = dat["fi"].values
    a1 = []
    b1 = 0
    for c1 in Fi:
        b1 = c1 + b1
        a1.append(b1)
    dat["Fi"] = a1
    uri = pie(dat)
    uri1=bars(dat)
    uri2=Dint(dat)
    print(dat)
    moda=df["Altura"].mode()
    mediana=df["Altura"].median()
    media=df["Altura"].mean()
    dato = datos.objects.all()
    contexto = {
    'datos':dato,
    'mod':dat,
    'data':uri,
    'data1':uri1,
    'data2':uri2,
    'Moda':moda,
    'Mediana':mediana,
    'Media':media,
    }
    return render(request,"Altura.html",contexto)

def peso(request):
    df = pd.read_csv("/home/alonso/Examen/Exm/Book1.csv")
    lis = df["Peso"].unique()
    dat = pd.DataFrame(lis, columns=["Peso"])
    datafi = pd.crosstab(index=df["Peso"], columns = "fi")
    li=datafi.values
    dat["fi"]=li
    datahi = 100 * datafi["fi"] / 30
    datahi = datahi.values
    dat["hi"]=datahi
    Hi = dat["hi"].values
    a = []
    b = 0
    for c in Hi:
        b = c + b
        a.append(b)
    dat["Hi"] = a
    Fi = dat["fi"].values
    a1 = []
    b1 = 0
    for c1 in Fi:
        b1 = c1 + b1
        a1.append(b1)
    dat["Fi"] = a1
    uri = pie(dat)
    uri1=bars(dat)
    uri2=Dint(dat)
    print(dat)
    moda=df["Peso"].mode()
    mediana=df["Peso"].median()
    media=df["Peso"].mean()
    dato = datos.objects.all()
    contexto = {
    'datos':dato,
    'mod':dat,
    'data':uri,
    'data1':uri1,
    'data2':uri2,
    'Moda':moda,
    'Mediana':mediana,
    'Media':media,
    }
    return render(request,"Peso.html",contexto)

def color(request):
    df = pd.read_csv("/home/alonso/Examen/Exm/Book1.csv")
    lis = df["color"].unique()
    dat = pd.DataFrame(lis, columns=["color"])
    datafi = pd.crosstab(index=df["color"], columns = "fi")
    li=datafi.values
    dat["fi"]=li
    datahi = 100 * datafi["fi"] / 30
    datahi = datahi.values
    dat["hi"]=datahi
    Hi = dat["hi"].values
    a = []
    b = 0
    for c in Hi:
        b = c + b
        a.append(b)
    dat["Hi"] = a
    Fi = dat["fi"].values
    a1 = []
    b1 = 0
    for c1 in Fi:
        b1 = c1 + b1
        a1.append(b1)
    dat["Fi"] = a1
    uri = pie(dat)
    uri1=bars(dat)
    uri2=Dint(dat)
    print(dat)
    moda=df["color"].mode()
    #mediana=df["color"].median()
    #media=df["color"].mean()
    dato = datos.objects.all()
    contexto = {
    'datos':dato,
    'mod':dat,
    'data':uri,
    'data1':uri1,
    'data2':uri2,
    'Moda':moda,
    #'Mediana':mediana,
    #'Media':media,
    }
    return render(request,"Color.html",contexto)

def velocidad(request):
    df = pd.read_csv("/home/alonso/Examen/Exm/Book1.csv")
    lis = df["Velocidad"].unique()
    dat = pd.DataFrame(lis, columns=["Velocidad"])
    datafi = pd.crosstab(index=df["Velocidad"], columns = "fi")
    li=datafi.values
    dat["fi"]=li
    datahi = 100 * datafi["fi"] / 30
    datahi = datahi.values
    dat["hi"]=datahi
    Hi = dat["hi"].values
    a = []
    b = 0
    for c in Hi:
        b = c + b
        a.append(b)
    dat["Hi"] = a
    Fi = dat["fi"].values
    a1 = []
    b1 = 0
    for c1 in Fi:
        b1 = c1 + b1
        a1.append(b1)
    dat["Fi"] = a1
    uri =pie(dat)
    uri1=bars(dat)
    uri2=Dint(dat)
    print(dat)
    moda=df["Velocidad"].mode()
    #mediana = 0
    #M=[]
    #a=len(dat["Velocidad"])
    #for i in range(a):
    #    if dat["Velocidad"].iloc[i] == "NAN":
    #      dat["Velocidad"].iloc[i]=0

    #M=dat['Velocidad']
    #mediana=M.median()
    #media=M.mean()
    dato = datos.objects.all()
    contexto = {
    'datos':dato,
    'mod':dat,
    'data':uri,
    'data1':uri1,
    'data2':uri2,
    'Moda':moda,
    #'Mediana':mediana,
    #'Media':media,
    }
    return render(request,"Velocidad.html",contexto)

def pie(dat):
    if "Altura" in dat:
        lab="Altura"
    elif "Peso" in dat:
        lab="Peso"
    elif "Velocidad" in dat:
        lab = "Velocidad"
    else:
        lab = "color"

    labels = dat[lab]

    sizes = dat["hi"]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    ax1.set_title('Frecuencia Relativa')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =urllib.parse.quote(string)
    return uri

def bars(dat):
#Grafica 2
    if "Altura" in dat:
        lab="Altura"
    elif "Peso" in dat:
        lab="Peso"
    elif "Velocidad" in dat:
        lab= "Velocidad"
    else:
        lab="color"

    plt.rcdefaults()
    fig, ax = plt.subplots()

    label = dat[lab]
    y_pos = np.arange(len(label))
    performance = dat['fi']

    ax.barh(y_pos, performance, xerr=None, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(label)
    ax.invert_yaxis()
    ax.set_title('Frecuencia Absoluta')

    fig1 = plt.gcf()
    buf1 = io.BytesIO()
    fig1.savefig(buf1,format='png')
    buf1.seek(0)
    string1 = base64.b64encode(buf1.read())
    uri1 =urllib.parse.quote(string1)
    return uri1

def Dint(dat):
    #Grafica 3
    if "Altura" in dat:
        lab = "Altura"
    elif "Peso" in dat:
        lab= "Peso"
    elif "Velocidad" in dat:
        lab = "Velocidad"
    else:
        lab = "color"

    labels = dat[lab]
    FrAcum = dat['Fi']
    FrRel = dat['hi']

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, FrAcum, width, label='Frecuencia Acumulada')
    rects2 = ax.bar(x + width/2, FrRel, width, label='Frecuencia Relativa')

    ax.set_title('Diagrama Integral')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    #autolabel(rects2)

    fig.tight_layout()

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =urllib.parse.quote(string)
    return uri
