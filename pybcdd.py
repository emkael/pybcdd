﻿import os
import sys

from bcdd.DDTable import DDTable
from bcdd.ParScore import ParScore
from bcdd.Exceptions import DllNotFoundException, FieldNotFoundException
from bcdd.PBNFile import PBNFile

def get_files(args):
    filenames = [name for name in args
                 if os.path.exists(name)
                 and (os.path.realpath(name) != os.path.realpath(__file__))]
    if len(filenames) == 0:
        raise FileNotFoundError('No valid filepaths provided!')
    return filenames

def main():
    files = get_files(sys.argv)
    errors = []
    for filename in files:
        try:
            print('Analyzing %s' % (filename))
            pbn_file = PBNFile(filename)
            for board in pbn_file.boards:
                table = DDTable(board)
                board_no = ''
                try:
                    board_no = board.get_number()
                except FieldNotFoundException:
                    board_no = '?'
                try:
                    dd_table = table.get_dd_table()
                    if dd_table is not None:
                        print('Board ' + board_no)
                        table.print_table(dd_table)
                        par = ParScore(board)
                        contract = par.get_par_contract(dd_table)
                        print(contract)
                        print('')
                        board.save_dd_table(dd_table)
                        board.save_par_contract(contract)
                        pbn_file.write_board(board)
                    else:
                        error = 'unable to determine DD table for board %s' \
                                % (board_no)
                        errors.append('[%s] %s' % (filename, error))
                        print('ERROR: ' + error)
                except DllNotFoundException:
                    raise
                except Exception as ex:
                    errors.append('[%s:%s] %s' % (filename, board_no, str(ex)))
                    print('ERROR: ' + str(ex))
                    raise
            pbn_file.save()
        except DllNotFoundException as ex:
            errors.append("libbcalcdds library could not be loaded - make sure it's present in application directory!");
            print('ERROR: ' + str(ex))
            break
        except Exception as ex:
            errors.append(str(ex))
            print('ERROR: ' + str(ex));
            raise
    if len(errors) > 0:
        print('Following ERRORs occured:')
        for error in errors:
            print(error)
        input('Press any key to continue...')

if __name__ == '__main__':
    main()