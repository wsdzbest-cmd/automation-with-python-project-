
import camelot 
table = camelot.read_pdf('file:///C:/Users/DELL/Downloads/python_revision_with_while_loop.pdf', pages='2')
print(table)
table.export('table.csv', f='csv', compress=True)
table[0].to_csv('table.csv')