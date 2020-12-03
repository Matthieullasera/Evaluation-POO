#cette classe utilise comme exemple les cartes Ultimate team dans fifa (voir photo en dessous du code)
class carte_joueur :
    
    maillot = 1

    def __init__(self,vit,dri,tir,defe,pas,phy):
        
        self.vit = vit
        self.dri = dri
        self.tir = tir
        self.defe = defe
        self.pas = pas
        self.phy = phy
    
    @classmethod
    def celebration(cls):
        cls.maillot -= 1 
    
    

class Joueur_basique(carte_joueur) : 

    def __init__(self,vit,dri,tir,defe,pas,phy,club,nom):
        super().__init__(vit,dri,tir,defe,pas,phy)
        self.club = club
        self.nom = nom

    def __str__ (self):
        return f"{self.nom}, Club :{self.club}, Vitesse :{self.vit}, Dribble: {self.dri}, Tir: {self.tir}, Defense: {self.defe}, Passe: {self.pas}, Physique: {self.phy}"
    
    
    def entrainement_vitesse(self,new_vit,nom):
        self.new_vit = new_vit
        self;nom = nom
        print(nom,"s'entrainé et a obtenu une augmentation en vitesse de :",new_vit)


class Joueur_boost(Joueur_basique):
    def __init__(self,vit,dri,tir,defe,pas,phy,club,nom):
        super().__init__(vit+2,dri+3,tir+3,defe+2,pas+1,phy+2,club,nom)




Giroud_base = Joueur_basique(39,71,79,42,70,77,"Chelsea","Giroud Basique")
Mbappe_base = Joueur_basique(96,91,86,39,78,76,"PSG","Mbappe Basique")
Mbappe_boost = Joueur_boost(96,91,86,39,78,76,"PSG","Mbappe Boost")
Giroud_boost = Joueur_boost(39,71,79,42,70,77,"Chelsea","Giroud Boost")
print(Mbappe_base)
print(Mbappe_boost)
print(Giroud_base)
print(Giroud_boost)
Giroud_base.entrainement_vitesse(4,"Giroud")
