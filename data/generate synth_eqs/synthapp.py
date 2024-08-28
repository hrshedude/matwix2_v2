from flask import Flask, render_template, request
import random
import itertools


alphas_s_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphas_s_L = "abcdefghijklmnopqrstuvwxyz"

nums_s = "1234567890"
symbs_s = "+-/*=()"

all_symbs = alphas_s_L+nums_s+symbs_s

font_familys =  ["serif","sans-serif","cursive","fantasy","monospace","Perpetua","Monaco","Didot","Brush Script","Copperplate","Comic Sans","Arial"]
font_styles  =  ["normal","italic"]
font_sizes = range(35,60,1)
font_weights =  range(100,851, 50)
align_items = ["flex-start", 'center', "flex-end"]
justify_items = ["flex-start", 'center', "flex-end"]


all_things = (font_familys,font_styles, font_sizes,font_weights,align_items, justify_items)

# totn = 3
# all_l = [[random.choice(i) for i in all_things] for _ in range(totn)]

# def rnd_l():
#   for _ in range(totn):
#     yield [random.choice(i) for i in all_stuff]

# all_l = rnd_l() 




def rnd_items(x, rng=(1,7)):
  """
  get random amount of items from iterable
  
  *here  specialise for str
  
  x: iterable
  rng-> tuple of range random
  """
  
  s = ""
  for _ in range(random.randint(*rng)):
    s += random.choice(x) 
    
  return s  
  
  
def fake_eq():

  # expr = rnd_items(nums_s, (1,4))+random.choice(symbs_s)+rnd_items(nums_s, (1,4))+random.choice(symbs_s)+rnd_items(nums_s, (1,2))
  # expr = rnd_items(all_symbs)
  expr = rnd_items(all_symbs, (1,1))

  return expr
  
  



app = Flask(__name__)

sym_text = fake_eq()
sl = [random.choice(i) for i in all_things]
cstate = True
imno = 0
svnm = sym_text.replace("*","[multiply]").replace("/","[divideforward]")

@app.route("/", methods=["GET", "POST"])
def index():
  
  global sym_text
  global sl
  global cstate
  global imno
  global svnm
  
  if request.method == "POST":
    
    sym_text = fake_eq()
    print(sym_text)
    svnm = sym_text.replace("*","[multiply]").replace("/","[divideforward]")

    sl = [random.choice(i) for i in all_things]
    imno +=1
    # if item == False:
    #   cstate = False
    # else:
    #   sym_text,imno,sl = item
      

  
  if cstate == True:
    return render_template("index.html",
                          sym_text=sym_text,
                          save_name=f"img_{svnm}_goofrmv{imno}.png",
                          font_family =  sl[0] ,
                          font_style  =  sl[1],
                          font_size   =  f"{sl[2]}px" ,
                          font_weight =  sl[3],
                          align_item = sl[4],
                          justify_item = sl[5]
                          )
  else:

    return "NIGGGA"

if __name__ == "__main__":
  app.run(debug=True)
