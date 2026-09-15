def dont_execute_me():
    module_execution_text: str = '''
    This is an external module loaded by the LBP Popit Color Generator\'s Main Program, main.py.
    It is not meant to be loaded as a standalone script.
    If you want to use its functions, use the Main Program (for the time being)
    '''

    print(module_execution_text)

def main():
    dont_execute_me()

if __name__ == '__main__':
    main()
