from fpdf import FPDF
import pandas as pd


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('C:/Users/user/PycharmProjects/SeniorV7.0/images/logo.png', 5, 1, 25)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Pre-Launch Forecaster', 0, 0, 'C')
        # Line break
        self.ln(20)
        self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'This File was automatically generated by PLF systems', 0, 0, 'C')

        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # Instantiation of inherited class
    def chapter_title(self, num, label,value):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Output %d : %s %s' % (num, label, value), 0, 1, 'L', 1)
        # Line break
        self.ln(4)
    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name, value):
        self.add_page()
        self.chapter_title(num, title, value)
        self.chapter_body(name)

    def dataset(self, datasetName):
        df = pd.read_csv(datasetName)
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times', '', 12)
        pdf.multi_cell(10, 12, '' + '\n' + '')
        pdf.chapter_title(1,'The Data you entered is', ':')
        pdf.cell(5, 10, 'The Data you entered is: ', 0, 1)
        pdf.cell(5, 10, 'Horsepower ' + str(df['horsepower'][0]), 0, 1)
        pdf.cell(5, 10, 'Car Width: ' + str(df['carwidth'][0]), 0, 1)
        pdf.cell(5, 10, 'Car Body: ' + str(df['carbody'][0]), 0, 1)
        pdf.cell(5, 10, 'Engine Type: ' + str(df['enginetype'][0]), 0, 1)

        pdf.cell(5, 10, 'Fuel Type: ' + str(df['fueltype'][0]), 0, 1)
        pdf.cell(5, 10, 'Aspiration: ' + str(df['aspiration'][0]), 0, 1)
        pdf.cell(5, 10, 'Cylinder Number: ' + str(df['cylindernumber'][0]), 0, 1)
        pdf.cell(5, 10, 'Drive Wheel: ' + str(df['drivewheel'][0]), 0, 1)
        pdf.cell(5, 10, 'Wheel Base: ' + str(df['wheelbase'][0]), 0, 1)
        pdf.cell(5, 10, 'Curb Weight: ' + str(df['curbweight'][0]), 0, 1)
        pdf.cell(5, 10, 'Engine Size: ' + str(df['enginesize'][0]), 0, 1)
        pdf.cell(5, 10, 'Boreratio: ' + str(df['boreratio'][0]), 0, 1)
        pdf.cell(5, 10, 'City MPG: ' + str(df['city_mpg'][0]), 0, 1)
        pdf.cell(5, 10, 'Highway MPG: ' + str(df['highwaympg'][0]), 0, 1)
        pdf.cell(5, 10, 'Car Length: ' + str(df['carlength'][0]), 0, 1)
        pdf.cell(5, 10, 'Car Width: ' + str(df['carwidth'][0]), 0, 1)

        pdf.cell(5, 10, 'Engine Cylinders: ' + str(df['Engine_Cylinders'][0]), 0, 1)
        pdf.cell(5, 10, 'Engine HP: ' + str(df['Engine_HP'][0]), 0, 1)
        # pdf.cell(0,0,5)
        pdf.cell(5, 10, 'Market Category: ' + str(df['Market_Category'][0]), 0, 1)
        pdf.cell(5, 10, 'Number of Doors: ' + str(df['Number_of_Doors'][0]), 0, 1)
        pdf.cell(5, 10, 'Vehicle Size: ' + str(df['Vehicle_Size'][0]), 0, 1)
        pdf.cell(5, 10, 'Vehicle Style: ' + str(df['Vehicle_Style'][0]), 0, 1)
        pdf.cell(5, 10, 'Year: ' + str(df['Year'][0]), 0, 1)
        pdf.cell(5, 10, 'city mpg: ' + str(df['city_mpg'][0]), 0, 1)
        pdf.cell(5, 10, 'highway MPG: ' + str(df['highway_MPG'][0]), 0, 1)

        print('Report Updated')
        return pdf
