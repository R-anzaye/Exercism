
def is_criticality_balanced(temperature, neutrons_emitted):
    emmision = temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and emmision < 500000 :
        return True
    else:
        return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage = (generated_power/theoretical_max_power) * 100 

    if percentage >= 80 :
        return "green"
    elif percentage < 80 and percentage >= 60 :
        return "orange"
    elif percentage < 60 and percentage >= 30 :
        return "red"
    elif percentage < 30 :
        return "black"
    else:
        return False


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    percentage = ((temperature * neutrons_produced_per_second)/threshold) * 100

    if percentage < 90 :
        return "LOW"
    elif (percentage >= 90 and percentage <=100)or (percentage > 100 and percentage <=110)   :
        return "NORMAL"
    else :
        return "DANGER"
   
