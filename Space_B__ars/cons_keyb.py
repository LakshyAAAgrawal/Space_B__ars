import pygame

def cons_keyb(surface, cap_char):
    pygame.font.init()
    L=[['*','<','>'],['Q','W','E','R','T','Y','U','I','O','P'],['A','S','D','F','G','H','J','K','L'],['Z','X','C','V','B','N','M']]
    myfont = pygame.font.SysFont('Courier', 30)
    #myfont2 = pygame.font.SysFont('Courier',20)
    myfont3 = pygame.font.SysFont('Courier',30,bold=True)
    ic=0
    inc=0
    inc1=0
    inc3=0
    s=pygame.Surface((931,380))
    s.set_alpha(50)
    s.fill((255,255,255))
    surface.blit(s,(46.5,380))
    #pygame.draw.rect(surface,(255,255,255,100),pygame.Rect(46.5,380,931,380))
    for p in range(3):
        s1=pygame.Surface((44.3+22.15,47.5))
        s1.set_alpha(64)
        s1.fill((0,119,255))
        surface.blit(s1,(90.8+44.3+88.6+88.6+88.6+ic-22.15,403.75))
        #pygame.draw.rect(surface,(66,71,104), pygame.Rect(90.8+44.3+88.6+88.6+88.6+ic-22.15, 403.75, 44.3+22.15, 47.5))
        textsurface = myfont.render((L[0])[p], True, (255,255,255))
        surface.blit(textsurface, (148+46.5+88.6+88.6+44.3 + ic-22.15, 417))
        if L[0][p] in cap_char:
            s1 = pygame.Surface((44.3 + 22.15, 47.5))
            s1.set_alpha(255)
            s1.fill((0, 119, 255))
            surface.blit(s1, (90.8 + 44.3 + 88.6 + 88.6 + 88.6 + ic - 22.15, 403.75))
            pygame.draw.rect(surface, (0,0,255),pygame.Rect(90.8 + 44.3 + 88.6 + 88.6 + 88.6 + ic-22.15, 403.75, 44.3+22.15, 47.5))
            textsurface = myfont3.render((L[0])[p], True, (255,255,255))
            surface.blit(textsurface, (148 + 46.5 + 88.6 + 88.6 + 44.3 + ic-22.15, 417))
        ic+=88.6

    for i in range(10):
        s2=pygame.Surface((44.3+10,47.5))
        s2.set_alpha(64)
        s2.fill((0,119,255))
        surface.blit(s2,(90.8+inc-10,475))
        #pygame.draw.rect(surface, (0,255,255,0.5),pygame.Rect(90.8+inc-10,475,44.3+10,47.5))
        textsurface = myfont.render((L[1])[i], True, (255, 255,255))
        surface.blit(textsurface, (100 + inc-5, 488.25))
        if L[1][i].lower() in cap_char:
            s2 = pygame.Surface((44.3 + 10, 47.5))
            s2.set_alpha(255)
            s2.fill((0, 119, 255))
            surface.blit(s2, (90.8 + inc - 10, 475))
            #pygame.draw.rect(surface, (255, 0, 255),pygame.Rect(90.8+inc -10,475, 44.3+10, 47.5))
            textsurface = myfont3.render((L[1])[i], True, (255, 255, 255))
            surface.blit(textsurface, (100 + inc-5, 488.25))
        inc+=88.6
    for j in range(9):
        s3 = pygame.Surface((44.3 + 10, 47.5))
        s3.set_alpha(64)
        s3.fill((0, 119, 255))
        surface.blit(s3, (90.8+44.3 + inc1-10, 546.25))
        #pygame.draw.rect(surface, (0, 255, 255,0.5), pygame.Rect(90.8+44.3 + inc1-10, 546.25, 44.3+10, 47.5))
        textsurface = myfont.render((L[2])[j], True, (255, 255,255))
        surface.blit(textsurface, (90.8+44.3+10.2 + inc1-5, 559.5))
        if L[2][j].lower() in cap_char:
            s3 = pygame.Surface((44.3 + 10, 47.5))
            s3.set_alpha(255)
            s3.fill((0, 119, 255))
            surface.blit(s3, (90.8 + 44.3 + inc1 - 10, 546.25))
            #pygame.draw.rect(surface, (255, 0, 255),pygame.Rect(90.8+inc1+44.3-10 ,546.25, 44.3+10, 47.5))
            textsurface = myfont3.render((L[2])[j], True, (255, 255, 255))
            surface.blit(textsurface, (90.8 + 44.3 + 10.2 + inc1-5, 559.5))
        inc1 += 88.6
    #for k in range(10):
        #pygame.draw.rect(surface, (0, 255, 255), pygame.Rect(44.3 + inc2, 546.25, 44.3, 47.5))
        #inc2 += 88.6
    for l in range(7):
        s3 = pygame.Surface((44.3 + 10, 47.5))
        s3.set_alpha(64)
        s3.fill((0, 119, 255))
        surface.blit(s3, (90.8+44.3+88.6+ inc3-10,617.5))
        #pygame.draw.rect(surface, (0, 255, 255,0.5), pygame.Rect(90.8+44.3+88.6+ inc3-10,617.5, 44.3+10, 47.5))
        textsurface = myfont.render((L[3])[l], True, (255, 255,255))
        surface.blit(textsurface, (90.8 + 44.3 + 88.6+10.2 + inc3-5, 630.75))
        if L[3][l].lower() in cap_char:
            s3 = pygame.Surface((44.3 + 10, 47.5))
            s3.set_alpha(255)
            s3.fill((0, 119, 255))
            surface.blit(s3, (90.8 + 44.3 + 88.6 + inc3 - 10, 617.5))
            #pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(90.8+44.3+88.6+ inc3-10,617.5 , 44.3+10, 47.5))
            textsurface = myfont3.render((L[3])[l], True, (255, 255, 255))
            surface.blit(textsurface, (90.8 + 44.3 + 10.2+88.6 + inc3, 630.75))
        inc3 += 88.6
    s4=pygame.Surface((177.2+44.3+22.15+22.15+22.15+22.15,41))
    s4.set_alpha(255)
    s4.fill((0,119,255))
    surface.blit(s4,(423.4-44.3-22.15-22.15,688.75))
    #pygame.draw.rect(surface,(0,255,255,0.5),pygame.Rect(423.4-44.3-22.15-22.15,688.75,177.2+44.3+22.15+22.15+22.15+22.15,41))
    if '_' in cap_char:
        pygame.draw.rect(surface, (255,0,255,0.5), pygame.Rect(423.4-44.3-22.15-22.15, 688.75, 177.2 + 44.3+44.3+22.15+22.15, 41))
    #pygame.draw.rect(surface,(0,255,255,0.5),pygame.Rect(423.4+177.2+44.3+44.3,688.75,88.6+44.3,47.5))
    #textsurface = myfont2.render("Enter", True, (255, 0, 0))
    #surface.blit(textsurface,((423.4+177.2+44.3+44.3+25,699)))

