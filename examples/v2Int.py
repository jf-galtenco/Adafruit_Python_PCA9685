
def v2Int(v,vmax,Imax):
    from math import floor    
    #transforem la consigne voltage en consigne pwm entre 0 et 4095
    # attention ce nest pas extremement precis mais ca suffit dans une boucle de controle relative
    return floor(Imax*v/vmax)
