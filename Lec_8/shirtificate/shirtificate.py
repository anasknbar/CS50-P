from fpdf import FPDF

class PDF(FPDF):
      
  def shirtificate(self):
    user_name = input("Name: ").strip()
    self.add_page('P','a4',False)
    self.set_font('helvetica', 'B', 30)
    self.image('shirtificate.png',x=14,y=80,h=180)
    self.cell(0, 50, 'CS50 Shirtificate', align='c',new_y="NEXT")
    self.set_text_color(250, 250, 250)
    self.cell(-185, 150, f'{user_name} took CS50', align='c')
    self.output("shirtificate.pdf")
    
    
def main():    
    
  pdf = PDF()
  
  pdf.shirtificate()
  
if __name__ == "__main__":
  main()

