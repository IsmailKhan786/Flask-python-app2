from distutils.log import debug
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from flask import Flask,request
app = Flask(__name__) #creating flask class object
 
@app.route('/') 
def home():
    return "Hello This is our flask";

@app.route('/arith',methods = ['POST'])
def arith():
    opr = request.form['opr']
    result = 0
    print(opr)
    no1 = int(request.form['no1'])
    no2 = int(request.form['no2'])
    if opr == '+':
        result = no1 + no2 
    elif opr == '-':
        result = no1 - no2 
    elif opr =='/':
        result = no1/no2
    elif opr =='*':
        result = no1 * no2 
    elif opr =='%':
        result = no1 % no2 
        
    else: 
        print("Error") 
    return "Result %s" %result

# app.route('/mcq',methods = ['POST'])
# def mcq():
     
#       q1=request.form['q1']
#       result1=0
    

#       if q1=='JavaScript':
#            result1=result1+1
      
#       return "Result %s" %result1

@app.route('/mcq',methods = ['POST'] )
def mcq():
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
  
    result1 = 0
    

    if q1 =='JavaScript':
        result1 = result1 +1
    if q2 =="JavaScript":
        result1+=1  
    if q3 =='JavaScript':
        result1 = result1 +1
    if q4 =="JavaScript":
        result1+=1  
    if q5 =="JavaScript":
        result1+=1  
              
         
    return f"Result is {result1}"

if __name__ =='__main__':
    app.run(debug= True)

