import requests
from bs4 import BeautifulSoup
from sys import argv
import os
import webbrowser
import random
import pickle
def randprob():
    try:
        with open("prob.txt", "rb") as fp: 
            problems = pickle.load(fp)
    except:
        problems=[]
    problem_type=argv[1].upper()
    if len(problems)!=0:
        problems=[problem for problem in problems if problem[1]==problem_type]
    
    if len(problems)==0:
        page_num=1
        while 1:
            try:
            
                url="https://codeforces.com/contests/page/"+str(page_num)
                page = BeautifulSoup(requests.get(url, timeout=15).text, 'lxml')
            except:
                print("Failed.Please try again later.")
                return
            contests=page.find_all('td')
        
            for contest in contests:
                if "Div. 2" in contest.text:
                    link="https://codeforces.com"+contest.find_next('a').attrs['href']
                    if [link,problem_type,0] not in problems:
                        problems.append([link,problem_type,0])
            if len(problems)!=0:
                break
            else:
                page_num+=1
    while 1:
        idx=random.randint(0,len(problems)-1)
        if problems[idx][2]==1:
            continue
        webbrowser.open(problems[idx][0]+"/problem/"+problems[idx][1])
        c=input('Solved?(y/n)')
        if c=="y":
            problems[idx][2]=1
        c=input('Another?(y/n)')
        if c=='n':
            break
    with open("prob.txt", "wb+") as fp:  
          pickle.dump(problems, fp)
if __name__ == "__main__":
    randprob()
    

