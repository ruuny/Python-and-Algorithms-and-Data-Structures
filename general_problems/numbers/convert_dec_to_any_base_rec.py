def convert_dec_to_any_base_rec(number, base):
    ''' 정수를 다른 진법(문자열)으로 변환한다.'''
    convertString = '012345679ABCDEF'
    if number < base: return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number//base, base) + convertString[number%base] 
    
def test_convert_dec_to_any_base_rec(module_name='this module'):
    number = 9
    base = 2
    assert(convert_dec_to_any_base_rec(number, base) == '1001')
        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_convert_dec_to_any_base_rec()
