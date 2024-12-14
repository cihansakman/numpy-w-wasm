import sys
import analyze_dataset
from utils import load_data, analyze_data, help_message
from analyze_dataset import exports


class Analyze(exports.Analyze):
    def analyze(self, file_path:str) -> str:
        print(f'Analyzing {file_path}...')
        data = load_data(file_path=file_path)
        
        result = ""
        
        #general info about the dataset
        column_names = data.dtype.names
        num_rows = len(data)
        num_columns = len(column_names)
        result += (f"\n=== General Outline of {file_path} ===")
        result += (f"\nNumber of rows: {num_rows}")
        result += (f"\nNumber of columns: {num_columns}")
        result += (f"\nColumn names: {', '.join(column_names)}\n")
    
        report = analyze_data(data)
    
            
        result +=("\n\n=== Analysis Report ===")
        for col, analysis in report.items():
            result += f"\n\nColumn: {col}"
            for key, value in analysis.items():
                result += f"\n\t{key}: {value}"
        
        #result += ("\n\n=== Columns with {regex_term} Mentioned ===")
        #for row in cost_rows:
        #    result += row
        
        return result


class Run(exports.Run):
    def run(self) -> None:
        args = sys.argv[1:]
        if len(args) != 1:
            help_message()
            exit(-1)

        analyze_obj = Analyze()
        print(analyze_obj.analyze(str(args[0])))