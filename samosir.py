#!/usr/bin/python
# coding=utf-8 

#Writen By :Nicoleus Sitorus
""" Github :Https://github.com/nicoleus
Youtube channel : ady sitorus ady
facebook  : Nicoleus Sitorus
The Place : Samosir, Danau Toba Nauli
"""
import requests,time,os,sys
import bs4,re,urllib
import BeautifulSoup as soup

r = '\x1b[31;1m'
y = '\x1b[33;1m'
b = '\x1b[34;1m'
p = '\x1b[35;1m'
c = '\x1b[36;1m'
w =  '\x1b[0;1m'
g = '\x1b[32;1m'
green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
pryellow = ("\033[93m")

class shit3:
  def __init__(self):
      self.ree=requests.Session()
      self.mee = bs4.BeautifulSoup
      self.cadow=[]
      self.header={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'}      
      self._urll=("https://www.google.com")
      n = "Only English to Arabic"
      me = "/search?ie=ISO-8859-1&hl=so&source=hp&biw=&bih=&q="+n+"&btnG=Raadin+Google&gbv="
      self._u= "http://translate.google.com/m?sl=ar&tl=en&hl=en"
      self.arabic = "http://translate.google.com/m?hl=en&sl=ar&tl=en&ie=windows-1256&prev=_m&q=Okbro"
      self.eng = "http://translate.google.com/m?hl=en&sl=so&tl=en&ie=windows-1256&prev=_m&q=bax waryaa"
      self._url = self.eng
      self.main()
      exit()
      self.dem= self.mee(self.ree.get(self._url).text,features='html.parser')
      self.f = open('/sdcard/full.html','w')
      x = self.dem.find('div',attrs={"class":"t0","dir":"ltr"})
      for xx in x:
          self.cadow.append(xx)
          self.somali= xx
          print self.somali
      #Arabic To English
  def ar(self):
      self.eng = "http://translate.google.com/m?hl=en&sl=en&tl=ar&ie=windows-1256&prev=_m&q=Ok i will"
      self.dem= self.mee(self.ree.get(self._url).text,features='html.parser')
      x = self.dem.find('div',attrs={"class":"o1","dir":"rtl"})
      for xx in x:
          self.cadow.append(xx)
          self.somali= xx
          return self.en()
      
    
  def sug(self,s):
      
      for i in s + '\n':
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.0002)          
  def main(self):
      print pryellow+''
      os.system('clear')
      ft = self.sug
      log = """
  
                   _     _  
                  | |   | |  ________   ______  __________   
                  | |___| | |  ___  || | |____| |       | |   ------ 
                  | |___  | | |   | || | |      |  /\   | |   |____ 
                  | |   | | | |___| || | |      |_______| |    ____| 
                  | |   | | |       || | |      |       | |          
                  |_|   |_| |_______|| |_|      |       |_|"""
      print log
      self.sug(w + '-' * 42)
      time.sleep(0.33)
      self.sug(g + 'YouTube Channel :' + c + 'ady sitorus ady')
      self.sug(g + 'Tool Type :' + c + 'Google Translate')
      self.sug(g + 'Github  : ' + c + 'https://github.com/nicoleus')
      self.sug(g + 'Facebook  : ' + c + 'Nicoleus Sitorus')
      self.sug(g + 'Open Source : ' + c + 'Yes')
      self.sug(g + 'Developer : ' + c + 'Nicoleus Sitorus... Oooo Yeee')  
      self.sug(g + 'The Pleace : Samosir, Nauli')
      self.sug(g + '#HORAS Indonesia Security Lite')
      self.sug(g + '#Subscribe YouTube')
      self.sug(g + '#Spesial Thanks To:')
      self.sug(g + '#' + c + 'Ijen Sinaga"')
      self.sug(g + '#' + c + 'Nicoleus Sitorus')
      self.sug(g + '#' + c + 'Wahyu GPS') 
      self.sug(g + '#' + c + 'BatakCyber')
      self.sug(g + '#' + c + 'COOL hACKER')
      self.sug(g + '#' + c + 'Hottua Haro')
      self.sug(g + '#' + c + 'SAMOSIR_TEAM Indonesia')
      self.sug(g + '#' + c + 'BATAK_NESE Security')
      self.sug(g + '#Association Batak Indonesian Right Wing')
      self.sug(g + '#And All Member Indonesia Security Lite')


      self.sug(g + '' + c + '.....HORAS HITA SUDE....')


      self.sug(g + '# ' + c + 'tunggu 8 detik Biar GetOut')
      time.sleep(1)
      print '-'*42
      self.sug(w + '-' * 42)
      print green+"([1]} Batak "+c+"To "+g+" Samosir"
      self.sug(w+'-'*42)
      print green+"([2]} Samosir "+c+"To "+g+" Batak"
      self.sug(w+'-'*42)
      print green+"([0])} HORAS..GoodBye.."
      self.sug(w+'-'*42)
      self.check()
      exit()
  def check(self):
      print
      me = green+"[🔧]Nicoleus=>> : "
      a = str(raw_input(me))
      if(a=='1'):
          self.s("en","so")
      elif(a=='2'):
          self.s('so','en')
      elif(a=='0'):
          time.sleep(1)
          exit()
      elif(a=='00'):
          time.sleep(1)
          shit3()
      else:
          print
          time.sleep(1)
          self.check()
       #samosir
  def s(self,me,you):
      print
      com = raw_input(green+'[🎩]your destination: ')
      print
      try:
          self.en = "http://translate.google.com/m?hl=en&sl="+me+"&tl="+you+"&ie=windows-1256&prev=_m&q="+com
          self.de= self.mee(self.ree.get(self.en).text,features='html.parser')
          x = self.de.find('div',attrs={"class":"t0","dir":"ltr"})
          for xx in x:
              self.cadow.append(xx)
              self.somali= xx
              print green+"[*]Output=>> : "+str(self.somali)
              print
              self.call()
              print
              time.sleep(1)
      except Exception as er:
          print 
          print "[*]Connection Error"+red+' 404'
          time.sleep(1)
          print
  def call(self):
      time.sleep(1.5)
      self.sug(w+'-'*42)
      print green+"([1]} Batak "+c+"To "+g+" Samosir"
      self.sug(w+'-'*42)
      print green+"([2]} Samosir "+c+"To "+g+" Batak"
      self.sug(w+'-'*42)
      print green+"([00])} Back..HORAS.."

 

      
      self.check() 
      
      
     
      
shit3()
