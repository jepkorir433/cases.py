class superhero:
     def _init_(self, name, power, secret_identity, level=1):
         self.name = name
         self.power = power
         self.secret_identity = secret_identity
         self.level =  level
         
         
         
def attack(self):
    print(f"{self.name} attack with{self.power}!")
         
         
         
def  display_info(self):
     print(f"{self.name} ,power:{self.power},Secret Identity:{self.secret_identity},level:{self.level}")
     
     
     
class Villain(superhero):
     def _init_(self, name, power, secret_identity, level=1):
           super()._init_(name, power, secret_identity, level)
           self.evil_plan = evil_plan   
           
          
def attack(self):
    print(f"{self.name} uses{self.power} to excute{self.evil_plan}!")
    
   
def reveal_plan(self):
        print(f"My evil plan is {self.evil_plan}!")
        
        
hero = superhero("Captain Light", "Laser Beams", "Bob Smith", 10)
villain = Villain("Dr.Chaos", "Mind Control", "Alice Grey", "world domination")
        
         
     
  
     