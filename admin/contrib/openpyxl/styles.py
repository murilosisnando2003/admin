from openpyxl.styles.fills import PatternFill
from openpyxl.styles.borders import Border, Side

fill = PatternFill(start_color='0070c0',
                   end_color='0070c0',
                   fill_type='solid')

border = Border(left=Side(border_style='thin',color='000000'),right=Side(border_style='thin',color='000000'),top=Side(border_style='thin',color='000000'),
        bottom=Side(border_style='thin',color='000000'))

fill_rosa = PatternFill(start_color='ff99ff',
                   end_color='ff99ff',
                   fill_type='solid')

fill_azul_claro = PatternFill(start_color='00b0f0',
                   end_color='00b0f0',
                   fill_type='solid')

fill_roxo = PatternFill(start_color='8064a2',
                   end_color='8064a2',
                   fill_type='solid')

fill_verde = PatternFill(start_color='92d050',
                   end_color='92d050',
                   fill_type='solid')

fill_vermelho = PatternFill(start_color='ff0000',
                   end_color='ff0000',
                   fill_type='solid')

fill_cinza = PatternFill(start_color='ebf1de',
                   end_color='ebf1de',
                   fill_type='solid')

