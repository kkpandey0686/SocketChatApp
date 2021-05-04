from key_generator import *

def text_to_numeric_cipher(text):
    cipher ="1"
    for ch in text:
        if ord(ch)>99:
            cipher+=str(ord(ch))
        elif ord(ch)>9:
            cipher+="0"
            cipher+=str(ord(ch))
        else:
            cipher+="00"
            cipher+=str(ord(ch))

    return cipher

def numeric_cipher_to_text(numeric_cipher):
    number = int(numeric_cipher)
    text=""

    while True:
        rem = number%1000
        number = number//1000
        ch = chr(rem)
        text+=ch

        if number == 1:
            return text[::-1]


def encrypt(x, y, p):
    res = 1  
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
 
        if ((y % 2) == 1) :
            res = (res * x) % p

        y = y//2  
        x = (x * x) % p
         
    return res


def decrypt(x, y, p):
    res = 1    
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        if ((y % 2) == 1) :
            res = (res * x) % p 

        y = y//2    
        x = (x * x) % p
         
    return res

# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sed laoreet nibh. Cras hendrerit elit vel pellentesque tincidunt. Fusce efficitur egestas tristique. Aliquam at sem et lacus ultricies tempor. Ut vitae est ac lacus tempor tincidunt. Sed tellus enim, ultrices ac est in, malesuada rhoncus lorem. Integer tempus dolor id porttitor convallis. Praesent sagittis pretium augue dapibus malesuada. Donec id elit lectus.Sed at enim volutpat, elementum tellus sed, aliquet sem. In ac efficitur arcu. Quisque at dapibus lectus, a luctus nisl. Fusce quis luctus lorem, eu venenatis enim. Curabitur aliquam ornare nisl non ornare. Nulla accumsan turpis quis commodo aliquam. Nulla iaculis arcu ut fringilla rhoncus. Quisque egestas, ipsum et iaculis laoreet, justo eros fermentum lacus, a tempus quam risus non urna.Sed hendrerit scelerisque lectus, et fermentum lectus facilisis sed. Fusce sed efficitur lorem, vitae tincidunt odio. Nulla elementum dictum faucibus. Mauris nec velit vitae lacus sagittis dapibus a nec sem. Phasellus faucibus ultrices cursus. Nunc diam ex, vehicula sit amet scelerisque vel, faucibus sit amet enim. Maecenas vitae luctus nisi, quis posuere arcu. Ut elit lectus, faucibus sed commodo laoreet, facilisis accumsan nisl. Nunc consequat efficitur urna, eu bibendum ex consectetur non. Aenean placerat quam ex, eget laoreet dolor aliquet et. Cras et blandit leo. Quisque eget tempor nisi, id fringilla mi. Donec sit amet sem dignissim, mollis tellus ac, commodo lectus. Phasellus mattis eros sed euismod pellentesque. Curabitur tincidunt arcu quis metus auctor tempor. Donec in tellus consectetur, accumsan est a, finibus ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sollicitudin dui libero, id vehicula erat vehicula ac. Curabitur massa enim, feugiat eget odio vel, imperdiet cursus orci. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas a lectus id odio lacinia iaculis vel ac elit. Proin placerat erat sit amet risus consectetur, a molestie ex tincidunt. Morbi hendrerit viverra arcu sed fringilla. Sed at gravida lorem. Nulla facilisi. Fusce ultricies justo sed nibh volutpat suscipit. Pellentesque sollicitudin elit vitae mi sodales venenatis. Vivamus interdum dui a nulla bibendum iaculis. Morbi magna nisl, auctor nec molestie sit amet, sagittis ac quam. Aenean vehicula eu nulla eget laoreeMorbi mauris lectus, mattis ac dui vel, accumsan sollicitudin felis. Pellentesque purus elit, blandit a condimentum et, tempor nec tortor. Nulla dapibus suscipit lectus, id gravida sem ullamcorper sed. Curabitur porta lacus eu pharetra iaculis. Morbi ante tellus, rhoncus vitae nisi at, vehicula viverra dui. Nunc semper quam ac cursus commodo. Fusce ac cursus ipsum. Vestibulum efficitur pulvinar urna, a volutpat mauris lacinia at. Suspendisse id magna turpis. Nam condimentum tincidunt enim vel vestibulum. Sed vestibulum felis a mauris elementum sodales. Curabitur pellentesque rhoncus eros quis efficitur. Vivamus lobortis semper quam non efficitur. Integer est dui, cursus vel pellentesque non, dignissim a elit. Curabitur tempor cursus sem, sed mollis dui aliquet sit ameFusce nunc eros, mollis id fringilla rutrum, dapibus sed tortor. Morbi at aliquam justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus consequat eget nisl a venenatis. In hac habitasse platea dictumst. In ornare in risus eu aliquet. Fusce non nulla ut elit fringilla feugiat quis eu nunc. Nulla arcu nisi, interdum in porttitor ac, placerat ornare felis. Phasellus semper mauris a tortor eleifend tincidunt. Vestibulum a fringilla nibh, eget auctor ex. Nulla blandit nunc pharetra, euismod risus a, luctus urnIn vulputate erat a lacinia sagittis. Nunc egestas lobortis sollicitudin. Quisque non lacus urna. Integer eget libero et nunc egestas condimentum id eu erat. Aliquam euismod id lectus nec scelerisque. Suspendisse et lacus pulvinar ligula feugiat fermentum. Sed leo enim, fermentum ornare urna ac, vehicula feugiat sapieSuspendisse libero odio, ultricies nec orci sed, aliquet luctus arcu. Praesent auctor lorem in sapien euismod imperdiet. Nunc sollicitudin leo leo, et volutpat libero bibendum non. Mauris molestie aliquam scelerisque. Fusce id risus placerat, pellentesque velit feugiat, accumsan massa. In porta dolor vitae tincidunt pellentesque. Aenean viverra orci ut nibh facilisis porta. Mauris suscipit quis urna sit amet sodales. Maecenas imperdiet commodo elementum. Aenean ut lacus faucibus, laoreet nunc ac, vehicula elit. Donec libero odio, consectetur sit amet nisi a, eleifend malesuada tortor. Curabitur sit amet eros elit. In et libero nec sapien mollis finibus non at tortor.Sed sollicitudin facilisis risus a iaculis. Donec pulvinar quam venenatis blandit imperdiet. Pellentesque lacinia mattis sapien vitae imperdiet. Aliquam quis varius metus, at elementum diam. Duis id hendrerit velit. Phasellus ornare eu enim vel tempor. Phasellus pharetra odio et ipsum feugiat tempus. In hac habitasse platea dictumst. Donec posuere diam at magna porttitor congue. Pellentesque vitae rutrum sem. Vestibulum vel iaculis leo, ac tincidunt orci. Duis tincidunt erat in lacinia tincidunt. Duis in elementum quam, vel aliquam purus.In mollis commodo magna ac venenatis. Donec elit ante, pretium quis purus vitae, ultricies hendrerit mauris. Curabitur facilisis facilisis placerat. Aenean ante felis, sollicitudin eu porta ac, semper ut purus. Suspendisse potenti. Vivamus mollis, leo mollis pharetra blandit, odio urna aliquam lectus, vitae vulputate turpis enim quis quam. Vivamus placerat interdum tortor ac volutpat. Donec nec velit id turpis tempor semper. Proin vulputate nisi id magna consequat, ut vulputate felis euismod. Sed a sodales risus. Nunc quis urna a felis posuere molestie. Vestibulum id dapibus urna. Cras in risus sed diam dictum facilisis. Aenean volutpat quis magna et semper. Donec eu tellus faucibus, finibus sapien cursus, gravida est. Curabitur sit amet iaculis purus.In hac habitasse platea dictumst. Sed ultricies egestas elit a tristique. Nunc facilisis, sapien nec auctor sagittis, dolor lorem hendrerit enim, eu tincidunt velit massa eu purus. Quisque mollis lacus velit, ut venenatis sem aliquam a. Maecenas id vestibulum elit. Suspendisse posuere urna id cursus mattis. Morbi suscipit nibh vel enim commodo, id lacinia libero viverra.Suspendisse eu placerat sem. Vestibulum rutrum purus nec mauris eleifend, eget ultricies elit rutrum. Fusce tristique lacinia placerat. Aliquam vitae aliquam est. In et massa mi. Donec mi libero, dignissim vitae ex et, auctor ornare massa. Quisque nec ipsum ex. Vivamus porttitor euismod turpis in convallis. Vestibulum congue dapibus nulla. In porta erat sed quam consequat."
# numeric_cipher = text_to_numeric_cipher(text)
# print(numeric_cipher)

# text_back = numeric_cipher_to_text(numeric_cipher)
# print(text_back)cls
