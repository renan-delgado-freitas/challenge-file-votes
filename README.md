# Data Processor

The Data Processor is a project that reads an input file in .dat format, filters the information, and generates a report with some statistics about the processed data.

## Features

- .dat File Reading: The project is capable of reading an input file in .dat format and processing the information contained in it.
- Data Filtering: The read data is filtered into three main categories: sellers, customers, and sales.
- Report Generation: The project generates a report with statistics about the processed data, such as the number of sellers and customers, the ID of the most expensive sale, and the worst seller.
- Sample Output: In addition to the report, the project also provides a function to print sales per salesman for debugging purposes.

## Requirements

- Python 3.11

## Installation

1. Make sure you have Python 3.11 installed on your system.
2. Clone this repository: `git clone https://github.com/renan-delgado-freitas/challenge-file-votes
3. Install the dependencies: `pip install -r requirements.txt`

## Usage

To run the data processing, execute the following command:

uvicorn main:app --host 0.0.0.0 --port 8000


## .dat File Structure

### For each type of data there is a different layout.
Seller data
The seller data has the format id 001 and the row will have the following format: 001çCPFçNameçSalary

#### Customer data
Customer data has the format id 002 and the row will have the following format: 002çCNPJçNameçBusiness Area

#### Sales data
The sales data has the format id 003. Inside the sales line, there is the list of items, which is enclosed by square brackets []. The line will have the following format: 003çSale IDç[Item ID-Item Quantity-Item Price]çSalesman name

#### Example Data
The following is an example of the data the system should be able to read.

- 001ç1234567891234çPedroç50000
- 001ç3245678865434çPauloç40000.99
- 002ç2345675434544345çJose da SilvaçRural
- 002ç2345675433444345çEduardo PereiraçRural
- 003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çPedro
- 003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çPaulo


## Files
- main.py: Contains the FastAPI application with routes for data processing.
- read_file.py: Contains the functions responsible for reading the input file, filtering the data, and creating the report.
- data/in/entrada.dat: Input file containing the data in .dat format.
- data/out/report.done.dat: Output file with the generated report.


# Sample Output

- Number of sellers in the input file: 7
- Number of customers in the input file: 8
- ID of the most expensive sale: 245
- Worst seller: Pedro
