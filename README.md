# SummariseMe

What it does: Reads in pdf files and generates a summary, so you no longer need to painfully read long and boring things :)

## Dependencies
- pdfminer
- six
- gensim

## How does it work? 
It works using a summarisation algorithm called TextRank, which was inspired by Google's PageRank algorithm. Read more about 
TextRank here: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwiz5MCgy5LgAhUHT30KHW7hCv0QFjAAegQICBAC&url=https%3A%2F%2Fweb.eecs.umich.edu%2F~mihalcea%2Fpapers%2Fmihalcea.emnlp04.pdf&usg=AOvVaw0BUSxH01zoqL1GTj3uu0k5.

## Usage
Install the relevant python libraries and add the file to your working directory. Change the relevant page range in the document that you
need to summarise and change the relevant file path to the file that you would like to summarise. Note: It currently only works for pdf files!
You can also specify the number of lines that you would like to summarise to (the number in code is 500).

## Testing
I have tested it with the pdf file in this directory, you can see the results for yourself in the summary.txt file :)
