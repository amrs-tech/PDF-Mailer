from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('C:\\xampp\\htdocs\\gct\\gct1.png', 8, 6, 20)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(90)
        # Title
        self.cell(30, 10, 'Government College of Technology, Coimbatore-13', 0, 0, 'C')
        # Line break
        self.ln(8)
        self.cell(90)
        self.set_font('Arial', 'B', 10)
        self.cell(30, 10, '(An Autonomous institution affiliated to Anna University)', 0, 0, 'C')


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
def generate(a,b,c):    
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', 'B', 13)
    pdf.ln(h='')
    pdf.ln(h='')
    
    pdf.cell(0, 10, 'Grievances Form', 0, 1,'C')
    pdf.ln(h='')
    pdf.ln(20)
    pdf.set_font('Times','',12)
    pdf.cell(0, 10, 'Designation - '+str(a), 0, 1)
    pdf.ln(10)

    pdf.cell(0, 10, 'Department - '+str(b), 0, 1)
    pdf.ln(10)

    pdf.cell(0, 10, 'Message - '+str(c), 0, 1)
    pdf.ln(10)

    pdf.output('output.pdf', 'F')