import numpy as np

def bayes_theorem(P_E, P_F_given_E, P_F):
    return (P_E * P_F_given_E) / P_F

def calc_P_F_given_E(P_E_and_F, P_E):
    return P_E_and_F / P_E

def calc_P_E_given_F(P_E_and_F, P_F):
    return P_E_and_F / P_F
    
def bothChildMale_given_at_least_one_male():    
    # Prior or P(E) = both children to be males
    P_E = np.random.random()
    
    # Evidence or P(F) = at least one children to be male
    P_F = np.random.random()
    
    # P(E and F)
    P_E_and_F = P_E * P_F
    
    # Likelihood or P( F|E )
    P_F_given_E = calc_P_F_given_E(P_E_and_F, P_E)
    
    # Posterior or P( E|F )
    P_E_given_F = bayes_theorem(P_E, P_F_given_E, P_F)
    
    print('\n The probability of both children to be males ' +
          'given that at least one child to be male = %.2f \n' % P_E_given_F)

def bothChildFemale_given_elder_female():    
    # Prior or P(E) = both children to be females
    P_E = np.random.random()
    
    # Evidence or P(F) = elder child being a female
    P_F = np.random.random()
    
    # P(E and F)
    P_E_and_F = P_E * P_F
    
    # Likelihood or P( F|E )
    P_F_given_E = calc_P_F_given_E(P_E_and_F, P_E)
    
    # Posterior or P( E|F )
    P_E_given_F = bayes_theorem(P_E, P_F_given_E, P_F)
    
    print('\n The probability that both children are females, ' + 
          'given that the elder child is a female = %.2f\n' % P_E_given_F)

bothChildMale_given_at_least_one_male()
bothChildFemale_given_elder_female()
