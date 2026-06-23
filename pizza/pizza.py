import tabulate
import sys
import csv

table = []

if len( sys.argv ) == 1 :
    sys.exit( 'Too few command-line arguments' )

elif len( sys.argv ) > 2 :
    sys.exit( 'Too many command-line arguments' )

elif len( sys.argv ) == 2 and not sys.argv[ 1 ].endswith( '.csv' ) :
    sys.exit( 'Not a CSV file' )

else :
    try :
        with open( sys.argv[ 1 ] ) as file :
            reader = csv.reader( file )
            for row in reader :
                table.append( row )

        print( tabulate.tabulate( table[ 1 : ] , headers = table[ 0 ] , tablefmt = "grid" ) )

    except FileNotFoundError :
        sys.exit( 'File does not exist' )