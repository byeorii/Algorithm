import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    numer = denom1*numer2 + denom2*numer1 # 분자
    denom = denom1 * denom2 # 분모
    gcd = math.gcd(denom, numer) # 최대공약수


        
    return [numer //gcd, denom //gcd]